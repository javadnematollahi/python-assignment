import os
from spleeter.separator import Separator

class separate_vocal_music:
  def __init__(self, path, output_path):
    self.path = path
    self.output_path = output_path

  def use_folder(self):
    for f in os.listdir(self.path):
      if os.path.isfile(os.path.join(self.path,f)):
        separator = Separator("spleeter:2stems")
        prediction = separator.separate_to_file(os.path.join(self.path,f), self.output_path)

  def use_file(self):
      if os.path.isfile(self.path):
        separator = Separator("spleeter:2stems")
        prediction = separator.separate_to_file(self.path, self.output_path)
      else:
        print("The path is not related to a file.")

if __name__ == "__main__":
  path = "singer_voices\singer_music"
  output_path = "singer_voices\singer"
  separate = separate_vocal_music(path, output_path)
  separate.use_folder()