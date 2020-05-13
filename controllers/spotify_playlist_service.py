from objects.track import Track, SpotifyTrack
from objects.playlist import Playlist
from typing import List
from interfaces.playlist_service import PlaylistService
import constants
import requests
from flask import session

class SpotifyPlaylistService(PlaylistService):

    def get_playlist(self, id): 
        URI = constants.GET_SPOTIFY_PLAYLIST_URI + id
        header = { "Authorization" : "Bearer" + session[constants.SPOTIFY_CREDENTIALS]}
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
        return NotImplementedError 

    def search_playlist_tracks(self, tracks: Track):
        return NotImplementedError

    def sync_playlist(self, playlist: Playlist):
        return NotImplementedError

    def update_playlist(self, playlist_id: int, track_ids: List[int]):
        return NotImplementedError 

    def create_playlist(self, playlist_title: str, track_ids: List[int]):
        return NotImplementedError 



