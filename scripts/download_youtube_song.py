import sys
import youtube_dl
import os
import googleapiclient.discovery
import json

def download_song(videoId):

    ydl_opts = {
        'outtmpl': 'songset/%(title)s-%(id)s.%(ext)s', 
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    # downloading a specific youtube video
    youtube_dl.YoutubeDL(ydl_opts).download(['https://www.youtube.com/watch?v='+videoId])