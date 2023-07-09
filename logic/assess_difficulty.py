
import config

def get_words_in_transcript():
    # Temporary test func
    with open("french_podcast_transcript.txt", "r") as f:
        data = f.read()
        print(data)
    words = data.split(" ")
    return words


def get_common_wordlist():
    # TODO - should ideally be able to account for plurals, feminine forms, verb conjugations
    with open(config.COMMON_WORDS_FILE, "r") as f:
        wordlist_raw = f.readlines()
        wordlist = list(map(lambda x: x.strip(), wordlist_raw))
    return wordlist


def assess_degree_of_uncommon_words(transcript_words:str, wordlist:list[str]):
    wordlist = get_common_wordlist()
    
    total_words = len(transcript_words)
    uncommon_words = 0

    for word in transcript_words:
        if word not in wordlist:
            uncommon_words += 1
    
    pct_uncommon_words = uncommon_words / total_words
    return pct_uncommon_words

     
#wordlist = get_common_wordlist()
#transcript = get_words_in_transcript()

#pct_uncommon_words = assess_degree_of_uncommon_words(transcript, wordlist)

#print(pct_uncommon_words)