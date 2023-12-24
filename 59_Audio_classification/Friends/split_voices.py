import pydub
import os


def split_voices():
    for file in os.listdir('wav_data'):
        audio = pydub.AudioSegment.from_file(os.path.join('wav_data', file))
        chunks = pydub.utils.make_chunks(audio, 1000)
        person_name = file.split('.')[0]
        os.makedirs(os.path.join('dataset',person_name), exist_ok=True)

        for i,chunk in enumerate(chunks):
            if len(chunk) >= 1000:
                chunk.export(os.path.join('dataset',person_name, f'voice_{i}.wav'))

if __name__ == "__main__":
    split_voices()
