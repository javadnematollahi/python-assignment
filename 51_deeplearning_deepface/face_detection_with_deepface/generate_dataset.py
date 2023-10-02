import os
from deepface import DeepFace
import pandas as pd


def generate_dataset():
  data_folder = 'assets'
  files = []
  feature = dict()
  featuress = []

  for f in os.listdir(data_folder) :
      files.append(f)
  print(files)
  for folder in files:
    new_path = os.path.join(data_folder, folder)
    print(new_path)
    print(os.listdir(new_path))
    for filename in os.listdir(new_path) :
      print(os.path.join(new_path, filename))
      embedding_objs = DeepFace.represent(img_path = os.path.join(new_path, filename), model_name = 'ArcFace', enforce_detection = False)
      feature['label'] = folder
      feature['file_name'] = filename
      for i in range(len(embedding_objs[0]["embedding"])) :
        feature[f'feature{i+1}'] = embedding_objs[0]["embedding"][i]
      feature_copy = feature.copy()
      featuress.append(feature_copy)
      feature.clear()

  df_input = pd.DataFrame(featuress)
  df_input.to_csv('dataset/input_data.csv', mode = 'w', index = False)