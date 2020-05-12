import flask
from flask import Blueprint
import requests
from urllib import parse
import json
from pathlib import Path

deezer_auth = Blueprint('deezer_auth', __name__, template_folder='templates')

# folder = Path("secrets/")
secrets_file = open("secrets/deezer_client_secret.json")
secrets = json.load(secrets_file)

@deezer_auth.route('/authorize')
def authorize():
    app_id = secrets["app_id"]
    redirect_uri = 'http://localhost:8080' + flask.url_for('deezer_auth.oauth2callback')
    URI = 'https://connect.deezer.com/oauth/auth.php?app_id={0}&redirect_uri={1}&perms=manage_library'.format(app_id, redirect_uri)
    print(URI)
    return flask.redirect(URI)


@deezer_auth.route('/oauth2callback')
def oauth2callback():
    app_id = secrets["app_id"]
    app_secret = secrets["app_secret"]
    code = flask.request.args.get('code')
    URI = 'https://connect.deezer.com/oauth/access_token.php?app_id={0}&secret={1}&code={2}'.format(app_id, app_secret, code)
    res = requests.post(URI)
    res_dict = parse.parse_qs(res.text) 
    print(res_dict['access_token'][0])
    flask.session['deezer_credentials'] = res_dict['access_token'][0]
    
    # if 'youtube_credentials' not in flask.session: 
    return flask.redirect(flask.url_for('youtube_auth.authorize'))
    # else:
    #     return 'authenticated'
