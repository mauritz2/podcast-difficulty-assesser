import config
from logic import downloader
from logic import transcriber
from logic import evaluator
from logic import printer

def get_podcast_urls():
    with open(config.FRENCH_PODCAST_FILE, "r") as f:
        raw_data = f.readlines()
    podcast_urls = [f.strip() for f in raw_data]
    return podcast_urls

if __name__ == "__main__":
    podcast_urls = get_podcast_urls()
    for url in podcast_urls:
        downloader.download_episode(url)
    #downloader.convert_mp3s_to_wavs()
    #transcriber.generate_all_transcript_jsons()
    #evaluator.add_uncommon_words_to_jsons()
    #evaluator.add_words_per_min_to_jsons()
    #printer.export_podcast_difficulty()