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

class GetMyPlaylistsTest(unittest.TestCase): 

    def setUp(self): 
        self.spotify_service = SpotifyPlaylistService()

    def validate_playlist(self, ps1, ps2): 
        self.assertEqual(len(ps1), len(ps2))
        for i in range(len(ps1)):
            self.assertEqual(ps1[i].id, ps2[i].id)
            self.assertEqual(ps1[i].title, ps2[i].title)

    @patch("controllers.spotify_playlist_service.session")
    @patch("controllers.spotify_playlist_service.requests.get")
    def test_get_playlists_authenticated(self, mock_get, mock_session): 
        mock_session.return_value = None
        mock_get.return_value.json.return_value = spotify_data.playlists_json_mock
        res = self.spotify_service.get_my_playlists()
        self.validate_playlist(res, spotify_data.playlists_mock)

    @patch("controllers.spotify_playlist_service.session")
    @patch("controllers.spotify_playlist_service.requests.get")
    def test_get_playlists_unauthenticated(self, mock_get, mock_session): 
        mock_session.return_value = None
        mock_get.return_value.json.return_value = spotify_data.invalid_token_mock
        res = self.spotify_service.get_my_playlists()
        self.assertEqual(res, spotify_data.invalid_token_mock)

class SearchTrackTest(unittest.TestCase): 

    def setUp(self): 
        self.spotify_service = SpotifyPlaylistService()

    @patch("controllers.spotify_playlist_service.session")
    def test_get_playlists_authenticated(self, mock_session): 
        mock_session.return_value = None
        self.spotify_service.search_playlist_track = Mock(return_value = spotify_data.track_search_json_mock)
        res = self.spotify_service.search_playlist_tracks(spotify_data.tracks)
        self.assertEqual(res, spotify_data.track_ids)

    @patch("controllers.spotify_playlist_service.session")
    def test_get_playlists_authenticated_looponce(self, mock_session): 
        mock_session.return_value = None
        self.spotify_service.search_playlist_track = Mock(side_effect = [spotify_data.no_results_mock, spotify_data.track_search_json_mock])
        res = self.spotify_service.search_playlist_tracks(spotify_data.tracks)
        self.assertEqual(res, spotify_data.track_ids)

    @patch("controllers.spotify_playlist_service.session")
    def test_get_playlists_unauthenticated(self, mock_session): 
        mock_session.return_value = None
        self.spotify_service.search_playlist_track = Mock(return_value = spotify_data.invalid_token_mock)
        res = self.spotify_service.search_playlist_tracks(spotify_data.tracks)
        self.assertEqual(res, spotify_data.invalid_token_mock)

class UpdatePlaylistTest(unittest.TestCase): 

    def setUp(self): 
        self.spotify_service = SpotifyPlaylistService()

    @patch("controllers.spotify_playlist_service.session")
    @patch("controllers.spotify_playlist_service.requests.post")
    def test_update_playlist(self, mock_post, mock_session): 
        self.spotify_service.get_playlist = Mock(return_value = spotify_data.playlist_mock)

        mock_session.return_value = None
        mock_post.return_value.json.return_value = spotify_data.successful_update_mock

        res = self.spotify_service.update_playlist("6UFxJtxcVnP9tzmt4mnuJS", spotify_data.tracks_to_add)

        self.assertEqual(res, ["6f88cBp9BBpWGxZGm8iWdm"])

    @patch("controllers.spotify_playlist_service.session")
    @patch("controllers.spotify_playlist_service.requests.post")
    def test_update_unauthenticated(self, mock_post, mock_session): 
        self.spotify_service.get_playlist = Mock(return_value = spotify_data.playlist_mock)

        mock_session.return_value = None
        mock_post.return_value.json.return_value = spotify_data.invalid_token_mock

        res = self.spotify_service.update_playlist("6UFxJtxcVnP9tzmt4mnuJS", spotify_data.tracks_to_add)

        self.assertEqual(res, spotify_data.invalid_token_mock)

