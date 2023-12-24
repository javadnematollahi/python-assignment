import pydub
import os


def split_voices():
    for file in os.listdir('singer_voices/rm_silence'):
        audio = pydub.AudioSegment.from_file(os.path.join('singer_voices/rm_silence', file))
        chunks = pydub.utils.make_chunks(audio, 1000)
        person_name = file.split('.')[0]
        os.makedirs(os.path.join('singer_voices/dataset',person_name), exist_ok=True)

        for i,chunk in enumerate(chunks):
            if len(chunk) >= 1000:
                chunk.export(os.path.join('singer_voices/dataset',person_name, f'voice_{i}.wav'), format='wav')

if __name__ == "__main__":
    split_voices()
