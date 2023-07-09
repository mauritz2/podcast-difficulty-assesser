import spotipy
import requests
import urllib.parse
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyPodcast:
    def __init__(self, client_id, client_secret):        
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))
        

    def download_episode_and_get_link(self, podcast_url:str, filename:str):
        parsed_url = urllib.parse.urlparse(podcast_url)
        podcast_id = parsed_url.path.split("/")[-1]
        
        # Get the first episode of the podcast
        # episode = self.sp.episode(podcast["episodes"]["items"][0]["id"])
        episode = self.sp.episode(podcast_id, market="US")
        # Download the audio preview file
        audio_url = episode["audio_preview_url"]
        response = requests.get(audio_url)
        # Fix weird signs in JSON
        with open(filename, "wb") as f:
            f.write(response.content)

        return filename
