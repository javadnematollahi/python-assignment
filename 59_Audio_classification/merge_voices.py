import pydub
import os


def merge_voices():
    path = "raw_data"
    two_files = []
    for file in os.listdir(path):
        name = file.split(".")[0]
        if len(name.split("_")) == 2:
            if name.split("_")[0] not in two_files:
                two_files.append(name.split("_")[0])
                result= 0
                for f in os.listdir(path):
                    if f.split(".")[0].split("_")[0] == name.split("_")[0] :
                        result += pydub.AudioSegment.from_file(f'raw_data/{f}')
                result.export(f"data/{name.split('_')[0]}.ogg")
        else:
            result = pydub.AudioSegment.from_file(f'raw_data/{file}')
            result.export(f"data/{name}.ogg")

