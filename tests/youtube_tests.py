import unittest
from unittest.mock import Mock, patch
from controllers.youtube_playlist_service import YoutubePlaylistService
from objects.track import Track
from objects.playlist import Playlist
from tests.mock_data import youtube_data

class RemoveExistingTracksTest(unittest.TestCase): 
    
    @patch.object(YoutubePlaylistService, '__init__', return_value=None)
    def setUp(self, mock_init): 
        self.youtube_service = YoutubePlaylistService()


    def test_remove_existing_tracks_one_dub(self):
        self.youtube_service.get_playlist = Mock(return_value = youtube_data.playlist_mock)

        cleaned_tracks = self.youtube_service.remove_existing_tracks(123, youtube_data.tracks_mock)

        self.assertEqual(1, len(cleaned_tracks))

    def test_remove_existing_tracks_no_dubs(self):
        self.youtube_service.get_playlist = Mock(return_value = Playlist(121, "test", []))

        cleaned_tracks = self.youtube_service.remove_existing_tracks(123, youtube_data.tracks_mock)

        self.assertEqual(2, len(cleaned_tracks))


if __name__ == '__main__':
    unittest.main()