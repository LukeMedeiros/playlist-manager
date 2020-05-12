import os
import flask
import requests
from routes.youtube_auth import youtube_auth
from routes.deezer_auth import deezer_auth
from routes.sync import  sync

app = flask.Flask(__name__)
# Note: A secret key is included in the sample so that it works.
# If you use this code in your application, replace this with a truly secret
# key. See https://flask.palletsprojects.com/quickstart/#sessions.
app.secret_key = 'REPLACE ME - this value is here as a placeholder.'

app.register_blueprint(youtube_auth, url_prefix='/youtube')
app.register_blueprint(deezer_auth, url_prefix='/deezer')
app.register_blueprint(sync, url_prefix='/sync')

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification.
  # ACTION ITEM for developers:
  #     When running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

  # Specify a hostname and port that are set as a valid redirect URI
  # for your API project in the Google API Console.
  app.run('localhost', 8080, debug=True)