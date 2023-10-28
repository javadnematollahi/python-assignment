import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import preprocess_input
import matplotlib.pyplot as plt
import numpy as np
import wandb
from wandb.keras import (
   WandbMetricsLogger,
   WandbModelCheckpoint,
)

run = wandb.init(project="Akhund_human")
config = wandb.config
wandb_callbacks = [
   WandbMetricsLogger(log_freq=5),
   WandbModelCheckpoint("models"),
]

dataset_path_train = "dataset/Akhund-Human"
width=height=224
idg=tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    horizontal_flip=True,
    brightness_range=(0.8,1),
    zoom_range=0.1,
    validation_split=0.1,
)

train_data=idg.flow_from_directory(
    dataset_path_train,
    target_size=(width,height),
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    subset='training',
)
val_data=idg.flow_from_directory(
    dataset_path_train,
    target_size=(width,height),
    class_mode='categorical',
    batch_size=32,
    shuffle=False,
    subset='validation',
)

model = tf.keras.applications.MobileNet(
    include_top=False,
    weights="imagenet",
    input_shape=(width,height,3),
    pooling ='avg'
    )

for layer in model.layers[0:-10]:
  layer.trainable = False

my_model = models.Sequential([
    model,
    layers.Flatten(),
    layers.Dropout(0.2),
    layers.Dense(2, activation="softmax"),
])

my_model.compile(optimizer = tf.keras.optimizers.RMSprop(learning_rate=1e-4),
              loss = tf.keras.losses.categorical_crossentropy,
              metrics = ['accuracy'])

checkpoint = tf.keras.callbacks.ModelCheckpoint("best_model_Akhund_human",
                                            save_best_only=True)
stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

history = my_model.fit(
    train_data,
    validation_data=val_data,
    epochs=20 ,
    callbacks=[stop_early, checkpoint,wandb_callbacks]
    )

loaded_model = tf.keras.models.load_model('best_model_Akhund_human')
loaded_model.evaluate(val_data)

loaded_model.save('dataset/Akhund_Human.h5')

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(20)

plt.figure(figsize=(12, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
