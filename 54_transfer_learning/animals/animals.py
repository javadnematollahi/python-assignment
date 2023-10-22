import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import preprocess_input
import matplotlib.pyplot as plt
import numpy as np

dataset_path_train = "dataset/animal"

idg=tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1./255,
    horizontal_flip=True,
    brightness_range=(0.8,1),
    zoom_range=0.1,
    validation_split=0.1,
    preprocessing_function=preprocess_input
)

train_data_animal=idg.flow_from_directory(
    dataset_path_train,
    target_size=(224,224),
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    subset='training',
)
val_data_animal=idg.flow_from_directory(
    dataset_path_train,
    target_size=(224,224),
    class_mode='categorical',
    batch_size=32,
    shuffle=True,
    subset='validation',
)

model = tf.keras.applications.RegNetX032(include_top=False , weights="imagenet", input_shape=(224,224,3))

my_model_animal = models.Sequential([
    model,
    layers.Flatten(),
    layers.Dense(512, activation="relu"),
    layers.Dropout(0.2),
    layers.Dense(256, activation="relu"),
    layers.Dropout(0.2),
    layers.Dense(5, activation="softmax"),
])

my_model_animal.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.001),
              loss = tf.keras.losses.categorical_crossentropy,
              metrics = ['accuracy'])

checkpoint = tf.keras.callbacks.ModelCheckpoint("best_model_animal",
                                            save_best_only=True)
stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

history_animal = my_model_animal.fit(train_data_animal, validation_data=val_data_animal, epochs=20 ,callbacks=[stop_early, checkpoint])

loaded_model_animal = tf.keras.models.load_model('best_model_animal')
# new_history = loaded_model.fit(train_dataset, epochs=20,
#                     validation_data=test_dataset,
#                     validation_steps=30,
#                     callbacks=[stop_early, checkpoint],
#                     )
loaded_model_animal.evaluate(val_data_animal)