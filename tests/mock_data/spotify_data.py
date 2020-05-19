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

track_ids = ["2DLqygtisuvhIUeV3aKJSe"]

tracks_to_add = ["6f88cBp9BBpWGxZGm8iWdm", "2DLqygtisuvhIUeV3aKJSe"]

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

playlists_mock = [Playlist("49W2BLxvDqnN3hsFLAIoqc", "The Sound of Deep Tropical House"), 
          Playlist("6UFxJtxcVnP9tzmt4mnuJS", "Tropical")]

playlists_json_mock = {
  "href": "https://api.spotify.com/v1/users/mces147q3zpo1duzjgo9eh16n/playlists?offset=0&limit=20",
  "items": [
    {
      "collaborative": False,
      "description": "See also <a href=\"spotify:playlist:6N2PLVejJ9XDl34SScxZmC\">Intro</a>, <a href=\"spotify:playlist:0p7c1H2K3rtsiTfJRbcbEd\">Pulse</a>, <a href=\"spotify:playlist:1hjRkG9qsGZK9eNMOx7snc\">Edge</a>, <a href=\"spotify:playlist:4n1kGt7QweqhlkDUBiF2IL\">♀Filter</a> or <a href=\"spotify:playlist:3jsxbQzgNzwXCFZmFarqk4\">2019</a>; or the Sounds of <a href=\"spotify:playlist:5Z4GsFxPRJiN9Qme2P9q6H\">Tropical House</a>, <a href=\"spotify:playlist:5OFsiAHgwlYHB6XLK0kJ4p\">Pop EDM</a>, <a href=\"spotify:playlist:7m1pFx600mZCOuIsOoEIZW\">New French Touch</a>, <a href=\"spotify:playlist:4ZRv1fFjjwpgAcosytT3bd\">Deep House</a>, <a href=\"spotify:playlist:4D7xfG82EyEq3BWglKNS6A\">Swedish Tropical House</a>, <a href=\"spotify:playlist:3pDxuMpz94eDs7WFqudTbZ\">EDM</a>, <a href=\"spotify:playlist:5ouQTmehX3Fu4L3JmMsTo3\">Deep Pop EDM</a>, <a href=\"spotify:playlist:6AzCASXpbvX5o3F8yaj1y0\">House</a>, <a href=\"spotify:playlist:3YjCK5F0D78d0WXHcwQ7tq\">Belgian EDM</a> or <a href=\"spotify:playlist:0IyFLwxEtAB5jszehTpWFJ\">Scandipop</a>; or much more at <a href=\"http://everynoise.com\">everynoise.com</a>.",
      "external_urls": {
        "spotify": "https://open.spotify.com/playlist/49W2BLxvDqnN3hsFLAIoqc"
      },
      "href": "https://api.spotify.com/v1/playlists/49W2BLxvDqnN3hsFLAIoqc",
      "id": "49W2BLxvDqnN3hsFLAIoqc",
      "images": [
        {
          "height": None,
          "url": "https://i.scdn.co/image/ab67706c0000da844d87849ce5863f19e4cdfe4b",
          "width": None
        }
      ],
      "name": "The Sound of Deep Tropical House",
      "owner": {
        "display_name": "The Sounds of Spotify",
        "external_urls": {
          "spotify": "https://open.spotify.com/user/thesoundsofspotify"
        },
        "href": "https://api.spotify.com/v1/users/thesoundsofspotify",
        "id": "thesoundsofspotify",
        "type": "user",
        "uri": "spotify:user:thesoundsofspotify"
      },
      "primary_color": None,
      "public": False,
      "snapshot_id": "NTg3NixhZTNlMGIxMzAyNjA0ZTQ1ZjM4NDM3NjFhM2FkMDZkOTU0YjQwNzFm",
      "tracks": {
        "href": "https://api.spotify.com/v1/playlists/49W2BLxvDqnN3hsFLAIoqc/tracks",
        "total": 460
      },
      "type": "playlist",
      "uri": "spotify:playlist:49W2BLxvDqnN3hsFLAIoqc"
    },
    {
      "collaborative": False,
      "description": "",
      "external_urls": {
        "spotify": "https://open.spotify.com/playlist/6UFxJtxcVnP9tzmt4mnuJS"
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
        "href": "https://api.spotify.com/v1/playlists/6UFxJtxcVnP9tzmt4mnuJS/tracks",
        "total": 3
      },
      "type": "playlist",
      "uri": "spotify:playlist:6UFxJtxcVnP9tzmt4mnuJS"
    }
  ],
  "limit": 20,
  "next": None,
  "offset": 0,
  "previous": None,
  "total": 6
}

