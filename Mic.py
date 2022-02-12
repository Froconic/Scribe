import speech_recognition as sr
import pyaudio

r = sr.Recognizer()


#Microphone
with sr.Microphone(   ) as source:
    # read the audio data from the default microphone
    audio = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio)
    print("Done.... Printing Now....")
    print(text)

with open("test-results.wav", "wb") as f:
    f.write(audio.get_wav_data())