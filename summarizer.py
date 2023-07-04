import os
from dotenv import load_dotenv
from spotifypodcast import SpotifyPodcast
#from youtubedownloader import YouTubeDownloader
#from whipertranscriber import WhisperTranscriber
#from gpt3summarizer import GPT3Summarizer

# Load API credentials from .env file
load_dotenv()

SPOTIFY_CLIENT_ID =  os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET =  os.getenv("SPOTIFY_CLIENT_SECRET")
OPENAI_API_KEY =  os.getenv("OPENAI_API_KEY")

OUTPUT = ['downloads/youtube', 'downloads/spotify', 'downloads/whisper',  'downloads/gpt3']
# create output directories if they don't exist
for dir in OUTPUT:
    if not os.path.exists(dir):
        os.makedirs(dir)

def summarize(podcast_url):
    
    print('Initializing podcast download...')
    print(f'podcast_url: {podcast_url}')
    
    file_id = None
    
    podcast = SpotifyPodcast(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    #file_id = podcast.get_episode_id(podcast_url)
    audio_path = podcast.download_episode(podcast_url)
    
    print(f"COMPLETE - Audio path: {audio_path}")

    #transcriber = WhisperTranscriber(OPENAI_API_KEY)
    #transcript = transcriber.transcribe(audio_path)    
    print(f'Completed summarization for ({podcast_url})')
    
#summarize("https://open.spotify.com/episode/0YqflJb8Wco8IDdGHPNTu8")
summarize("https://open.spotify.com/episode/46deyZlBRfOvcSzT9NO10r?si=9cb4bc644b024e3b")