import Transcribe as transcribe
import os

path = "audio test/"
text = "text/"
object = os.scandir(path)

def scribe(object):
  for n in object:
    filename = os.path.join(text, n.name + ".txt")
    if n.is_file():
      print(n.name)
      print("Creating text file...")
      a, b = filename.split(".wav")
      print(a)
      print(b)
      filename = a + b
      print(filename)
      if os.path.exists(filename):
          print("File already exists")
      else:
        print("Transcription working...")
        transcribe.get_large_audio_transcription(n)
        print("Done!")
        print("Text working...")
        print(transcribe.whole_text)
        with open(filename, "w") as f:
            print("Writing to file...")
            f.write(transcribe.whole_text)
            print("Done!")

scribe(object)
object.close()