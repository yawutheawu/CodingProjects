import os
import spotipy
import asyncio
import constants
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

#https://developer.spotify.com/documentation/web-api/concepts/scopes

def resetDir():
    """ Sets current working directory to the folder containing the script
        (For Relative Pathing)
    """
    fileName = __file__
    if type(fileName.split("\\")) == list and len(fileName.split("\\"))>1:
        fileName = fileName.split("\\")[-1]
        filePath = __file__.replace(fileName,"")
    else:
        fileName = fileName.split("/")[-1]
        filePath = __file__.replace(fileName,"")
    os.chdir(filePath)
    return os.path.abspath(filePath)

def retSpotifyCreds() -> list:
    """ Loads credentials from spotifyCreds.env file (SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI) and
        returns the ID, SECRET and REDIRECTURI
    """
    resetDir()
    load_dotenv("spotifyCreds.env")

    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    client_redirectURI = os.getenv("SPOTIPY_REDIRECT_URI")

    return client_id,client_secret,client_redirectURI


client_id, client_secret, client_red_URI = retSpotifyCreds()
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=client_red_URI,
                                               scope=constants.scope))

def get_top_tracks(numTracks:int = 20) -> list:
    """
    Gets User's top tracks as defined by numTracks, otherwise defaults to 20
    """
    results = sp.current_user_saved_tracks(limit=numTracks)
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx + 1, track['artists'][0]['name'], " – ", track['name'])

def getCurrentlyPlaying():
    return sp.current_playback()

def get_album_tracks(album_id):
    return sp.album_tracks(album_id)

def generateAlbumURIs(albumID):
    data = get_album_tracks(albumID)
    uriList = []
    for i in data["items"]:
        uriList.append(i["uri"])
    return uriList

def queueAlbum(albumID):
    for i in generateAlbumURIs(albumID):
        sp.add_to_queue(i)

def isWatchedAlbumNext():
    #sp.queue()["queue"][0]["uri"]
    if sp.queue()["queue"][0]["album"]["id"] in constants.checkAlbumIds:
        queueAlbum(sp.queue()["queue"][0]["album"]["id"])

def inWatchedAlbum():
    if getCurrentlyPlaying()["item"]["album"]["id"] in constants.flowAlbums:
        data = get_album_tracks(getCurrentlyPlaying()["item"]["album"]["id"])
        flag = False
        for i in data["items"]:
            if not flag:
                if i["uri"] == getCurrentlyPlaying()["item"]["uri"]:
                    flag = True
                else:
                    pass
            else:
                sp.add_to_queue(i["uri"])


#https://stackoverflow.com/questions/59520761/how-to-await-a-coroutine-until-a-condition-is-met