import pydub
import os
import tensorflow as tf
from collections import Counter
import numpy as np



class Audio_classification:
    def __init__(self):
        ...
        
    def merge_voices(self, input_path, output_path):
        two_files = []
        for fil in os.listdir(input_path):
            name = fil.split(".")[0]
            if len(name.split("_")) == 2:
                if name.split("_")[0] not in two_files:
                    two_files.append(name.split("_")[0])
                    result= 0
                    for f in os.listdir(input_path):
                        if f.split(".")[0].split("_")[0] == name.split("_")[0] :
                            result += pydub.AudioSegment.from_file(f'{input_path}/{f}')
                    result.export(f"{output_path}/{name.split('_')[0]}.wav", format='wav')
            else:
                result = pydub.AudioSegment.from_file(f'{input_path}/{fil}')
                result.export(f"{output_path}/{name}.wav", format='wav')
    def remove_silence_and_to_wav(self, input_path, output_path, min_silence_len=2000, silence_thresh=-45, output_format="wav"):
        files = os.listdir(input_path)
        for file in files:
            audio = pydub.AudioSegment.from_file(os.path.join(input_path, file))
            chunks = pydub.silence.split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh)
            result = sum(chunks)
            file_name = file.split('.')[0]
            result.export(os.path.join(output_path, f'{file_name}.{output_format}'), format=output_format)
    def split_voices(self, input_path, output_path):
        for file in os.listdir(input_path):
            audio = pydub.AudioSegment.from_file(os.path.join(input_path, file))
            chunks = pydub.utils.make_chunks(audio, 1000)
            person_name = file.split('.')[0]
            os.makedirs(os.path.join(output_path,person_name), exist_ok=True)
        for i,chunk in enumerate(chunks):
            if len(chunk) >= 1000:
                chunk.export(os.path.join(output_path,person_name, f'voice_{i}.wav'), format='wav')
    def make_train_validation(self, dataset_path, validation_split=0.2):
        self.dataset_path=dataset_path
        self.train_data = tf.keras.utils.audio_dataset_from_directory(
            self.dataset_path,
            batch_size=1,
            shuffle=True,
            validation_split=validation_split,
            subset='training',
            output_sequence_length=48000,
            label_mode="categorical",
            labels="inferred",
            seed=59
        )
        self.validation_data = tf.keras.utils.audio_dataset_from_directory(
            self.dataset_path,
            batch_size=1,
            shuffle=True,
            validation_split=validation_split,
            subset='validation',
            output_sequence_length=48000,
            label_mode="categorical",
            labels="inferred",
            seed=59
        )
        return self.train_data, self.validation_data
    def make_model(self, activation='relu',optimizer=tf.keras.optimizers.Adam(), loss='categorical_crossentropy'):
        self.model = tf.keras.models.Sequential([
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

        self.model.compile(
            optimizer=optimizer,
            loss=loss,
            metrics=['accuracy']
        )
    def fit_model(self, best_model_path="best_friend_model", monitor_for_bset_model='val_accuracy',monitor_for_early_stop='val_accuracy',epochs=50):
        os.makedirs(best_model_path, exist_ok=True)
        checkpoint = tf.keras.callbacks.ModelCheckpoint(best_model_path,
                                                        save_best_only=True, monitor=monitor_for_bset_model)
        stop_early = tf.keras.callbacks.EarlyStopping(monitor=monitor_for_early_stop, patience=50)

        history = self.model.fit(
                            self.train_data,
                            validation_data=self.validation_data,
                            epochs=epochs,
                            callbacks=[stop_early, checkpoint]          
                            )
    def evaluate_model(self, best_model_path):
        loaded_model = tf.keras.models.load_model(best_model_path)
        loaded_model.evaluate(self.validation_data)


    def inference_model(self, sample, friend_list="friend_voice_data/dataset", model_path="best_friend_model"):
        if isinstance(friend_list, str):
            friends = []
            for f in os.listdir(friend_list):
                if os.path.isfile(os.path.join(friend_list,f))==False:
                    friends.append(f)
            print(friends)
        elif isinstance(friend_list, list):
            friends = friend_list

        audio  = pydub.AudioSegment.from_file(sample)
        audio = audio.set_sample_width(2)
        audio = audio.set_frame_rate(48000)
        audio = audio.set_channels(1)
        chunks = pydub.silence.split_on_silence(audio, min_silence_len=2000, silence_thresh=-45)
        result = sum(chunks)
        chunkses = pydub.utils.make_chunks(result, 1000)
        os.makedirs('sample', exist_ok=True)
        for fr in os.listdir('sample'):
            os.remove(os.path.join('sample',fr))

        for i,chunk in enumerate(chunkses):
            if len(chunk) >= 1000:
                chunk.export(os.path.join('sample', f'voice_{i}.wav'), format='wav')
        loaded_model = tf.keras.models.load_model(model_path)

        preds = []
        for f in os.listdir('sample'):
            if os.path.isfile(os.path.join('sample',f)):
                x = tf.io.read_file(os.path.join('sample',f))
                x, sample_rate = tf.audio.decode_wav(x, desired_channels=1, desired_samples=48000,)
                x = tf.squeeze(x, axis=-1)
                x = x[tf.newaxis,...]
                pred = loaded_model(x)
                preds.append(np.argmax(pred))
        unique = Counter(preds).keys()
        num = Counter(preds).values()
        unique=list(unique)
        num=list(num)
        print(friends[unique[np.argmax(num)]])

if __name__ == "__main__":
    audio_classify = Audio_classification()
    # audio_classify.merge_voices("friend_voice_data/raw_data", "friend_voice_data/stick_data")
    # audio_classify.remove_silence_and_to_wav('friend_voice_data/data', 'friend_voice_data/wav_data')
    # audio_classify.split_voices('friend_voice_data/wav_data', 'friend_voice_data/dataset')
    # audio_classify.make_train_validation("friend_voice_data/dataset")
    # audio_classify.make_model()
    # audio_classify.fit_model()
    # audio_classify.evaluate_model("best_friend_model")
    audio_classify.inference_model("friend_voice_data/javad_testvoice/javad_voice_test2.ogg")





    


