import unittest
from controllers.deezer_playlist_service import DeezerPlaylistService

class SyntTest(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()