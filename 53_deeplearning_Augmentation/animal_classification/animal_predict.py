import os
import numpy as np
import cv2
import tensorflow as tf

data_folder = 'assets/animals'
images = []
files = []
feature = dict()
featuress = []

for f in os.listdir(data_folder) :
    files.append(f)

files.sort()
print(files)

model = tf.keras.models.load_model('weights/animals.h5')
animals = ['🐱','🐶','🐘','🦒','🐼']
for f in os.listdir('test') :
    image = cv2.imread(f'test/{f}')
    image = cv2.resize(image, (224,224))
    image = np.array(image)/255
    # print(image.shape)
    image = np.expand_dims(image, axis=0) 
    # print(image.shape)
    result = model.predict(image)
    # print(result)

    out = np.argmax(result)
    # print(out)
    print(f'real image and model predict are:   {f[:-4]} -> {animals[out]}')
