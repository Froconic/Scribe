import Scribe as scribe
import os

path = "audio test/"
text = "audio test/text/"
object = os.scandir(path)

for n in object:
  if n.is_file():
    print(n.name)
    print("Transcription working...")
    scribe.get_large_audio_transcription(n)
    print("Done!")
    print("Text working...")
    print(scribe.whole_text)
    with open(os.path.join(text, n.name + ".txt"), "w") as f:
      print("Writing to file...")
      f.write(scribe.whole_text)
    print("Done!")

object.close()

# def scribe(file):
#   for file in os.listdir(path):
#     if file.endswith(".wav"):
#       with open(file,"r+")as f:
#         print("Working...")
#         scribe.get_large_audio_transcription(path)
#         print("Done!")
#         f.write(scribe.whole_text)
        
# with open('Text/test.txt', 'w') as f:
#     print("Working...")
#     scribe.get_large_audio_transcription(path)
#     print("Done!")
#     print(scribe.whole_text)
#     f.write(scribe.whole_text)
#     print("Audio transcribed successfully")
