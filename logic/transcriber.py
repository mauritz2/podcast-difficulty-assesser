import json
import speech_recognition as sr

import config
from .utils import get_files_of_type

r = sr.Recognizer()

def generate_all_transcripts():
        jsons = get_files_of_type(config.TRANSCRIPT_FOLDERPATH, "json")
        for filename in jsons:
                generate_transcript(filename)

def generate_transcript(filename:str):
        transcript_dict = {}
        #wav_filepath = str(config.WAV_FOLDERPATH / filename)
        transcript_filepath = config.TRANSCRIPT_FOLDERPATH / (filename[:-4] + "_transcript.json") 
        with sr.AudioFile(wav_filepath) as source:         
                audio = r.record(source)
                transcript = r.recognize_google(audio, language=config.PODCAST_LANGUAGE)
                transcript_dict["transcript"] = transcript
                
                audio_length = int(source.DURATION)
                transcript_dict["audio_length"] = audio_length
                
                with open(transcript_filepath, 'w', encoding="utf8") as output_file:
                        json.dump(transcript_dict, output_file, ensure_ascii=False)
        print(f"Transcription saved at {transcript_filepath}")
        print(transcript_dict["transcript"])
