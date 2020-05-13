import unittest
from controllers.spotify_playlist_service import SpotifyPlaylistService
from unittest.mock import Mock, patch
from tests.mock_data import spotify_data

class GetPlaylistTest(unittest.TestCase): 

    def setUp(self): 
        self.spotify_service = SpotifyPlaylistService()

    def validate_playlist(self, p1, p2): 
        self.assertEqual(p1.id, p2.id)
        self.assertEqual(p1.title, p2.title)
        self.assertEqual(len(p1.tracks), len(p2.tracks))
        for i in range(len(p1.tracks)): 
            self.assertEqual(p1.tracks[i].id, p2.tracks[i].id)
            self.assertEqual(p1.tracks[i].name, p2.tracks[i].name)
            self.assertEqual(p1.tracks[i].artist, p2.tracks[i].artist)

    @patch("controllers.spotify_playlist_service.session")
    @patch("controllers.spotify_playlist_service.requests.get")
    def test_get_valid_playlist(self, mock_get, mock_session): 
        mock_session.return_value = None
        mock_get.return_value.json.return_value = spotify_data.playlist_json_mock
        res = self.spotify_service.get_playlist("6UFxJtxcVnP9tzmt4mnuJS")
        self.validate_playlist(res, spotify_data.playlist_mock)

    @patch("controllers.spotify_playlist_service.session")
    @patch("controllers.spotify_playlist_service.requests.get")
    def test_get_invalid_playlist(self, mock_get, mock_session): 
        mock_session.return_value = None
        mock_get.return_value.json.return_value = spotify_data.invalid_id_mock
        res = self.spotify_service.get_playlist("6UFxJtxcVnP9tzmt4mnuJS")
        self.assertEqual(spotify_data.invalid_id_mock, res)

    @patch("controllers.spotify_playlist_service.session")
    @patch("controllers.spotify_playlist_service.requests.get")
    def test_get_invalid_token(self, mock_get, mock_session): 
        mock_session.return_value = None
        mock_get.return_value.json.return_value = spotify_data.invalid_token_mock
        res = self.spotify_service.get_playlist("6UFxJtxcVnP9tzmt4mnuJS")
        self.assertEqual(spotify_data.invalid_token_mock, res)
