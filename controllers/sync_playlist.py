from controllers.youtube_playlist_service import YoutubePlaylistService
from controllers.deezer_playlist_service import DeezerPlaylistService
from controllers.spotify_playlist_service import SpotifyPlaylistService
from typing import List
from objects.playlist import Playlist

class SyncPlaylist:

    def sync_playlist(self, playlist: Playlist, sync_with: List[str]): 
        for service in sync_with: 
            res = None
            if service == 'deezer': 
                deezer_service = DeezerPlaylistService()
                # so here is where we want to return the items that were not successfully added
                res = deezer_service.sync_playlist(playlist)
            elif service == 'youtube':
                youtube_service = YoutubePlaylistService()
                # so here is where we want to return the items that were not successfully added
                res = youtube_service.sync_playlist(playlist)
            elif service == 'spotify': 
                spotify_service = SpotifyPlaylistService()
                # so here is where we want to return the items that were not successfully added
                res = spotify_service.sync_playlist(playlist)

            print("syncing with: " + service)
            # still making a request even when there no songs to sync
            print(res)