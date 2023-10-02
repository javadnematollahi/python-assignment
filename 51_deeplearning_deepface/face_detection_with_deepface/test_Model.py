import os
import numpy as np
from deepface import DeepFace
import tensorflow as tf

data_folder = 'assets'
images = []
files = []
feature = dict()
featuress = []

for f in os.listdir(data_folder) :
    files.append(f)

files.sort()
# print(files)
embedding_objs = DeepFace.represent(img_path = 'dataset/mehran_ghaforian.jpg', model_name = "ArcFace")
a=np.asarray(embedding_objs[0]["embedding"])
a = a.reshape(-1,512)
print(a.shape)
print(len(embedding_objs[0]["embedding"]))
model= tf.keras.models.load_model("weights/face_model.h5")
out = model.predict(a)
out = np.argmax(out)
# print(out)
print(files[out])