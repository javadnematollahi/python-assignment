import os
from spleeter.separator import Separator

path = "singer_voices\singer_music"
for f in os.listdir(path):
  if os.path.isfile(os.path.join(path,f)):
    separator = Separator("spleeter:2stems")
    prediction = separator.separate_to_file(os.path.join(path,f), "singer_voices\singer")