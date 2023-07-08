import os
from dotenv import load_dotenv
from pathlib import Path 



load_dotenv()

# Spotify credentials
SPOTIFY_CLIENT_ID =  os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET =  os.getenv("SPOTIFY_CLIENT_SECRET")
OPENAI_API_KEY =  os.getenv("OPENAI_API_KEY")

# Filename config
OUTPUT = Path("outputs")


WAV_FOLDERPATH = OUTPUT / "audio_wav_files"


#WAV_FOLDERPATH = OUTPUT + "/" + WAV_FOLDERNAME
PODCAST_FILENAME_BASE = "french_podcast"
PODCAST_FILENAME_MP3 = PODCAST_FILENAME_BASE + ".mp3" 
PODCAST_FILENAME_WAV = PODCAST_FILENAME_BASE + ".wav"
PODCAST_FILENAME_TRANSCRIPT = PODCAST_FILENAME_BASE + "_transcript.txt"
COMMON_WORDS_FILE = "assets/top_1000_french_words.csv"
