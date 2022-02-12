import Transcribe as transcribe
import os

# Variables declared
path = "audio test/"
text = "text/"
# Opens the directory
object = os.scandir(path)

# Loops through the directory
def scribe(object):
  for n in object:
    filename = os.path.join(text, n.name + ".txt")
    # Checks if file exists
    if n.is_file():
      print(n.name)
      print("Creating text file...")
      # Split file name to create new file name
      a, b = filename.split(".wav")
      print(a)
      print(b)
      filename = a + b
      print(filename)
      # Checks if file exists
      if os.path.exists(filename):
          print("File already exists")
      else:
        print("Transcription working...")
        transcribe.get_large_audio_transcription(n)
        print("Done!")
        print("Text working...")
        print(transcribe.whole_text)
        # Write transcription to  text file
        with open(filename, "w") as f:
            print("Writing to file...")
            f.write(transcribe.whole_text)
            print("Done!")

scribe(object)
object.close()