# Podcast Oral Comprehension Difficulty Assesser

**Purpose**

This script downloads a podcast audio sample from Spotify, converts the speech to text, and then estimates the difficulty metrics based on the transcripts. The purpose is to make it easier to find podcasts at the right difficulty level to improve oral comprehension.

**Prerequisites**
1. Install packages in requirements.txt
2. Create the folders defined in config.py

**Run for a new podcast**
1. Add a link to an episode of the podcast in "french_podcasts.csv" for any new podcasts to assess
2. "python main.py"
3. Check outputs in output folder, one JSON per podcast is generated 

**Run for other languages**
1. Update evaluator.py to use a different spacy language
2. Change the config "PODCAST_LANGUAGE"

