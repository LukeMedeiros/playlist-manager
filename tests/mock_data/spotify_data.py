from objects.track import Track, SpotifyTrack
from objects.playlist import Playlist

playlist_json_mock = {
  "collaborative": False,
  "description": "",
  "external_urls": {
    "spotify": "https://open.spotify.com/playlist/6UFxJtxcVnP9tzmt4mnuJS"
  },
  "followers": {
    "href": None,
    "total": 0
  },
  "href": "https://api.spotify.com/v1/playlists/6UFxJtxcVnP9tzmt4mnuJS",
  "id": "6UFxJtxcVnP9tzmt4mnuJS",
  "images": [
    {
      "height": 640,
      "url": "https://i.scdn.co/image/ab67616d0000b2736571aca637ba942edba50344",
      "width": 640
    }
  ],
  "name": "Tropical",
  "owner": {
    "display_name": "MrMoss",
    "external_urls": {
      "spotify": "https://open.spotify.com/user/mces147q3zpo1duzjgo9eh16n"
    },
    "href": "https://api.spotify.com/v1/users/mces147q3zpo1duzjgo9eh16n",
    "id": "mces147q3zpo1duzjgo9eh16n",
    "type": "user",
    "uri": "spotify:user:mces147q3zpo1duzjgo9eh16n"
  },
  "primary_color": None,
  "public": True,
  "snapshot_id": "NCw4ZGY3Yjk4MGFmYjZhYzY1NzEzYTMxOTRmYjJlYjFiZWRmNjJkN2Zh",
  "tracks": {
    "href": "https://api.spotify.com/v1/playlists/6UFxJtxcVnP9tzmt4mnuJS/tracks?offset=0&limit=100",
    "items": [
      {
        "added_at": "2020-03-18T23:57:57Z",
        "added_by": {
          "external_urls": {
            "spotify": "https://open.spotify.com/user/mces147q3zpo1duzjgo9eh16n"
          },
          "href": "https://api.spotify.com/v1/users/mces147q3zpo1duzjgo9eh16n",
          "id": "mces147q3zpo1duzjgo9eh16n",
          "type": "user",
          "uri": "spotify:user:mces147q3zpo1duzjgo9eh16n"
        },
        "is_local": False,
        "primary_color": None,
        "track": {
          "album": {
            "album_type": "single",
            "artists": [
              {
                "external_urls": {
                  "spotify": "https://open.spotify.com/artist/2QlwnS23KrBeshXFyK5U6M"
                },
                "href": "https://api.spotify.com/v1/artists/2QlwnS23KrBeshXFyK5U6M",
                "id": "2QlwnS23KrBeshXFyK5U6M",
                "name": "LVNDSCAPE",
                "type": "artist",
                "uri": "spotify:artist:2QlwnS23KrBeshXFyK5U6M"
              }
            ],
            "available_markets": [
              "AD",
              "AE",
              "AR",
              "AT",
              "AU",
              "BE",
              "BG",
              "BH",
              "BO",
              "BR",
              "CA",
              "CH",
              "CL",
              "CO",
              "CR",
              "CY",
              "CZ",
              "DE",
              "DK",
              "DO",
              "DZ",
              "EC",
              "EE",
              "EG",
              "ES",
              "FI",
              "FR",
              "GB",
              "GR",
              "GT",
              "HK",
              "HN",
              "HU",
              "ID",
              "IE",
              "IL",
              "IN",
              "IS",
              "IT",
              "JO",
              "JP",
              "KW",
              "LB",
              "LI",
              "LT",
              "LU",
              "LV",
              "MA",
              "MC",
              "MT",
              "MX",
              "MY",
              "NI",
              "NL",
              "NZ",
              "OM",
              "PA",
              "PE",
              "PH",
              "PL",
              "PS",
              "PT",
              "PY",
              "QA",
              "RO",
              "SA",
              "SE",
              "SG",
              "SK",
              "SV",
              "TH",
              "TN",
              "TR",
              "TW",
              "US",
              "UY",
              "VN",
              "ZA"
            ],
            "external_urls": {
              "spotify": "https://open.spotify.com/album/0z7F1uxjghiQIGFc79XSXN"
            },
            "href": "https://api.spotify.com/v1/albums/0z7F1uxjghiQIGFc79XSXN",
            "id": "0z7F1uxjghiQIGFc79XSXN",
            "images": [
              {
                "height": 640,
                "url": "https://i.scdn.co/image/ab67616d0000b2736571aca637ba942edba50344",
                "width": 640
              },
              {
                "height": 300,
                "url": "https://i.scdn.co/image/ab67616d00001e026571aca637ba942edba50344",
                "width": 300
              },
              {
                "height": 64,
                "url": "https://i.scdn.co/image/ab67616d000048516571aca637ba942edba50344",
                "width": 64
              }
            ],
            "name": "Dive With Me",
            "release_date": "2017-11-03",
            "release_date_precision": "day",
            "total_tracks": 2,
            "type": "album",
            "uri": "spotify:album:0z7F1uxjghiQIGFc79XSXN"
          },
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/2QlwnS23KrBeshXFyK5U6M"
              },
              "href": "https://api.spotify.com/v1/artists/2QlwnS23KrBeshXFyK5U6M",
              "id": "2QlwnS23KrBeshXFyK5U6M",
              "name": "LVNDSCAPE",
              "type": "artist",
              "uri": "spotify:artist:2QlwnS23KrBeshXFyK5U6M"
            },
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/5i09Vd9N18qRJl2RcXODOp"
              },
              "href": "https://api.spotify.com/v1/artists/5i09Vd9N18qRJl2RcXODOp",
              "id": "5i09Vd9N18qRJl2RcXODOp",
              "name": "Cathrine Lassen",
              "type": "artist",
              "uri": "spotify:artist:5i09Vd9N18qRJl2RcXODOp"
            }
          ],
          "available_markets": [
            "AD",
            "AE",
            "AR",
            "AT",
            "AU",
            "BE",
            "BG",
            "BH",
            "BO",
            "BR",
            "CA",
            "CH",
            "CL",
            "CO",
            "CR",
            "CY",
            "CZ",
            "DE",
            "DK",
            "DO",
            "DZ",
            "EC",
            "EE",
            "EG",
            "ES",
            "FI",
            "FR",
            "GB",
            "GR",
            "GT",
            "HK",
            "HN",
            "HU",
            "ID",
            "IE",
            "IL",
            "IN",
            "IS",
            "IT",
            "JO",
            "JP",
            "KW",
            "LB",
            "LI",
            "LT",
            "LU",
            "LV",
            "MA",
            "MC",
            "MT",
            "MX",
            "MY",
            "NI",
            "NL",
            "NZ",
            "OM",
            "PA",
            "PE",
            "PH",
            "PL",
            "PS",
            "PT",
            "PY",
            "QA",
            "RO",
            "SA",
            "SE",
            "SG",
            "SK",
            "SV",
            "TH",
            "TN",
            "TR",
            "TW",
            "US",
            "UY",
            "VN",
            "ZA"
          ],
          "disc_number": 1,
          "duration_ms": 220432,
          "episode": False,
          "explicit": False,
          "external_ids": {
            "isrc": "NLZ541701341"
          },
          "external_urls": {
            "spotify": "https://open.spotify.com/track/2DLqygtisuvhIUeV3aKJSe"
          },
          "href": "https://api.spotify.com/v1/tracks/2DLqygtisuvhIUeV3aKJSe",
          "id": "2DLqygtisuvhIUeV3aKJSe",
          "is_local": False,
          "name": "Dive With Me (feat. Cathrine Lassen)",
          "popularity": 57,
          "preview_url": "https://p.scdn.co/mp3-preview/440d46fb735de4e4640a7d9b25ce544efecc1d55?cid=774b29d4f13844c495f206cafdad9c86",
          "track": True,
          "track_number": 1,
          "type": "track",
          "uri": "spotify:track:2DLqygtisuvhIUeV3aKJSe"
        },
        "video_thumbnail": {
          "url": None
        }
      }
    ],
    "limit": 100,
    "next": None,
    "offset": 0,
    "previous": None,
    "total": 3
  },
  "type": "playlist",
  "uri": "spotify:playlist:6UFxJtxcVnP9tzmt4mnuJS"
}

tracks = [SpotifyTrack("2DLqygtisuvhIUeV3aKJSe","Dive With Me (feat. Cathrine Lassen)", "LVNDSCAPE", "Dive With Me", "NLZ541701341")]

playlist_mock = Playlist("6UFxJtxcVnP9tzmt4mnuJS", "Tropical", tracks)

invalid_id_mock = {
  "error": {
    "status": 404,
    "message": "Invalid playlist Id"
  }
}

invalid_token_mock = {
  "error": {
    "status": 401,
    "message": "Invalid access token"
  }
}

