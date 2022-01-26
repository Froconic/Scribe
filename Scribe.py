import speech_recognition  as sr
import pyaudio
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("microphone \"{1}\" found for 'Microphone(device_index={0})'".format(index, name))
#
filename = "audio/test.wav"
#
# # initialize the recognizer
r = sr.Recognizer()
# Short clips
# open the file
# with sr.AudioFile(filename) as source:
#     # listen for the data (load audio to memory)
#     audio_data = r.record(source)
#     # recognize (convert from speech to text)
#     text = r.recognize_google(audio_data)
#     print(text)

#     #Large clips
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text
path = "audio/01052022273.WAV"
print("\nFull Text:", get_large_audio_transcription(path))

# #Microphone
# with sr.Microphone(   ) as source:
#     # read the audio data from the default microphone
#     audio = r.record(source, duration=5)
#     print("Recognizing...")
#     # convert speech to text
#     text = r.recognize_google(audio)
#     print("Done.... Printing Now....")
#     print(text)
   
# with open("test-results.wav", "wb") as f:
#     f.write(audio.get_wav_data())