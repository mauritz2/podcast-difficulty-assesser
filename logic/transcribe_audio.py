import json
import speech_recognition as sr

import config
from .utils import get_files_of_type

r = sr.Recognizer()

def generate_all_transcripts():
        wav_files = get_files_of_type(config.WAV_FOLDERPATH, "wav")
        for filename in wav_files:
                #audio_filepath = config.WAV_FOLDERPATH / file_name
                generate_transcript(filename)

def generate_transcript(filename:str):
        transcript_dict = {}
        wav_filepath = str(config.WAV_FOLDERPATH / filename)
        transcript_filepath = config.TRANSCRIPT_FOLDERPATH / (filename[:-4] + "_transcript.json") 
        with sr.AudioFile(wav_filepath) as source:
                audio = r.record(source)
                audio_length = int(source.DURATION)
                
                transcript = r.recognize_google(audio, language=config.PODCAST_LANGUAGE)
                #transcript_name = filename[:-4] + "_transcript.json"
                #filepath = config.TRANSCRIPT_FOLDERPATH / transcript_name

                transcript_dict["transcript"] = transcript
                transcript_dict["audio_length"] = audio_length
                # TODO: Add so it saves to output files, creating if if it doesn't exist
                with open(transcript_filepath, 'w', encoding="utf8") as output_file:
                        json.dump(transcript_dict, output_file, ensure_ascii=False)
                print("JSON saving complete")

