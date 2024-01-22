import tensorflow as tf
import numpy as np
import pandas as pd
import time


class EmojiTextClassifier:
    def __init__(self) -> None:
        pass

    def read_csv(self, file_path):
        df = pd.read_csv(file_path)
        X = np.array(df["sentence"])
        Y = np.array(df["label"], dtype=int)
        return X,Y

    def load_dataset(self, dataset_path, word_vectors,feature_count):
        self.X_train, self.Y_train = self.read_csv(f"{dataset_path}/train.csv")
        self.X_test, self.Y_test = self.read_csv(f"{dataset_path}/test.csv")
        x_train_avg = []
        x_test_avg = []
        for x_train in self.X_train:
            x_train_avg.append(self.sentence_to_feature_vectors_avg(x_train, word_vectors,feature_count))
        for x_test in self.X_test:    
            x_test_avg.append(self.sentence_to_feature_vectors_avg(x_test, word_vectors,feature_count))
        self.X_train = np.array(x_train_avg)
        self.X_test = np.array(x_test_avg)

        self.Y_train = tf.keras.utils.to_categorical(self.Y_train, num_classes=5)
        self.Y_test = tf.keras.utils.to_categorical(self.Y_test, num_classes=5)
        return self.X_train.shape, self.X_test.shape

    def load_feature_vectors(self, features_path):
        f = open(features_path, encoding="utf-8")

        self.word_vectors = {}
        for line in f:
            line = line.strip().split()
            word = line[0]
            vector = np.array(line[1:], dtype=np.float64)
            self.word_vectors[word] = vector
        return  self.word_vectors
    
    def sentence_to_feature_vectors_avg(self, sentence, word_vectors, feature_count=50):
        # try:
            sente = sentence.lower()
            words = sente.strip().split(" ")
            sum_vectors = np.zeros((feature_count, ))
            for word in words:
                if word !="":
                    sum_vectors += word_vectors[word]

            avg_vectors = sum_vectors/len(words)
            return avg_vectors
        # except:
        #     return "There is a problem with sentence"

    def load_model(self, input_shape=(50, ), loss="categorical_crossentropy", model_path=None):
        if model_path == None:
            self.model = tf.keras.models.Sequential([
                    tf.keras.layers.Dropout(0.2),
                    tf.keras.layers.Dense(10, input_shape=input_shape, activation="relu"),
                    tf.keras.layers.Dense(5,  activation="softmax")
                    ])
            self.model.compile(
                optimizer=tf.keras.optimizers.Adam(),
                loss=loss,
                metrics=["accuracy"]
            )
        else:
            self.model = tf.keras.models.load_model(model_path)
    
    def train(self, best_model_path="best_model", monitor_for_best_model='val_accuracy',monitor_for_early_stop='val_accuracy',epochs=200):
        checkpoint = tf.keras.callbacks.ModelCheckpoint(best_model_path,
                                                        save_best_only=True,
                                                        monitor=monitor_for_best_model)
        stop_early = tf.keras.callbacks.EarlyStopping(monitor=monitor_for_early_stop, patience=50)
        self.model.fit(self.X_train, self.Y_train, 
                       epochs=epochs, 
                       validation_data=(self.X_test, self.Y_test),
                       callbacks=[stop_early, checkpoint]
                       )

    def test(self, best_model_path=None, test=True):
        if best_model_path != None:
            self.model = tf.keras.models.load_model(best_model_path)
        if test == True:
            self.model.evaluate(self.X_test, self.Y_test)
        else:
            self.model.evaluate(self.X_train, self.Y_train)

    def predict(self, test_sentence, word_vectors, feature_count):
        my_test_avg = self.sentence_to_feature_vectors_avg(test_sentence, word_vectors, feature_count)
        my_test_avg = np.array([my_test_avg])
        result = self.model.predict(my_test_avg)
        y_pred = np.argmax(result)
        emojies = ["❤️", "⚾", "🙂", "😒", "🍴" ]
        print(emojies[y_pred])
        return emojies[y_pred]


if __name__=="__main__":
    feature_count = 50
    model_path_save = f"best_model_{feature_count}d"
    etc = EmojiTextClassifier()
    word_vectors = etc.load_feature_vectors(f"features\glove.6B.{feature_count}d.txt")
    etc.load_dataset("Emoji_Text_Classification", word_vectors, feature_count=feature_count)
    etc.load_model(input_shape=(feature_count, ))#, model_path=model_path_save)
    etc.train(best_model_path=model_path_save)
    etc.test(model_path_save, test=False)
    etc.test(model_path_save, test=True)
    X,Y = etc.read_csv("Emoji_Text_Classification/test.csv")
    start = time.time() 
    for x in X:
        etc.predict(x, word_vectors, feature_count)
    print("Inference time: ",(time.time() - start)/(len(X)))