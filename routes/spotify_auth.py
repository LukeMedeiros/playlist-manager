import json
from flask import Flask, request, redirect, g, render_template, Blueprint, session
import requests
from urllib.parse import quote
import sys

spotify_auth = Blueprint('spotify_auth', __name__, template_folder='templates')

secrets_file = open("secrets/spotify_client_secret.json")
secrets = json.load(secrets_file)

#  Client Keys
CLIENT_ID = secrets["client_id"]
CLIENT_SECRET = secrets["client_secret"]
# Spotify URLS
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# Server-side Parameters
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8080
REDIRECT_URI = "{}:{}/callback".format(CLIENT_SIDE_URL, PORT)
SCOPE = "playlist-modify-public playlist-modify-private ugc-image-upload user-read-playback-state streaming user-read-email playlist-read-collaborative user-modify-playback-state user-read-private user-library-modify user-top-read user-read-currently-playing app-remote-control user-read-recently-played user-library-read"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    # "state": STATE,
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": CLIENT_ID
}


@auth.route("/authorize")
def index():
    # Authorization
    url_args = "&".join(["{}={}".format(key, quote(val)) for key, val in auth_query_parameters.items()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)


@auth.route("/oauth2callback")
def oauth2callback():
    # Requests refresh and access tokens
    auth_token = request.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload)

    # Tokens are Returned to Application
    response_data = json.loads(post_request.text)
    session["spotify_credentials"] = response_data["access_token"]

    return "authenticated"
