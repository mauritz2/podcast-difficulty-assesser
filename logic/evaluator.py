import json

import config
from .utils import get_files_of_type

def get_transcript_words(filename:str):
    filepath = config.TRANSCRIPT_FOLDERPATH / filename
    with open(filepath, "r") as f:
        data = json.load(f)
        transcript = data["transcript"]
    words = transcript.split(" ")
    return words


def get_common_wordlist():
    with open(config.COMMON_WORDS_FILE, "r") as f:
        wordlist_raw = f.readlines()
        wordlist = list(map(lambda x: x.strip(), wordlist_raw))
    return wordlist


def calculate_pct_uncommon_words(transcript_words:list[str], wordlist:list[str]):
    # TODO - should ideally be able to account for plurals, feminine forms, verb conjugations
    #wordlist = get_common_wordlist()
    
    total_words = len(transcript_words)
    uncommon_words = 0

    for word in transcript_words:
        if word not in wordlist:
            uncommon_words += 1
    
    pct_uncommon_words = uncommon_words / total_words
    return pct_uncommon_words


def add_uncommon_words_to_jsons():
    wordlist = get_common_wordlist()

    filenames = get_all_transcript_jsons()
    for filename in filenames:
        words = get_transcript_words(filename)
        pct_uncommon = calculate_pct_uncommon_words(words, wordlist)
        # TODO - continue here by writing result to JSON


def get_all_transcript_jsons():
    transcripts = get_files_of_type(config.TRANSCRIPT_FOLDERPATH, ".json")
    return transcripts
