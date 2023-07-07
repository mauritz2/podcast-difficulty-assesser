import os
from dotenv import load_dotenv

load_dotenv()

# Spotify credentials
SPOTIFY_CLIENT_ID =  os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET =  os.getenv("SPOTIFY_CLIENT_SECRET")
OPENAI_API_KEY =  os.getenv("OPENAI_API_KEY")

# Filenames
OUTPUT = ['downloads']
PODCAST_FILENAME_BASE = "french_podcast"
PODCAST_FILENAME_MP3 = PODCAST_FILENAME_BASE + ".mp3" 
PODCAST_FILENAME_WAV = PODCAST_FILENAME_BASE + ".wav"
PODCAST_FILENAME_TRANSCRIPT = PODCAST_FILENAME_BASE + "_transcript.txt"
COMMON_WORDS_FILE = "assets/top_1000_french_words.csv"
