import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from cv2 import imread, resize, cvtColor, COLOR_BGR2RGB
import matplotlib.pyplot as plt
import wandb
from wandb.keras import (
   WandbMetricsLogger,
   WandbModelCheckpoint,
)
run = wandb.init(project="Age_detection")
config = wandb.config
wandb_callbacks = [
   WandbMetricsLogger(log_freq=5),
   WandbModelCheckpoint("models"),
]
width= height= 128
images = []  #X
ages = []    #Y
for image_name in os.listdir("assets/UTKFace"):
    ages.append(int(image_name.split('_')[0]))
    image = imread("assets/UTKFace"+image_name)
    image = resize(image, (width,height))
    image = cvtColor(image, COLOR_BGR2RGB)
    images.append(image)
images_pd = pd.Series(images, name="Images")
ages_pd = pd.Series(ages, name="Ages")
df = pd.concat([images_pd, ages_pd], axis=1)
del images
del ages
df = df[df['Ages']<80]
df_26_1 = df[(df["Ages"] == 26) | (df["Ages"] == 1)]
df_without26_1 = df[(df["Ages"] != 26) & (df["Ages"] != 1)]
df_26_1 = df_26_1.sample(frac=0.3)
df = pd.concat([df_26_1, df_without26_1], axis=0)
del df_26_1
del df_without26_1
X = np.array(df['Images'].values.tolist())
Y = np.array(df['Ages'].values.tolist())
del df
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size=0.2)
del X
del Y
image_data_generator = ImageDataGenerator(
    rescale=1./255,
    horizontal_flip=True,
)
train_data = image_data_generator.flow(
                                       X_train,
                                       Y_train,
                                       batch_size=32,
                                       shuffle=True
                                       )
validation_data = image_data_generator.flow(
                                       X_validation,
                                       Y_validation,
                                       batch_size=16,
                                       shuffle=False
                                       )
del X_train
del Y_train
del X_validation
del Y_validation
base_model = tf.keras.applications.MobileNet(
    weights='imagenet',
    include_top=False,
    input_shape=(width,height,3),
    pooling='avg'
)
for layer in base_model.layers[0:-10]:
  layer.trainable = False
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(1, activation='relu')
])
model.compile(
    loss= tf.keras.losses.mean_absolute_error,
    optimizer=tf.keras.optimizers.Adam(),
)

checkpoint = tf.keras.callbacks.ModelCheckpoint("best_model_age_detection",
                                            save_best_only=True)
stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=50)
history = model.fit(
          train_data,
          validation_data=validation_data,
          epochs=20,
          callbacks=[stop_early, checkpoint, wandb_callbacks])
loaded_model = tf.keras.models.load_model('best_model_age_detection')
loaded_model.save('assets/Age_prediction.h5')
loaded_model.evaluate(validation_data)

