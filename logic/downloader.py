import spotipy
import requests
import urllib.parse
from spotipy.oauth2 import SpotifyClientCredentials
from pydub import AudioSegment

import config
from .utils import get_files_of_type

def download_episode(podcast_url:str):
    sp = get_authenticated_spotipy()

    parsed_url = urllib.parse.urlparse(podcast_url)
    podcast_id = parsed_url.path.split("/")[-1]    
    # Download the audio preview file
    # TODO - build check if episode already exists - if so skip it
    # create output directories if they don't exist
    #for dir in config.OUTPUT:
    #    if not os.path.exists(dir):
    #        os.makedirs(dir)

    episode = sp.episode(podcast_id, market="US")
    audio_url = episode["audio_preview_url"]
    response = requests.get(audio_url)
    
    # TODO make is so that the JSON is created already here containing the name
    podcast_name = episode.get("show").get("name")
    filename = podcast_name.lower().replace(" ", "_") + ".mp3"
    filepath = config.MP3_FOLDERPATH / filename

    with open(filepath, "wb") as f:
        f.write(response.content)

    print(f"MP3 saved at {filepath}")


def get_authenticated_spotipy():
       sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=config.SPOTIFY_CLIENT_ID,
                client_secret=config.SPOTIFY_CLIENT_SECRET))
       return sp

def convert_mp3s_to_wavs():
    mp3_files = get_files_of_type(config.MP3_FOLDERPATH, "mp3")
    for mp3 in mp3_files:
         new_name = mp3[:-3] + "wav"
         sound = AudioSegment.from_mp3(config.MP3_FOLDERPATH / mp3)
         sound.export(config.WAV_FOLDERPATH / new_name, format="wav")
    print(f"MP3 converted to WAV and saved at {config.WAV_FOLDERPATH / new_name}")
