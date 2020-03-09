import sys, os
from settings import *
from functions import *

client_id = '96032b93d38a45cc8a89124d99138c90'
client_secret = '5df846d674fc4e2ea7ac34bfbb8f5122'
os.system(f"export SPOTIPY_CLIENT_ID={client_id}")
os.system(f"export SPOTIPY_CLIENT_SECRET={client_secret}")

service = SERVICE
link = LINK

if service == 'playlist':
    getPlaylist(link)

elif service == 'albun':
    pass

elif service == 'music':
    searchMiusic()
