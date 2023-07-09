import os
import config
import json
import speech_recognition as sr

r = sr.Recognizer()

def generate_all_transcripts():
        wav_files = get_list_of_wav_files()
        for file in wav_files:
                audio_filepath = config.WAV_FOLDERPATH / file
                generate_transcript(str(audio_filepath))


def generate_transcript(audio_filepath:str):
        transcript_dict = {}

        with sr.AudioFile(audio_filepath) as source:
                audio = r.record(source)
                audio_length = int(source.DURATION)
                
                transcript = r.recognize_google(audio, language=config.PODCAST_LANGUAGE)
                transcript_name = audio_filepath[:-3] + "_transcript.json"
                
                transcript_dict["transcript"] = transcript
                transcript_dict["audio_length"] = audio_length
                # TODO: Add so it saves to output files, creating if if it doesn't exist
                with open(transcript_name, 'w', encoding="utf8") as output_file:
                        json.dump(transcript_dict, output_file, ensure_ascii=False)


def get_list_of_wav_files():
        files_in_folder = os.listdir(config.WAV_FOLDERPATH)
        wav_files = [f for f in files_in_folder if f[-3:] == "wav"]
        return wav_files


generate_all_transcripts()
