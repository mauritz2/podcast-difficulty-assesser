

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

