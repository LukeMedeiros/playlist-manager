# playlist-manager

Orignally planned on creating a simple script for managing playlists between streaming services (ie YouTube, Deezer, Spotify, etc). 
However, a server is needed in order receive auth tokens from the respective streaming service. 

## Setup 

### Youtube OAuth
1. Create a new google project at [google dev console](https://console.developers.google.com/ )
2. Configure a consent screen with the following settings  
  * User type: External 
  * Application name: any
3. Create Credentials
  * Select OAuth client ID
  * Application type: web app
4. Download the client and add it to the project under the directory secrets named youtube_client_secret.json
 
### Deezer OAuth
1. Create a new deezer app at [deezer dev console](https://developers.deezer.com/myapps/create)
2. when finished add a file to the secrets directory named deezer_client_secret.json of the format 
{
  "app_id": "your_id", 
  "add_secret": "your_secret"
}

## End Points 

### authentication
http://localhost:8080/youtube/authorize 

http://localhost:8080/deezer/authorize 

### sync deezer playlists with youtube 
http://localhost:8080/sync/deezer?id=your_playlist_id

### sync youtube playlists with deezer 
http://localhost:8080/sync/youtube?id=your_playlist_id

### sync playlists across streaming services with common name 
http://localhost:8080/sync?title=playlist_name
