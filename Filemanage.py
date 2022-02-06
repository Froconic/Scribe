import Scribe as scribe

path = "Audios/test.wav"
with open('test.txt', 'w') as f:
    f.write(scribe.get_large_audio_transcription(path))
    print("\nFull Text:", scribe.get_large_audio_transcription(path))