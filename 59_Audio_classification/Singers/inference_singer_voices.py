import pydub
import tensorflow as tf
import os
import numpy as np

path = "singer_voices/test/yegane_sample.wav"
audio = pydub.AudioSegment.from_file(path)
audio = audio.set_sample_width(2)
# audio = audio.set_frame_rate(48000)
audio = audio.set_channels(1)
chunks = pydub.silence.split_on_silence(audio, min_silence_len=500, silence_thresh=-25)
result = sum(chunks)

loaded_model = tf.keras.models.load_model('best_model_singer')

singers = []
for f in os.listdir("singer_voices/dataset"):
    singers.append(f.split('_')[0])

result.export(f"new_file.wav", format="wav")
path = "new_file.wav"
x = tf.io.read_file(path)
x, sample_rate = tf.audio.decode_wav(x, desired_channels=1, desired_samples=48000,)
x = tf.squeeze(x, axis=-1)
x = x[tf.newaxis,...]

pred = loaded_model(x)
print(np.argmax(pred))
print("voice belong to: ",singers[np.argmax(pred)])