class CreatePlaylistTest(unittest.TestCase): 
    
    def setUp(self): 
        self.spotify_service = SpotifyPlaylistService()

    @patch("controllers.spotify_playlist_service.session")
    @patch("controllers.spotify_playlist_service.requests.post")
    def test_create_playlist(self, mock_post, mock_session): 
        mock_session.return_value = None  
        mock_post.return_value.ok = True 
        mock_post.return_value.json.return_value = spotify_data.playlist_creation_mock
        self.spotify_service.get_current_user = Mock(return_value = spotify_data.user_json_mock)
        
        res = self.spotify_service.create_playlist("new palylsit")
        self.assertEqual("5WbpjFKUylN0Q80q7eKaen", res)

    @patch("controllers.spotify_playlist_service.session")
    @patch("controllers.spotify_playlist_service.requests.post")
    def test_create_playlist_failure(self, mock_post, mock_session): 
        mock_session.return_value = None  
        mock_post.return_value.ok = False 
        mock_post.return_value.json.return_value = spotify_data.invalid_token_mock
        self.spotify_service.get_current_user = Mock(return_value = spotify_data.user_json_mock)
        
        res = self.spotify_service.create_playlist("new palylsit")
        self.assertEqual("error", res)

    @patch("controllers.spotify_playlist_service.session")
    @patch("controllers.spotify_playlist_service.requests.post")
    def test_create_playlist_failure2(self, mock_post, mock_session): 
        self.spotify_service.get_current_user = Mock(return_value = "error")
        
        res = self.spotify_service.create_playlist("new palylsit")
        self.assertEqual("not authenticated", res)

class GetUserTest(unittest.TestCase): 
    
    def setUp(self): 
        self.spotify_service = SpotifyPlaylistService()

    @patch("controllers.spotify_playlist_service.session")
    @patch("controllers.spotify_playlist_service.requests.post")
    def test_get_user_success(self, mock_post, mock_session): 
        mock_session.return_value = None  
        mock_post.return_value.ok = True 
        mock_post.return_value.json.return_value = spotify_data.user_json_mock

        res = self.spotify_service.get_current_user()
        self.assertEqual(spotify_data.user_json_mock, res)

    @patch("controllers.spotify_playlist_service.session")
    @patch("controllers.spotify_playlist_service.requests.post")
    def test_get_user_failure(self, mock_post, mock_session): 
        mock_session.return_value = None  
        mock_post.return_value.ok = False 

        res = self.spotify_service.get_current_user()
        self.assertEqual("error", res)

class SyncPlaylistTest(unittest.TestCase): 

    def setUp(self): 
        self.spotify_service = SpotifyPlaylistService()

    def test_sync_playlist_update(self): 
        self.spotify_service.get_my_playlists = Mock(return_value = spotify_data.playlists_mock)
        self.spotify_service.search_playlist_tracks = Mock(return_value = spotify_data.track_ids)
        self.spotify_service.update_playlist = Mock(return_value = spotify_data.track_ids)

        res = self.spotify_service.sync_playlist(spotify_data.playlist_mock)
        self.assertTrue(self.spotify_service.update_playlist.called)
        self.assertEqual(spotify_data.track_ids, res)

    def test_sync_playlist_create(self): 
        self.spotify_service.get_my_playlists = Mock(return_value = [])
        self.spotify_service.search_playlist_tracks = Mock(return_value = spotify_data.track_ids)
        self.spotify_service.create_playlist = Mock(return_value = "6UFxJtxcVnP9tzmt4mnuJS")
        self.spotify_service.update_playlist = Mock(return_value = spotify_data.track_ids)

        res = self.spotify_service.sync_playlist(spotify_data.playlist_mock)
        self.assertTrue(self.spotify_service.create_playlist.called)
        self.assertEqual(spotify_data.track_ids, res)