track_search_json_mock = {
  "tracks": {
    "href": "https://api.spotify.com/v1/search?query=LVNDSCAPE+Dive+With+Me+%28feat.+Cathrine+Lassen%29&type=track&offset=0&limit=20",
    "items": [
      {
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
        "disc_number": 1,
        "duration_ms": 220432,
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
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:2DLqygtisuvhIUeV3aKJSe"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of"
              },
              "href": "https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of",
              "id": "0LyfQWJT6nXafLPZqxe9Of",
              "name": "Various Artists",
              "type": "artist",
              "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1BgwXTWWQOpXz0GyxFe7Y4"
          },
          "href": "https://api.spotify.com/v1/albums/1BgwXTWWQOpXz0GyxFe7Y4",
          "id": "1BgwXTWWQOpXz0GyxFe7Y4",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b27354800fb9bde4b18fc0a3a7ff",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/ab67616d00001e0254800fb9bde4b18fc0a3a7ff",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/ab67616d0000485154800fb9bde4b18fc0a3a7ff",
              "width": 64
            }
          ],
          "name": "Study Music, Vol. 1: Deep House (Presented by Spinnin' Records)",
          "release_date": "2020-02-12",
          "release_date_precision": "day",
          "total_tracks": 40,
          "type": "album",
          "uri": "spotify:album:1BgwXTWWQOpXz0GyxFe7Y4"
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
        "disc_number": 1,
        "duration_ms": 220432,
        "explicit": False,
        "external_ids": {
          "isrc": "NLZ541701341"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4Ba6s6Lr21pRcgwSavnefX"
        },
        "href": "https://api.spotify.com/v1/tracks/4Ba6s6Lr21pRcgwSavnefX",
        "id": "4Ba6s6Lr21pRcgwSavnefX",
        "is_local": False,
        "name": "Dive With Me (feat. Cathrine Lassen)",
        "popularity": 11,
        "preview_url": "https://p.scdn.co/mp3-preview/440d46fb735de4e4640a7d9b25ce544efecc1d55?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:4Ba6s6Lr21pRcgwSavnefX"
      }
    ],
    "limit": 20,
    "next": None,
    "offset": 0,
    "previous": None,
    "total": 3
  }
}

no_results_mock = {
  "tracks": {
    "href": "https://api.spotify.com/v1/search?query=LVNDSCA+gfds4%28feat.+Cathrine+Lassen%29&type=track&offset=0&limit=20",
    "items": [],
    "limit": 20,
    "next": None,
    "offset": 0,
    "previous": None,
    "total": 0
  }
}

successful_update_mock = {
  "snapshot_id": "NDQsZDQ5MzhiZTMwMWJmNWFhNzg0Njg5ZjRlYzIzNmYwZTYwOTg1NzcxYg=="
}

user_json_mock = {
  "country": "CA",
  "display_name": "MrMoss",
  "email": "imlukemedeiros@gmail.com",
  "explicit_content": {
    "filter_enabled": False,
    "filter_locked": False
  },
  "external_urls": {
    "spotify": "https://open.spotify.com/user/mces147q3zpo1duzjgo9eh16n"
  },
  "followers": {
    "href": None,
    "total": 0
  },
  "href": "https://api.spotify.com/v1/users/mces147q3zpo1duzjgo9eh16n",
  "id": "mces147q3zpo1duzjgo9eh16n",
  "images": [],
  "product": "open",
  "type": "user",
  "uri": "spotify:user:mces147q3zpo1duzjgo9eh16n"
}

playlist_creation_mock = {
  "collaborative": False,
  "description": "New playlist description",
  "external_urls": {
    "spotify": "https://open.spotify.com/playlist/5WbpjFKUylN0Q80q7eKaen"
  },
  "followers": {
    "href": None,
    "total": 0
  },
  "href": "https://api.spotify.com/v1/playlists/5WbpjFKUylN0Q80q7eKaen",
  "id": "5WbpjFKUylN0Q80q7eKaen",
  "images": [],
  "name": "New Playlist",
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
  "public": False,
  "snapshot_id": "MSwzYjE3OGQ3ZGUyMjFmMTg3NDVlNGYzOTI0YjgyNzJiODJkY2U4OGFj",
  "tracks": {
    "href": "https://api.spotify.com/v1/playlists/5WbpjFKUylN0Q80q7eKaen/tracks",
    "items": [],
    "limit": 100,
    "next": None,
    "offset": 0,
    "previous": None,
    "total": 0
  },
  "type": "playlist",
  "uri": "spotify:playlist:5WbpjFKUylN0Q80q7eKaen"
}