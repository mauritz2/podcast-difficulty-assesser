

# For each list in list of French podcast URLs
# Download the audio to the download folder - if the name doesn't already exist

# Transcriber
    # init(folder)
    # Instantiate with a folder with .WAV
    # Loop through WAVs and load .wav from disk
    # Save transcription as JSON
    # Name, length, URL, 
    
# DifficultyAssesser
    # Take folder name of JSONs as input
    # Load transcrtip JSON from folder
    # Assess difficulty metrics
    # Add difficulty metrics to the JSON

# SpotifyDownloader
    # Download episode from Spotify
    # Save audio files (turn to WAV before saving)
    # Error handling for downloadings
    # Get the podcast name and use that as file name

# create output directories if they don't exist
#for dir in config.OUTPUT:
#    if not os.path.exists(dir):
#        os.makedirs(dir)


#download_episode("https://open.spotify.com/episode/1Beb93JHF0RtSdTfPwFYVK?si=bbe1aa65d22d4be9")
#summarize("https://open.spotify.com/episode/0YqflJb8Wco8IDdGHPNTu8")
#summarize("https://open.spotify.com/episode/46deyZlBRfOvcSzT9NO10r?si=9cb4bc644b024e3b")
