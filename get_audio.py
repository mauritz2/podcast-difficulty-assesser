import os
import config
from spotifypodcast import SpotifyPodcast

# create output directories if they don't exist
for dir in config.OUTPUT:
    if not os.path.exists(dir):
        os.makedirs(dir)

def get_audio(podcast_url):
    podcast = SpotifyPodcast(config.SPOTIFY_CLIENT_ID, config.SPOTIFY_CLIENT_SECRET)
    audio_path = podcast.download_episode_and_get_link(podcast_url=podcast_url, filename=config.PODCAST_FILENAME_MP3)    
    print(f"Download complete at {audio_path}")
    
#summarize("https://open.spotify.com/episode/0YqflJb8Wco8IDdGHPNTu8")
#summarize("https://open.spotify.com/episode/46deyZlBRfOvcSzT9NO10r?si=9cb4bc644b024e3b")
get_audio("https://open.spotify.com/episode/1Beb93JHF0RtSdTfPwFYVK?si=bbe1aa65d22d4be9")