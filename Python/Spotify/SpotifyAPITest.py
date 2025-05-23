#https://spotipy.readthedocs.io/en/2.25.1/
#https://docs.python.org/3/library/asyncio-task.html

import os
import spotifyFunctions as funcs
import spotipy
import asyncio
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

funcs.resetDir()
data = funcs.inWatchedAlbum()