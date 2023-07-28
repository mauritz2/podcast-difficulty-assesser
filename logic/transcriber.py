import json
import speech_recognition as sr

import config
from .utils import get_files_of_type, get_value_from_json, add_value_to_json

r = sr.Recognizer()

def generate_all_transcripts():
        jsons = get_files_of_type(config.TRANSCRIPT_FOLDERPATH, "json")
        for filename in jsons:
                generate_transcript(filename)

def generate_transcript(filename:str):
        #transcript_dict = {}
        #wav_filepath = str(config.WAV_FOLDERPATH / filename)
        #transcript_filepath = config.TRANSCRIPT_FOLDERPATH / (filename[:-4] + ".json") # + "_transcript.json") 
        transcript_filepath = config.TRANSCRIPT_FOLDERPATH / filename # [:-4] + ".json") # + "_transcript.json") 
        #get_value_from_json(transcript_filepath, )
        wav_filename = get_value_from_json(transcript_filepath, "wav_filename")
        with sr.AudioFile(str(config.WAV_FOLDERPATH / wav_filename)) as source:         
                audio = r.record(source)
                transcript = r.recognize_google(audio, language=config.PODCAST_LANGUAGE)
                
                add_value_to_json(transcript_filepath, "transcript", transcript)


                #transcript_dict["transcript"] = transcript
                
                audio_length = int(source.DURATION)
                
                add_value_to_json(transcript_filepath, "audio_length", audio_length)
                
                #transcript_dict["audio_length"] = audio_length
                
                #with open(transcript_filepath, 'w', encoding="utf8") as output_file:
                #        json.dump(transcript_dict, output_file, ensure_ascii=False)
        print(f"Transcription saved at {transcript_filepath}")
        #print(transcript_dict["transcript"])
