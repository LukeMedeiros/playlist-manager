from flask import Flask, Blueprint, request, session, redirect
from controllers.youtube_playlist_service import YoutubePlaylistService
from controllers.deezer_playlist_service import DeezerPlaylistService
from controllers.spotify_playlist_service import SpotifyPlaylistService
from controllers.sync_playlist import SyncPlaylist
from interfaces.playlist_service import PlaylistService
from objects.playlist import Playlist
from typing import List
import constants
import json 

sync = Blueprint('sync', __name__, template_folder='templates')

@sync.route("/youtube")
def sync_youtube_playlist():
    # if 'credentials' not in session:
    #     return redirect('youtube_auth.authorize')
    playlist_id = request.args.get('id')
    streaming_services = request.args.get("streaming_services")
    youtube_service = YoutubePlaylistService()
    sync_playlist(youtube_service, playlist_id, streaming_services)
    return "synced youtube playlist with deezer successfully"

@sync.route("/deezer")
def sync_deezer_playlist():
    # before anything it should validate the token

    playlist_id = request.args.get('id')
    streaming_services = request.args.get("streaming_services")
    result = validate_params(playlist_id, streaming_services, "deezer") 
    if result != "valid":
        return result 

    deezer_service = DeezerPlaylistService()
    result = sync_playlist(deezer_service, playlist_id, streaming_services.split(","))
    # temporary patch 
    if result == "invalid id": 
        return result 
    return "synced deezer playlist with : " + streaming_services

@sync.route("/spotify")
def sync_spotify_playlist():
    # before anything it should validate the token
    playlist_id = request.args.get('id')
    streaming_services = request.args.get("streaming_services")
    spotify_service = SpotifyPlaylistService()
    sync_playlist(spotify_service, playlist_id, streaming_services)
    # need to create a better return message
    return "synced spotify playlist with: " + streaming_services

# TODO need to add spotify support
@sync.route('')
def sync_across_streaming_services():
    playlist_title = request.args.get('title')

    deezer_service = DeezerPlaylistService()
    deezer_playlist_id = get_playlist_by_title(deezer_service, playlist_title)
    if deezer_playlist_id == None: 
        return "No deezer playlist found with title: " + playlist_title
    
    youtube_service = YoutubePlaylistService()
    youtube_playlist_id = get_playlist_by_title(youtube_service, playlist_title)
    if youtube_playlist_id == None: 
        return "No youtube playlist found with title: " + playlist_title
    
    sync_playlist(deezer_service, deezer_playlist_id, ["youtube"])
    sync_playlist(youtube_service, youtube_playlist_id, ["deezer"])

    return "synced playlist named: " + playlist_title + " successfully accross youtube and deezer"

def get_playlist_by_title(playlist_service: PlaylistService, playlist_title):
    playlists = playlist_service.get_my_playlists()
    playlist_id = None
    for playlist in playlists: 
        if playlist.title == playlist_title:
            playlist_id = playlist.id
            break
    return playlist_id

def sync_playlist(playlist_service: PlaylistService, playlist_id: str, sync_with: List[str]):
    # id passed could not exist 
    playlist_to_sync = playlist_service.get_playlist(playlist_id)
    if type(playlist_to_sync) != Playlist: 
        return "invalid id"
    sync_service = SyncPlaylist()
    sync_service.sync_playlist(playlist_to_sync, sync_with)
    # on successful sync I should return a list of the songs which were successfully synced
    # or something along these lines 

def validate_params(id: str, streaming_services: str, root_service: str) -> str: 
    if type(id) != str or id == "": 
        return "invalid id" 
    streaming_services = streaming_services.split(",")
    for streaming_service in streaming_services: 
        if streaming_service not in constants.VALID_SERVICES:
            return "invalid streaming service: " + streaming_service
        if streaming_service == root_service: 
            return "root service cannot be synced" 
    return "valid"
