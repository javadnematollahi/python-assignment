import tensorflow as tf
import os

dataset_path = "dataset"

train_data = tf.keras.utils.audio_dataset_from_directory(
    dataset_path,
    batch_size=4,
    shuffle=True,
    validation_split=0.2,
    subset='training',
    output_sequence_length=48000,
    label_mode="categorical",
    labels="inferred",
    seed=59
)

validation_data = tf.keras.utils.audio_dataset_from_directory(
    dataset_path,
    batch_size=4,
    shuffle=True,
    validation_split=0.2,
    subset='validation',
    output_sequence_length=48000,
    label_mode="categorical",
    labels="inferred",
    seed=59
)

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv1D(32, kernel_size=40, strides=16, activation='relu',input_shape=(48000,1)),
    tf.keras.layers.MaxPool1D(4),
    tf.keras.layers.Conv1D(128, kernel_size=3, activation='relu'),
    tf.keras.layers.MaxPool1D(4),
    tf.keras.layers.Conv1D(64, kernel_size=10, activation='relu'), 
    tf.keras.layers.MaxPool1D(4),  
    tf.keras.layers.Conv1D(64, kernel_size=10, activation='relu'), 
    tf.keras.layers.MaxPool1D(4),  
    tf.keras.layers.Conv1D(32, kernel_size=3, activation='relu'), 
    tf.keras.layers.MaxPool1D(4),  

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(32,activation='relu'),
    tf.keras.layers.Dense(18,activation='softmax')
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss="categorical_crossentropy",
    metrics=['accuracy']
)

checkpoint = tf.keras.callbacks.ModelCheckpoint("best_friend_model",
                                            save_best_only=True, monitor='val_accuracy')
stop_early = tf.keras.callbacks.EarlyStopping(monitor='val_accuracy', patience=50)

model.fit(
    train_data,
    validation_data=validation_data,
    epochs=150,
    callbacks=[stop_early, checkpoint]
)

loaded_model = tf.keras.models.load_model('best_friend_model')
loaded_model.evaluate(validation_data)
