with open('test.txt', 'w') as f:
    f.write(get_large_audio_transcription(path))
    print("\nFull Text:", get_large_audio_transcription(path))