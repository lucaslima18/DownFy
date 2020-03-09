from __future__ import unicode_literals
import spotipy, youtube_dl, json
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def searchMiusic():
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'playlistend': 1,
        'writethumbnail': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        nome = input('Give your music name:')
        try:
            ydl.download([f'https://www.youtube.com/results?search_query={nome}'])
        
        except:
            print("One problem happen! sorry...")

def catchPlaylistMiusic():
    for line in f:
        print(line)

def getAlbum(link):
    urn = 'spotify:album:6GzqMW6Tq0drVxlBUvivzd'

    album = sp.album_tracks(urn)
    print(album)

def getPlaylist(link):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'playlistend': 1,
        'writethumbnail': True,
    }
    music_count = 0
    playlist = sp.playlist(link, None, None)
    total = playlist['tracks']['total']
    print(f"Start Download the playlist: {playlist['name']} de {playlist['owner']['display_name']}...\n")
    for item in playlist['tracks']['items']:
        music_count = music_count + 1
        artists = item['track']['album']['artists'][0]['name']
        item = item['track']['name']
        music = f'{item}, {artists}'

        print(f"Downloading({music_count}/{total}): {item}, {artists}...")
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([f'https://www.youtube.com/results?search_query={music}'])
            except:
                print("One problem happen! sorry...")
        print("\n")