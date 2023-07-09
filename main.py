import config
from logic import downloader
from logic import transcriber
from logic import evaluator


def get_podcast_urls():
    # TODO - this func is very slow - refactor
    with open(config.FRENCH_PODCAST_FILE, "r") as f:
        raw_data = f.readlines()
    podcast_urls = [f.strip() for f in raw_data]
    return podcast_urls

if __name__ == "__main__":
    #podcast_urls = get_podcast_urls()
    # TODO - build check if episode already exists - if so skip it
    #for url in podcast_urls:
        # TODO - update so it saves in the right asset folder
    #    download.download_episode(url)
    
    #download.convert_mp3s_to_wavs()
    # TODO - build same check here - skip if transcript exists
    # Maybe make a flag to force overwrite if needed
    #transcriber.generate_all_transcript_jsons()
    evaluator.add_uncommon_words_to_jsons()
    #difficulty.add_talking_speed_to_jsons()



# create output directories if they don't exist
#for dir in config.OUTPUT:
#    if not os.path.exists(dir):
#        os.makedirs(dir)

#download_episode("https://open.spotify.com/episode/1Beb93JHF0RtSdTfPwFYVK?si=bbe1aa65d22d4be9")
#summarize("https://open.spotify.com/episode/0YqflJb8Wco8IDdGHPNTu8")
#summarize("https://open.spotify.com/episode/46deyZlBRfOvcSzT9NO10r?si=9cb4bc644b024e3b")
