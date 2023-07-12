import os
from dotenv import load_dotenv
from pathlib import Path 

load_dotenv()

# Spotify credentials
SPOTIFY_CLIENT_ID =  os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET =  os.getenv("SPOTIFY_CLIENT_SECRET")
OPENAI_API_KEY =  os.getenv("OPENAI_API_KEY")

# Transcription config
PODCAST_LANGUAGE = "fr-FR"

# Output file paths
OUTPUT = Path("outputs")
WAV_FOLDERPATH = OUTPUT / "wav_files"
MP3_FOLDERPATH = OUTPUT / "mp3_files"
TRANSCRIPT_FOLDERPATH = OUTPUT / "transcripts"

# Asset file paths
COMMON_WORDS_FILE = "assets/top_1000_french_words_lem.csv"
FRENCH_PODCAST_FILE = "assets/french_podcasts.csv"