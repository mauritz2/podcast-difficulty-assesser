import json
import spacy

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
    total_words = len(transcript_words)
    uncommon_words = 0

    # If does not exist - run "python3 -m spacy download fr_core_news_md"
    nlp = spacy.load("fr_core_news_md")
    
    for word in transcript_words:
        doc = nlp(word)
        lemmatized_word = [token for token in doc][0].lemma_
        if lemmatized_word not in wordlist:
            uncommon_words += 1
    
    pct_uncommon_words = round(uncommon_words / total_words, 3)
    return pct_uncommon_words


def add_uncommon_words_to_jsons():
    wordlist = get_common_wordlist()

    filenames = get_all_transcript_jsons()
    for filename in filenames:
        words = get_transcript_words(filename)
        pct_uncommon = calculate_pct_uncommon_words(words, wordlist)
        with open(config.TRANSCRIPT_FOLDERPATH / filename, "r") as f:
            transcript = json.load(f)
        with open(config.TRANSCRIPT_FOLDERPATH / filename, "w", encoding="utf8") as updated_json:
            transcript["pct_uncommon_words"] = pct_uncommon
            json.dump(transcript, updated_json, ensure_ascii=False)
        print(f"Amount of uncommon words for {filename}: {pct_uncommon}")

def add_words_per_min_to_jsons():
    # TODO - reduce duplication with add_uncommon_words_to_json()
    filenames = get_all_transcript_jsons()
    for filename in filenames:
        with open(config.TRANSCRIPT_FOLDERPATH / filename, "r") as f:
            transcript_json = json.load(f)
        
        audio_length = transcript_json["audio_length"]
        num_words = len(get_transcript_words(filename))
        words_per_min = (num_words / audio_length) * 60
        transcript_json["french_words_per_min"] = words_per_min
        
        with open(config.TRANSCRIPT_FOLDERPATH / filename, "w", encoding="utf8") as updated_json:
            json.dump(transcript_json, updated_json, ensure_ascii=False)
        print(f"Words per minute for {filename}: {words_per_min}")
    
def get_all_transcript_jsons():
    transcripts = get_files_of_type(config.TRANSCRIPT_FOLDERPATH, ".json")
    return transcripts
