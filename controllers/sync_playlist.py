from controllers.youtube_playlist_service import YoutubePlaylistService
from controllers.deezer_playlist_service import DeezerPlaylistService
from typing import List
from objects.playlist import Playlist

class SyncPlaylist:

    def sync_playlist(self, playlist: Playlist, sync_with: List[str]): 
        youtube_service = YoutubePlaylistService()
        deezer_service = DeezerPlaylistService()
        for service in sync_with: 
            if service == 'deezer': 
                deezer_service.sync_playlist(playlist)
            elif service == 'youtube':
                youtube_service.sync_playlist(playlist)