import json
import spotipy
import requests
import urllib.parse
from spotipy.oauth2 import SpotifyClientCredentials
from pydub import AudioSegment

import config
from .utils import get_files_of_type, add_value_to_json, get_value_from_json


def download_episode(podcast_url:str):
    # TODO - break out into smaller functions

    if has_podcast_been_downloaded(podcast_url):
        print(f"Podcast {podcast_url} has already been downloaded")
        return 
    
    # TODO - redundant to make this call every download episode call
    sp = get_authenticated_spotipy()

    parsed_url = urllib.parse.urlparse(podcast_url)
    podcast_id = parsed_url.path.split("/")[-1]    

    episode = sp.episode(podcast_id, market="US")
    audio_url = episode["audio_preview_url"]
    response = requests.get(audio_url)
    
    podcast_name = episode.get("show").get("name")    
    filename = podcast_name.lower().replace(":", "_").replace(" ", "_")
    mp3_filename = filename + ".mp3"
    mp3_filepath = config.MP3_FOLDERPATH / mp3_filename

    with open(mp3_filepath, "wb") as f:
        f.write(response.content)
    print(f"MP3 saved at {mp3_filepath}")

    json_filepath = config.TRANSCRIPT_FOLDERPATH / (filename + "_transcript.json")

    json_dict = {"podcast_name": podcast_name,
                 "podcast_url": podcast_url,
                 "mp3_filename":mp3_filename,
                 "podcast_url": podcast_url}
    with open(json_filepath, 'w', encoding="utf8") as output_file:
        json.dump(json_dict, output_file, ensure_ascii=False)
    print(f"Transcript saved at {json_filepath}")


def has_podcast_been_downloaded(podcast_url:str):
        jsons = get_files_of_type(config.TRANSCRIPT_FOLDERPATH, ".json")
        for json in jsons:
                downloaded_url = get_value_from_json(config.TRANSCRIPT_FOLDERPATH / json, "podcast_url")
                if podcast_url == downloaded_url:
                        return True
        else:
                return False

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
         add_value_to_json(config.TRANSCRIPT_FOLDERPATH / (new_name[:-4] + "_transcript.json"), "wav_filename", new_name)
    
    print(f"MP3 converted to WAV and saved at {config.WAV_FOLDERPATH / new_name}")