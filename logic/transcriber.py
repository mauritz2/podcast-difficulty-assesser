import json
import speech_recognition as sr

import config
from .utils import get_files_of_type

r = sr.Recognizer()

def generate_all_transcript_jsons():
        wav_files = get_files_of_type(config.WAV_FOLDERPATH, "wav")
        for filename in wav_files:
                #audio_filepath = config.WAV_FOLDERPATH / file_name
                generate_transcript_json(filename)

def generate_transcript_json(filename:str):
        transcript_dict = {}
        wav_filepath = str(config.WAV_FOLDERPATH / filename)
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
