import pydub
import os

def remove_silence_and_to_wav():
    files = os.listdir('data')
    for file in files:
        audio = pydub.AudioSegment.from_file(os.path.join('data', file))

        chunks = pydub.silence.split_on_silence(audio, min_silence_len=2000, silence_thresh=-45)
        result = sum(chunks)
        file_name = file.split('.')[0]
        result.export(os.path.join('wav_data', f'{file_name}.wav'), format="wav")


if __name__ == "__main__":
    remove_silence_and_to_wav()