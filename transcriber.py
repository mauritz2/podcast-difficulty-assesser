import config
import speech_recognition as sr
from pydub import AudioSegment

sound = AudioSegment.from_mp3(config.PODCAST_FILENAME_MP3)
sound.export(config.PODCAST_FILENAME_WAV, format="wav")

r = sr.Recognizer()
with sr.AudioFile(config.PODCAST_FILENAME_WAV) as source:
        audio = r.record(source)  # read the entire audio file                  

        with open(config.PODCAST_FILENAME_TRANSCRIPT, "w+") as transcript_f:
                transcript = r.recognize_google(audio, language="fr-FR")
                print(transcript)
                transcript_f.write(transcript)
                print("Writing to file complete")