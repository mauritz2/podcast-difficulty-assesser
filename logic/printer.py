import csv
import json
import config

from .utils import get_files_of_type


def export_podcast_difficulty():
    transcripts = get_files_of_type(config.TRANSCRIPT_FOLDERPATH, ".json")
    for transcript in transcripts:
        with open(config.TRANSCRIPT_FOLDERPATH / transcript, "r", encoding="utf8") as transcript_file:
            transcript_dict = json.load(transcript_file)
            podcast_name = transcript_dict["podcast_name"]
            pct_unknown_words = transcript_dict["pct_unknown_words"]
            french_words_per_minute = transcript_dict["french_words_per_minute"]
            with open(config.OUTPUT / "podcast_difficulty.csv", "a", encoding="utf8") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow([podcast_name, pct_unknown_words, french_words_per_minute])