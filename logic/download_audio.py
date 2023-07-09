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
    episode = sp.episode(podcast_id, market="US")
    audio_url = episode["audio_preview_url"]
    response = requests.get(audio_url)
    
    # TODO make is so that the JSON is created already here containing the name
    podcast_name = episode.get("show").get("name")
    filename = podcast_name.lower().replace(" ", "_") + ".mp3"
    filepath = config.MP3_FOLDERPATH / filename

    # Transform to .wav using AudioSegment before saving
    with open(filepath, "wb") as f:
        f.write(response.content)


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

#download_episode("https://open.spotify.com/episode/1Beb93JHF0RtSdTfPwFYVK?si=bbe1aa65d22d4be9")
