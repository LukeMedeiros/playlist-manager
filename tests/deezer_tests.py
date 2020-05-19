import unittest
from unittest.mock import Mock, patch
from controllers.deezer_playlist_service import DeezerPlaylistService
from tests.mock_data import deezer_data
from objects.track import DeezerTrack 

class RemoveExistingTest(unittest.TestCase):

    def setUp(self): 
        self.deezer_service = DeezerPlaylistService()

    def test_empty_playlist_and_tracks(self):
        tracks_to_add = []
        playlist_tracks = []
        cleaned_playlist = self.deezer_service.remove_existing(tracks_to_add, playlist_tracks)
        self.assertEqual([], cleaned_playlist)   

    def test_empty_playlist(self):
        tracks_to_add = [1, 2, 3] 
        playlist_tracks = []
        cleaned_playlist = self.deezer_service.remove_existing(tracks_to_add, playlist_tracks)
        self.assertEqual(tracks_to_add, cleaned_playlist)

    def test_no_conflicting_tracks(self):
        tracks_to_add = [1, 2, 3] 
        playlist_tracks = [4, 5, 6]
        cleaned_playlist = self.deezer_service.remove_existing(tracks_to_add, playlist_tracks)
        self.assertEqual(tracks_to_add, cleaned_playlist)

    def test_conflicting_tracks(self):
        tracks_to_add = [3, 1, 2, 6] 
        playlist_tracks = [2, 3]
        cleaned_playlist = self.deezer_service.remove_existing(tracks_to_add, playlist_tracks)
        self.assertEqual([1, 6], cleaned_playlist)

    def test_conflicting_tracks_str(self):
        tracks_to_add = ['6f88cBp9BBpWGxZGm8iWdm', '2DLqygtisuvhIUeV3aKJSe']
        playlist_tracks = ['2DLqygtisuvhIUeV3aKJSe']
        cleaned_playlist = self.deezer_service.remove_existing(tracks_to_add, playlist_tracks)
        self.assertEqual(['6f88cBp9BBpWGxZGm8iWdm'], cleaned_playlist)

class RemoveDuplicatesTest(unittest.TestCase):

    def setUp(self): 
        self.deezer_service = DeezerPlaylistService()

    def test_empty_tracks(self):
        tracks_to_add = []
        cleaned_playlist = self.deezer_service.remove_duplicates(tracks_to_add)
        self.assertEqual([], cleaned_playlist)  

    def test_one_duplicate(self):
        tracks_to_add = [1, 1]
        cleaned_playlist = self.deezer_service.remove_duplicates(tracks_to_add)
        self.assertEqual([1], cleaned_playlist)   

    def test_multiple_duplicates(self):
        tracks_to_add = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
        cleaned_playlist = self.deezer_service.remove_duplicates(tracks_to_add)
        self.assertEqual([1, 2, 3, 4], cleaned_playlist)   

class RemoveParanthesisTest(unittest.TestCase): 

    def setUp(self): 
        self.deezer_service = DeezerPlaylistService()

    def test_empty_string(self):
        empty_string = "" 
        self.assertEqual("", self.deezer_service.remove_paranthesis(empty_string))

    def test_one_paranthesis_set(self): 
        one_paranthesis_set = "()" 
        self.assertEqual("", self.deezer_service.remove_paranthesis(one_paranthesis_set))

    def test_two_paranthesis_set(self): 
        two_paranthesis_set = "() (still should exist)" 
        self.assertEqual(" (still should exist)", self.deezer_service.remove_paranthesis(two_paranthesis_set))

class GetPlaylistTest(unittest.TestCase): 

    def setUp(self): 
        self.deezer_service = DeezerPlaylistService()

    def check_playlist_values(self, playlist1, playlist2): 
        self.assertEqual(playlist1.id, playlist2.id)
        self.assertEqual(playlist1.title, playlist2.title)
        self.assertEqual(len(playlist1.tracks), len(playlist2.tracks))
        for i in range(len(playlist1.tracks)): 
            self.assertEqual(playlist1.tracks[i].id, playlist2.tracks[i].id)

    @patch('controllers.deezer_playlist_service.requests.get')
    def test_valid_id(self, mock_get):
        mock_get.return_value.json.return_value = deezer_data.playlist_json_mock
        self.deezer_service.set_isrc = Mock()

        playlist = self.deezer_service.get_playlist(908622995)
        self.assertTrue(mock_get.called)
        self.check_playlist_values(deezer_data.playlist_mock, playlist)

    @patch('controllers.deezer_playlist_service.requests.get')
    def test_invalid_id(self, mock_get): 
        mock_get.return_value.json.return_value = deezer_data.data_exception_mock
        self.deezer_service.set_isrc = Mock() 

        playlist = self.deezer_service.get_playlist(1)
        self.assertEqual("DataException", playlist)

class SetTrackISRCTest(unittest.TestCase):

    def setUp(self): 
        self.deezer_service = DeezerPlaylistService()

    @patch('controllers.deezer_playlist_service.requests.get')
    def test_valid_track(self, mock_get):
        mock_get.return_value.json.return_value = deezer_data.track_json_mock

        track = DeezerTrack("3135556", "Harder, Better, Faster, Stronger", "Daft Punk", "Discovery")
        self.deezer_service.set_isrc(track)
        self.assertTrue(mock_get.called)
        return_track = DeezerTrack("3135556", "Harder, Better, Faster, Stronger", "Daft Punk", "Discovery", "GBDUW0000059")
        self.assertEqual(return_track.isrc, track.isrc)

