import googleapiclient.discovery
import google.oauth2.credentials
import requests
from objects.track import Track 
from objects.playlist import Playlist
import flask
from interfaces.playlist_service import PlaylistService
from typing import List
import difflib

class YoutubePlaylistService(PlaylistService): 

    # api_service_name = None
    # api_version = None
    # youtube = None

    def __init__(self): 
        api_service_name = "youtube"
        api_version = "v3"
        credentials = google.oauth2.credentials.Credentials(
            **flask.session['youtube_credentials'])
        self.youtube = googleapiclient.discovery.build(
                api_service_name, api_version, credentials=credentials )

    # getting the name of a playlist
    # current testing playlist "PLBY2oJTdHuT9A0PqU4UIdtECNliQhWM6-"
    def get_playlist_title(self, id):
        request = self.youtube.playlists().list(
            part="snippet",
            id=id
        )
        response = request.execute()
        return response['items'][0]['snippet']['title']

    # start of the songs retrieval
    def get_playlist_tracks(self, id):
        response = {}
        tracks = []
        # used to initially enter the while loop 
        flag = True
        while "nextPageToken" in response or flag: 
            flag = False
            request = self.youtube.playlistItems().list(
                part="id, snippet", 
                playlistId=id, 
                maxResults=50, 
                pageToken=response["nextPageToken"] if "nextPageToken" in response else ""
            )

            response = request.execute()
            for track in response['items']:
                if 'Private video' == track['snippet']['title']:
                    continue
                # request to get the channel name, which is most often associated with 
                # the artist 
                request2 = self.youtube.videos().list(
                    part="snippet",
                    id=track['snippet']['resourceId']['videoId']
                )
                response2 = request2.execute()
                artist = response2['items'][0]['snippet']['channelTitle']
                # some common anotation which needs to be removed
                artist = artist.replace('- Topic', '')
                track = Track(track['snippet']['resourceId']['videoId'], track['snippet']['title'], artist)
                tracks.append(track)

        return tracks

    def get_playlist(self, id): 
        title = self.get_playlist_title(id) 
        tracks = self.get_playlist_tracks(id) 
        return Playlist(id, title, tracks)

    def get_my_playlists(self):
        request = self.youtube.playlists().list(
                part="snippet",
                mine=True
            )
        res = request.execute()
        my_playlists = []
        for playlist in res['items']:
            id = playlist['id']
            title = playlist['snippet']['title']
            my_playlists.append(Playlist(id, title))
        return my_playlists

    def query_track(self, track):
        response = None
        if hasattr(track, 'isrc'):
            request = self.youtube.search().list(
                part = "snippet", 
                q = track.isrc
            )
            response = request.execute()
        if response == None or len(response['items']) == 0: 
            request = self.youtube.search().list(
                part = "snippet", 
                q = "{0} - {1}".format(track.artist, track.name)
            )
            response = request.execute()
        if len(response['items']) == 0: 
            print('query')
            print("{0} - {1}".format(track.artist, track.name))
        return response

    def search_playlist_tracks(self, tracks: List[Track]):
        track_ids = [] 
        missing_tracks = []

        for track in tracks: 
            response = self.query_track(track)
            # response might not always have tracks 
            if len(response['items']) == 0: 
                missing_tracks.append(track)
                continue
            track_id = response['items'][0]['id']['videoId']
            track_ids.append(track_id)
        return {"track_ids" : track_ids, "missing_tracks" : missing_tracks}

    def remove_existing_tracks(self, playlist_id: Playlist, tracks: List[Track]) -> List[Track]: 
        tracks_to_remove = []
        playlist = self.get_playlist(playlist_id)
        # messy implementation, basically going through each track and comparing it to those in the playlist
        # could get this down to O(n+m) not worth the effort right now 
        for search_track in tracks: 
            for playlist_track in playlist.tracks: 
                seq = difflib.SequenceMatcher(isjunk=None, a=playlist_track.name, b=search_track.name)
                if seq.ratio() > .8: 
                    tracks_to_remove.append(search_track)
                    break

        for track in tracks_to_remove: 
            tracks.remove(track)

        return tracks

    def sync_playlist(self, playlist):
        my_playlists = self.get_my_playlists()

        for my_playlist in my_playlists: 
            if playlist.title == my_playlist.title:
                # since youtube imposes such a low quota we need to remove the songs
                # that are already found in the playlist so we dont end up searching for 
                # duplicates 
                cleaned_tracks = self.remove_existing_tracks(my_playlist.id, playlist.tracks)
                track_results = self.search_playlist_tracks(cleaned_tracks)
                self.update_playlist(my_playlist.id, track_results["track_ids"])
                # what shitty return types, I should definitely beable to see the 
                # songs that were and werent added in the response 
                return track_results["missing_tracks"]
        
        track_results = self.search_playlist_tracks(playlist.tracks)
        self.create_playlist(playlist.title, track_results["track_ids"])
        return track_results["missing_tracks"] 

    def insert_track(self, playlist_id, track_id): 
        request = self.youtube.playlistItems().insert(
            part="snippet",
            body={
                    "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                    "kind": "youtube#video",
                    "videoId": track_id
                    }
                }
            }
        )
        return request.execute()

    def update_playlist(self, playlist_id, track_ids):
        # we need to make sure we are not adding any songs that are already found in the playlist 
        # first get all the songs in the current playlist 
        playlist_tracks = self.get_playlist_tracks(playlist_id)
        playlist_ids = [] 
        for track in playlist_tracks: 
            playlist_ids.append(track.id)

        # then compare the lists and remove any duplicate tracks 
        track_ids_to_add = self.remove_existing(self.remove_duplicates(track_ids), self.remove_duplicates(playlist_ids))
        # if there are no tracks to add this request shouldnt be made 
        if len(track_ids_to_add) == 0: 
            return track_ids_to_add
        for track_id in track_ids_to_add: 
            self.insert_track(playlist_id, track_id)
            # validate response 

    def create_playlist(self, playlist_title, track_ids):
        request = self.youtube.playlists().insert(
            part="snippet", 
            body={
                "snippet": {
                    "title": playlist_title
                }
            }
        )
        response = request.execute()
        playlist_id = response['id'] 
        self.update_playlist(playlist_id, track_ids)

    # # duplicate code remove TODO 
    # def remove_existing(self, tracks_to_add, playlist_tracks):
    #     # two pointer approach on sorted arrays 
    #     non_dublicates = []
    #     tracks_to_add.sort()
    #     playlist_tracks.sort()
    #     i = 0 
    #     j = 0
    #     while i < len(tracks_to_add) and j < len(playlist_tracks):
    #         if tracks_to_add[i] < playlist_tracks[j]:
    #             non_dublicates.append(tracks_to_add[i])
    #             i += 1
    #         elif tracks_to_add[i] > playlist_tracks[j]:
    #             j += 1
    #         else:
    #             i += 1 
    #             j += 1
    #     while i < len(tracks_to_add):
    #         non_dublicates.append(tracks_to_add[i])
    #         i += 1
    #     return non_dublicates

    # def remove_duplicates(self, track_ids):
    #     return list(dict.fromkeys(track_ids))