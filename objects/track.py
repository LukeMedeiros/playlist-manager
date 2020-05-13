from typing import List

class Track: 
    def __init__(self, id, name, artist, album=""):
        self.id = id
        self.name = name
        self.artist = artist 
        self.album = album

class DeezerTrack(Track):
    def __init__(self, id, name, artist, album, isrc=""):
        Track.__init__(self, id, name, artist, album) 
        self.isrc = isrc

    def set_isrc(self, isrc):
        self.isrc = isrc

class SpotifyTrack(Track):
    def __init__(self, id, name, artist, album, artists: List[str], isrc=""):
        Track.__init__(self, id, name, artist, album) 
        self.isrc = isrc
        self.artists = artists

    def set_isrc(self, isrc):
        self.isrc = isrc
