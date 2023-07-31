import speech_recognition as sr

import config
from .utils import get_files_of_type, get_value_from_json, add_value_to_json

r = sr.Recognizer()

def generate_all_transcripts():
        jsons = get_files_of_type(config.TRANSCRIPT_FOLDERPATH, "json")
        for filename in jsons:
                filepath = config.TRANSCRIPT_FOLDERPATH / filename
                if is_not_transcribed(filepath):
                        generate_transcript(filepath)


def generate_transcript(filepath: str):
        wav_filename = get_value_from_json(filepath, "wav_filename")
        with sr.AudioFile(str(config.WAV_FOLDERPATH / wav_filename)) as source:         
                audio = r.record(source)
                transcript = r.recognize_google(audio, language=config.PODCAST_LANGUAGE)
                add_value_to_json(filepath, "transcript", transcript)
                audio_length = int(source.DURATION)
                
                add_value_to_json(filepath, "audio_length", audio_length)
        print(f"Transcription saved at {filepath}")


def is_not_transcribed(filepath:str):
        transcript = get_value_from_json(filepath, "transcript")
        if transcript == None:
                return True
        else:
                return False
        