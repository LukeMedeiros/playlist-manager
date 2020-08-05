import requests
import flask
from objects.track import DeezerTrack 
from objects.playlist import Playlist
from interfaces.playlist_service import PlaylistService
import time

class DeezerPlaylistService(PlaylistService):

    def set_isrc(self, track):
        URI = "https://api.deezer.com/track/{0}".format(track.id)
        res = requests.get(URI).json() 
        track.set_isrc(res['isrc'])

    def get_playlist(self, id): 
        URI = "https://api.deezer.com/playlist/{0}".format(id)
        res = requests.get(URI).json()
        if "error" in res: 
            return res["error"]["type"]
        id = res['id']
        title = res['title'] 
        tracks = []
        for track in res['tracks']['data']:
            track = DeezerTrack(track['id'], track['title'], track['artist']['name'], track['album'])
            self.set_isrc(track)
            tracks.append(track)
        return Playlist(id, title, tracks)

    # get deezer songs
    def search_playlist_tracks(self, tracks): 
        track_ids = []
        missing_tracks = []
        for track in tracks:
            track_name = track.name 
            track_artist = track.artist
            URI = "https://api.deezer.com/search?q=artist:'" + track_artist +"' track:'"+ track_name+"'"
            res = requests.get(URI)
            data = res.json()
            
            # what if the artist is not actually the artist as it is just the channel name? need to try without the artist 
            # aswell 
            while track_name != self.remove_paranthesis(track_name) and data['total'] == 0:
                track_name = self.remove_paranthesis(track_name)
                URI = "https://api.deezer.com/search?q=artist:'" + track_artist +"' track:'"+ track_name+"'"
                res = requests.get(URI)
                data = res.json()

            if data['total'] == 0:
                URI = "https://api.deezer.com/search?q=track:" + track.name
                res = requests.get(URI)
                data = res.json()

            if data['total'] == 0:
                print('no match: ', track_name, track_artist)
                continue

            if len(data['data']) > 0:
                track_ids.append(data['data'][0]['id'])
            else: 
                missing_tracks.append(track)
        
        return {"track_id" : track_ids, "missing_tracks" : missing_tracks}

    def get_my_playlists(self):
        URI = 'https://api.deezer.com/user/me?access_token={0}'.format(flask.session['deezer_credentials'])
        res = requests.get(URI).json()
        # this error should never happen, does that mean we shouldnt test it?
        if "error" in res: 
            return res["error"]["type"]
        id = res['id']
        URI = 'https://api.deezer.com/user/me/playlists?access_token={0}'.format(flask.session['deezer_credentials'])
        res = requests.get(URI).json()
        playlists =[]
        for playlist in res['data']:
            if playlist['creator']['id'] == id:
                playlists.append(Playlist(playlist['id'], playlist['title']))
        return playlists

    def get_playlist_track_ids(self, playlist_id):
        playlist = self.get_playlist(playlist_id)
        if isinstance(playlist, str):
            return playlist
        track_ids = []
        for track in playlist.tracks: 
            track_ids.append(track.id)
        return track_ids

    def update_playlist(self, playlist_id, track_ids):
        # need to remove songs that are already in the playlist
        playlist_track_ids = self.get_playlist_track_ids(playlist_id)
        track_ids_to_add = self.remove_existing(self.remove_duplicates(track_ids), self.remove_duplicates(playlist_track_ids))
        # if there are no tracks to add this request shouldnt be made 
        if len(track_ids_to_add) == 0: 
            return track_ids_to_add
        str_ids = '[,' + ','.join(str(id) for id in track_ids_to_add) + ']'
        URI = 'https://api.deezer.com/playlist/{0}/tracks?songs={1}&access_token={2}'.format(playlist_id, str_ids, flask.session['deezer_credentials'])
        res = requests.post(URI).json()
        if "error" in res: 
            return res
        return track_ids_to_add

    def create_playlist(self, playlist_title):
        URI = 'https://api.deezer.com/user/me/playlists?title={0}&access_token={1}'.format(playlist_title, flask.session['deezer_credentials'])
        res = requests.post(URI).json()
        if "error" in res: 
            return res["error"]["type"]
        return res["id"] 

    # def sync_playlist(self, playlist):
    #     my_playlists = self.get_my_playlists()

    #     # deezer doesnt allow you to add duplicates so getting all tracks should be fine 
    #     track_ids = self.search_playlist_tracks(playlist.tracks)
    #     # check if the playlist title exists in my deezer library 
    #     for my_playlist in my_playlists:
    #         if playlist.title == my_playlist.title:
    #             # update the current playlist
    #             res = self.update_playlist(my_playlist.id, track_ids)
    #             if res == "true":
    #                 # maybe should give more information
    #                 return 'playlist updated'
    #             return res  
        
    #     # create a new playlist 
    #     playlist_id = self.create_playlist(playlist.title)
    #     self.update_playlist(playlist_id, track_ids)
    #     return 'playlist created'
