import os
import config
import json
import speech_recognition as sr
from pydub import AudioSegment


class Transcriber:
        def __init__(self, audio_folder:str):
                self.audio_folder = audio_folder
                # Check if folder exists and if not create it (?)
                self.r = sr.Recognizer()


        def generate_all_transcripts(self):
                wav_files = self.get_list_of_wav_files()
                for file in wav_files:
                        audio_filepath = config.WAV_FOLDERPATH / file
                        self.generate_transcript(audio_filepath)


        def generate_transcript(self, audio_filepath):
                transcript_dict = {}
                print(audio_filepath)
                with sr.AudioFile(audio_filepath) as source:
                        audio = self.r.record(source)
                        audio_length = int(source.DURATION)
                        
                        transcript = self.r.recognize_google(audio, language="fr-FR")
                        transcript_name = audio_filepath[:-3] + "_transcript.json"
                        
                        transcript_dict["transcript"] = transcript
                        transcript_dict["audio_length"] = audio_length
                        with open(transcript_name, 'w') as output_file:
                                json.dump(transcript_dict, output_file)


        def get_list_of_wav_files(self):
                files_in_folder = os.listdir(self.audio_folder)
                #print(self.audio_folder)
                #files_in_folder = os.listdir("outputs/audio_wav_files")
                #print(files_in_folder)
                wav_files = [f for f in files_in_folder if f[-3:] == "wav"]
                return wav_files


tr = Transcriber(config.WAV_FOLDERPATH)
tr.generate_all_transcripts()

#sound = AudioSegment.from_mp3(config.PODCAST_FILENAME_MP3)
#sound.export(config.PODCAST_FILENAME_WAV, format="wav")
#print(f"My duration is {sound.duration_seconds}")

#r = sr.Recognizer()
#with sr.AudioFile(config.PODCAST_FILENAME_WAV) as source:
#        audio = r.record(source)  # read the entire audio file                  #
#
#        with open(config.PODCAST_FILENAME_TRANSCRIPT, "w+") as transcript_f:
#                transcript = r.recognize_google(audio, language="fr-FR")
#                print(transcript)
#                transcript_f.write(transcript)
#                print("Writing to file complete")