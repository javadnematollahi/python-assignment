import cv2
import pyfiglet
from insightface.app import FaceAnalysis
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--image1", type=str, help="image1 path")
parser.add_argument("--image2", type=str, help="image2 path")
args = parser.parse_args()

image1_path = args.image1
image2_path = args.image2

app = FaceAnalysis(providers=['CPUExecutionProvider'], name='buffalo_s')
app.prepare(ctx_id=0, det_size=(640, 640))

image_1 = cv2.imread(image1_path)
image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2RGB)

result = app.get(image_1)
embed1 = result[0]["embedding"]

image_2 = cv2.imread(image2_path)
image_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2RGB)

result2 = app.get(image_2)
embed2 = result2[0]["embedding"]

if np.sqrt(np.sum((embed1 - embed2)**2))<25:
    f = pyfiglet.figlet_format("Same Persons", font="slant")
    print(f)
else:
    f = pyfiglet.figlet_format("Different Persons", font="slant")
    print(f)
