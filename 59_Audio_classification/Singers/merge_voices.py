import pydub
import os


def merge_voices():
    path = "singer_voices/singer"
    two_files = []
    for fil in os.listdir(path):
        name = fil.split(".")[0]
        if len(name.split("_")) == 2:
            if name.split("_")[0] not in two_files:
                two_files.append(name.split("_")[0])
                result= 0
                for f in os.listdir(path):
                    if f.split(".")[0].split("_")[0] == name.split("_")[0] :
                        result += pydub.AudioSegment.from_file(f'singer_voices/singer/{f}')
                result.export(f"singer_voices/stick_data/{name.split('_')[0]}.wav", format='wav')
        else:
            result = pydub.AudioSegment.from_file(f'singer_voices/singer/{fil}')
            result.export(f"singer_voices/stick_data/{name}.wav", format='wav')

if __name__ == "__main__":
    merge_voices()

