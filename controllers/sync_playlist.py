from controllers.youtube_playlist_service import YoutubePlaylistService
from controllers.deezer_playlist_service import DeezerPlaylistService
from controllers.spotify_playlist_service import SpotifyPlaylistService
from typing import List
from objects.playlist import Playlist

class SyncPlaylist:

    def sync_playlist(self, playlist: Playlist, sync_with: List[str]): 
        for service in sync_with: 
            if service == 'deezer': 
                deezer_service = DeezerPlaylistService()
                deezer_service.sync_playlist(playlist)
            elif service == 'youtube':
                youtube_service = YoutubePlaylistService()
                youtube_service.sync_playlist(playlist)
            elif service == 'spotify': 
                spotify_service = SpotifyPlaylistService()
                spotify_service.sync_playlist(playlist)