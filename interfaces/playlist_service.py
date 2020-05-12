from abc import ABC, abstractmethod
from objects.track import Track
from objects.playlist import Playlist
from typing import List

class PlaylistService(ABC):

    @abstractmethod
    def get_playlist(self, id): 
        pass

    @abstractmethod
    def get_my_playlists(self): 
        pass 

    @abstractmethod
    def search_playlist_tracks(self, tracks: Track):
        pass

    @abstractmethod
    def sync_playlist(self, playlist: Playlist):
        pass

    @abstractmethod
    def update_playlist(self, playlist_id: int, track_ids: List[int]):
        pass 

    @abstractmethod
    def create_playlist(self, playlist_title: str, track_ids: List[int]):
        pass 

    def remove_paranthesis(self, track_name):
        flag = False
        start = -1
        end = -1
        for i in range(len(track_name)):
            if track_name[i] == '(':
                start = i
                flag = True
            if flag and track_name[i] == ')':
                end = i
                break 
        if end == -1 or start == -1: 
            return track_name 
        else:
            return track_name[:start] + track_name[end+1:]

    def remove_existing(self, tracks_to_add, playlist_tracks):
        # two pointer approach on sorted arrays 
        non_dublicates = []
        tracks_to_add.sort()
        playlist_tracks.sort()
        i = 0 
        j = 0
        while i < len(tracks_to_add) and j < len(playlist_tracks):
            if tracks_to_add[i] < playlist_tracks[j]:
                non_dublicates.append(tracks_to_add[i])
                i += 1
            elif tracks_to_add[i] > playlist_tracks[j]:
                j += 1
            else:
                i += 1 
                j += 1
        while i < len(tracks_to_add):
            non_dublicates.append(tracks_to_add[i])
            i += 1
        return non_dublicates

    def remove_duplicates(self, track_ids):
        return list(dict.fromkeys(track_ids))