class GetMyPlaylistsTest(unittest.TestCase): 

    def setUp(self): 
        self.deezer_service = DeezerPlaylistService()

    @patch('controllers.deezer_playlist_service.flask.session')
    @patch('controllers.deezer_playlist_service.requests.get')
    def test_authenticated_user(self, mock_get, mock_session):
        mock_session.return_value = None
        mock_get.return_value.json.side_effect = [deezer_data.user_info_mock, deezer_data.all_playlists_mock]

        playlists = self.deezer_service.get_my_playlists()
        self.assertEqual(2, mock_get.call_count)
        self.assertEqual("2954914226", playlists[0].id)  


    @patch('controllers.deezer_playlist_service.flask.session')
    @patch('controllers.deezer_playlist_service.requests.get')
    def test_unauthenticated_user(self, mock_get, mock_session):
        mock_session.return_value = None
        mock_get.return_value.json.side_effect = [deezer_data.auth_error_mock, deezer_data.auth_error_mock]

        playlists = self.deezer_service.get_my_playlists()
        self.assertEqual(1, mock_get.call_count)
        self.assertEqual(deezer_data.errors[300], playlists)

class GetPlaylistTracksIdsTest(unittest.TestCase):

    def setUp(self): 
        self.deezer_service = DeezerPlaylistService()

    def test_valid_playlist(self):
        self.deezer_service.get_playlist = Mock(return_value = deezer_data.playlist_mock)
        track_ids = self.deezer_service.get_playlist_track_ids(908622995)
        self.assertEqual(["672264322"], track_ids)

    def test_invalid_playlist_id(self):
        self.deezer_service.get_playlist = Mock(return_value = deezer_data.errors[800])
        track_ids = self.deezer_service.get_playlist_track_ids("908622995")
        self.assertEqual(deezer_data.errors[800], track_ids)

class CreatePlaylistTest(unittest.TestCase): 
    def setUp(self): 
        self.deezer_service = DeezerPlaylistService()

    @patch('controllers.deezer_playlist_service.flask.session')
    @patch('controllers.deezer_playlist_service.requests.post')
    def test_authenticate_create(self, mock_post, mock_flask):
        playlist_mock = deezer_data.playlist_creation_mock
        mock_flask.return_value = None
        mock_post.return_value.json.return_value = playlist_mock
        playlist_id = self.deezer_service.create_playlist("test playlist")
        self.assertTrue(mock_post.called)
        self.assertEqual(playlist_mock["id"], playlist_id)

    @patch('controllers.deezer_playlist_service.flask.session')
    @patch('controllers.deezer_playlist_service.requests.post')
    def test_unauthenticate_create(self, mock_post, mock_flask):
        mock_post.return_value.json.return_value = deezer_data.auth_error_mock
        mock_flask.return_value = None
        playlist_id = self.deezer_service.create_playlist("test playlist")
        self.assertTrue(mock_post.called)
        self.assertEqual(deezer_data.errors[200], playlist_id)

class UpdatePlaylistTest(unittest.TestCase): 

    def setUp(self): 
        self.deezer_service = DeezerPlaylistService()

    @patch('controllers.deezer_playlist_service.flask.session')
    @patch('controllers.deezer_playlist_service.requests.post')
    def test_successful_update(self, mock_post, mock_flask):
        mock_flask.return_value = None
        mock_post.return_value.json.return_value = "true"
        self.deezer_service.get_playlist_track_ids = Mock(return_value = [])
        self.deezer_service.remove_duplicates = Mock(side_effect = [[69223545], []])
        self.deezer_service.remove_existing = Mock(return_value = [69223545])

        updated_successfully = self.deezer_service.update_playlist(7636096362, [69223545])
        self.assertEqual(updated_successfully, "true")

    @patch('controllers.deezer_playlist_service.flask.session')
    @patch('controllers.deezer_playlist_service.requests.post')
    def test_unauthenticated_update(self, mock_post, mock_flask):
        mock_flask.return_value = None
        mock_post.return_value.json.return_value = deezer_data.auth_error_mock
        self.deezer_service.get_playlist_track_ids = Mock(return_value = [])
        self.deezer_service.remove_duplicates = Mock(side_effect = [[69223545], []])
        self.deezer_service.remove_existing = Mock(return_value = [69223545])

        auth_error = self.deezer_service.update_playlist(7636096362, [69223545])
        self.assertEqual(auth_error, deezer_data.errors[200])

class SyncPlaylistTest(unittest.TestCase): 
    
    def setUp(self): 
        self.deezer_service = DeezerPlaylistService()

    def test_sync_by_update(self):
        playlist_mock = deezer_data.playlist_mock
        self.deezer_service.get_my_playlists = Mock(return_value = [playlist_mock])
        self.deezer_service.search_playlist_tracks = Mock(return_value = deezer_data.track_ids_mock)
        self.deezer_service.update_playlist = Mock(return_value = "true")

        res = self.deezer_service.sync_playlist(playlist_mock)
        self.assertEqual(res, "playlist updated")

    def test_sync_by_create(self):
        playlist_mock = deezer_data.playlist_mock
        self.deezer_service.get_my_playlists = Mock(return_value = [])
        self.deezer_service.search_playlist_tracks = Mock(return_value = deezer_data.track_ids_mock)
        self.deezer_service.create_playlist = Mock(return_value = 7636068622)
        self.deezer_service.update_playlist = Mock(return_value = "true")

        res = self.deezer_service.sync_playlist(playlist_mock)
        self.assertEqual(res, "playlist created")

if __name__ == '__main__':
    unittest.main()

