import tensorflow as tf
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import numpy as np
import glob
import cv2
import os
from load_process_data import *
import wandb
from wandb.keras import (
   WandbMetricsLogger,
   WandbModelCheckpoint,
)
run = wandb.init(project="House_price_by_numerical")
config = wandb.config
wandb_callbacks = [
   WandbMetricsLogger(log_freq=5),
   WandbModelCheckpoint("models"),
]

df = load_house_attributes('Houses Dataset/HousesInfo.txt')
(train, test) = train_test_split(df, test_size=0.25, random_state=42)
maxPrice = train["price"].max()
trainY = train["price"] / maxPrice
testY = test["price"] / maxPrice
trainX, testX = process_house_attributes(df, train, test)

my_model = Sequential([

    tf.keras.layers.Dense(12, input_shape=(10,),activation="relu"),
    # tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(4, activation="relu"),
    # tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1, activation="linear"),
])

my_model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4),
              loss = tf.keras.losses.mean_absolute_percentage_error
              )

checkpoint = tf.keras.callbacks.ModelCheckpoint("best_model_house_price_numerical",
                                            save_best_only=True)
stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=50)

history = my_model.fit(
    x=trainX, y=trainY,
	  validation_data=(testX, testY),
    epochs=200 ,
    callbacks=[stop_early, checkpoint, wandb_callbacks]
    )

loaded_model = tf.keras.models.load_model('best_model_house_price_numerical')
loaded_model.save('weights/numerical_House_price.h5')
loaded_model.evaluate(testX, testY)

