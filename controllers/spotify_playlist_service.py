from objects.track import Track, SpotifyTrack
from objects.playlist import Playlist
from typing import List
from interfaces.playlist_service import PlaylistService
import constants
import requests
from flask import session
import json

class SpotifyPlaylistService(PlaylistService):

    def get_playlist(self, id): 
        URI = constants.GET_SPOTIFY_PLAYLIST_URI + id
        header = { "Authorization" : "Bearer " + session[constants.SPOTIFY_CREDENTIALS]}
        res = requests.get(URI, headers = header).json()
        
        if "error" in res: 
            # how should we handle errors?  
            # probably should just pass it along for now 
            return res

        id = res["id"]
        title = res["name"] 
        tracks = []
        for track in res["tracks"]["items"]: 
            track_item = track["track"]
            track_id = track_item["id"] 
            name = track_item["name"] 
            artists = []
            for artist in track_item["artists"]: 
                artists.append(artist["name"])
            album = track_item["album"]["name"] 
            isrc = track_item["external_ids"]["isrc"]
            tracks.append(SpotifyTrack(track_id, name, artists[0], album, isrc, artists))

        return Playlist(id, title, tracks)

    def get_my_playlists(self): 
        header = { "Authorization" : "Bearer " + session[constants.SPOTIFY_CREDENTIALS]}
        res = requests.get(constants.GET_MY_SPOTIFY_PLAYLISTS_URI, headers = header).json()
        
        if "error" in res: 
            # how should we handle errors?  
            # probably should just pass it along for now 
            return res

        playlists = []

        for playlist in res["items"]: 
            id = playlist["id"]
            name = playlist["name"]
            playlists.append(Playlist(id, name))
        
        return playlists 

    def search_playlist_track(self, query, header): 
        URI = constants.SEARCH_SPOTIFY + "?q=" + query + "&type=track" 
        res = requests.get(URI, headers = header).json()
        return res

    def search_playlist_tracks(self, tracks: Track):
        # need to query without the artist aswell 
        track_ids = []
        missing_tracks = []
        header = { "Authorization" : "Bearer " + session[constants.SPOTIFY_CREDENTIALS]}
        for track in tracks: 
            track_name = track.name
            query = track.artist + " " + track_name 
            res = self.search_playlist_track(query, header)

            if "error" in res: 
                return res

            while track_name != self.remove_paranthesis(track_name) and res["tracks"]["total"] == 0: 
                track_name = self.remove_paranthesis(track_name)
                query = track.artist + " " + track_name 
                res = self.search_playlist_track(query, header)

            if res["tracks"]["total"] == 0:
                res = self.search_playlist_track(track.name, header)
                
            if res["tracks"]["total"] == 0 : 
                missing_tracks.append(track)
            else: 
                track_ids.append(res["tracks"]["items"][0]["id"])

        return {"track_ids" : track_ids, "missing_tracks" : missing_tracks}

    # def sync_playlist(self, playlist: Playlist):
    #     my_playlists = self.get_my_playlists()
    #     track_ids = self.search_playlist_tracks(playlist.tracks)

    #     for my_playlist in my_playlists: 
    #         if playlist.title == my_playlist.title: 
    #             res = self.update_playlist(my_playlist.id, track_ids)
    #             # res is the track ids which were added, or an error if unsuccessful
    #             return res
        
    #     playlist_id = self.create_playlist(playlist.title)
    #     print("playlist_id", playlist_id)

    #     res = self.update_playlist(playlist_id, track_ids)
    #     return res

    def update_playlist(self, playlist_id: int, track_ids: List[int]):
        header = { "Authorization" : "Bearer " + session[constants.SPOTIFY_CREDENTIALS]}
        # error prone
        playlist = self.get_playlist(playlist_id)
        playlist_track_ids = []
        for track in playlist.tracks:
            playlist_track_ids.append(track.id)

        tracks_to_add = self.remove_existing(track_ids, playlist_track_ids)
        # if there are no tracks to add this request shouldnt be made 
        if len(tracks_to_add) == 0: 
            return tracks_to_add
        str_ids = "spotify:track:" + ',spotify:track:'.join(str(id) for id in tracks_to_add)
        URI = constants.GET_SPOTIFY_PLAYLIST_URI + "{0}/tracks?uris={1}".format(playlist_id, str_ids)
        res = requests.post(URI, headers = header).json()

        if "error" in res: 
            return res
        # else return the tracks which were added
        return tracks_to_add 

    def get_current_user(self):
        header = { "Authorization" : "Bearer " + session[constants.SPOTIFY_CREDENTIALS]}
        res = requests.get(constants.GET_SPOTIFY_CURRENT_USER, headers = header) 
        if(res.ok): 
            return res.json()
        # how to handle this error
        return "error"

    def create_playlist(self, playlist_title: str):
        user = self.get_current_user()
        if user == "error": 
            # still poor error handling 
            return "not authenticated"
        id = user["id"] 
        header = { "Authorization" : "Bearer " + session[constants.SPOTIFY_CREDENTIALS]}
        URI = constants.CREATE_SPOTIFY_PLAYLIST + id + "/playlists"
        body = { "name" : playlist_title}
        res = requests.post(URI, data = json.dumps(body), headers = header)
        if(res.ok): 
            return res.json()["id"]
        return "error" 



