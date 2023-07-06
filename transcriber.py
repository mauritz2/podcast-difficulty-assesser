import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav
PODCAST_FILENAME_BASE = "french_podcast"
PODCAST_FILENAME_MP3 = PODCAST_FILENAME_BASE + ".mp3" 
PODCAST_FILENAME_WAV = PODCAST_FILENAME_BASE + ".wav"
PODCAST_FILENAME_TRANSCRIPT = PODCAST_FILENAME_BASE + "_transcript.txt"

sound = AudioSegment.from_mp3(PODCAST_FILENAME_MP3)
sound.export(PODCAST_FILENAME_WAV, format="wav")

# use the audio file as the audio source                                        
r = sr.Recognizer()
with sr.AudioFile(PODCAST_FILENAME_WAV) as source:
        audio = r.record(source)  # read the entire audio file                  

        with open(PODCAST_FILENAME_TRANSCRIPT, "w+") as transcript_f:
                transcript = r.recognize_google(audio, language="fr-FR")
                print(transcript)
                transcript_f.write(transcript)
                print("Writing to file complete")