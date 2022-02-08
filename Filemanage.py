import Scribe as scribe

path = "Audios/test.wav"
text = "Text/"
with open('Text/test.txt', 'w') as f:
    print("Working...")
    scribe.get_large_audio_transcription(path)
    print("Done!")
    print(scribe.whole_text)
    f.write(scribe.whole_text)
    print("Audio transcribed successfully")
