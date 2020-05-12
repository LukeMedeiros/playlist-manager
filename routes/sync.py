from flask import Flask, Blueprint, request, session, redirect
from controllers.youtube_playlist_service import YoutubePlaylistService
from controllers.deezer_playlist_service import DeezerPlaylistService
from controllers.sync_playlist import SyncPlaylist
from interfaces.playlist_service import PlaylistService
from typing import List
import json 

sync = Blueprint('sync', __name__, template_folder='templates')

@sync.route("/youtube")
def sync_youtube_playlist():
    # if 'credentials' not in session:
    #     return redirect('youtube_auth.authorize')
    playlist_id = request.args.get('id')
    youtube_service = YoutubePlaylistService()
    sync_playlist(youtube_service, playlist_id, ["deezer"])
    return "synced youtube playlist with deezer successfully"

@sync.route("/deezer")
def sync_deezer_playlist():
    # before anything it should validate the token
    playlist_id = request.args.get('id')
    deezer_service = DeezerPlaylistService()
    sync_playlist(deezer_service, playlist_id, ["youtube"])
    return "synced deezer playlist with youtube successfully"

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
    playlist_to_sync = playlist_service.get_playlist(playlist_id)
    # id passed could not exist 
    sync_service = SyncPlaylist()
    sync_service.sync_playlist(playlist_to_sync, sync_with)