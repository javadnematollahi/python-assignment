import cv2
import matplotlib.pyplot as plt
from insightface.app import FaceAnalysis
import numpy as np
import argparse
from smart_camera.creat_face_bank import AddUser


class FaceIdentification:
    def __init__(self, threshold=25) :
        self.app = FaceAnalysis(providers=['CPUExecutionProvider'], name='buffalo_s')
        self.app.prepare(ctx_id=0, det_size=(640, 640))
        self.threshold = threshold
        self.url='http://192.168.229.162:8080/video'

    def face_identification(self, npy_face_bank_path):
        face_bank = np.load(npy_face_bank_path, allow_pickle=True)
        print("len", len(face_bank))
        access = False
        no_camera = False
        try:
            video = cv2.VideoCapture(0)
        except:
            print("except")
        try:
            video = cv2.VideoCapture(self.url)
        except:
            no_camera = True
        if no_camera == False:
            _,frame = video.read()

            video.set(3,1280)
            video.set(4,960)
            while True:
                ok,frame = video.read()

                if not ok:
                    break
                image_g = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                resultg = self.app.get(image_g)
                for result in resultg:
                    for person in face_bank:
                        face_bank_person_embedding = person["embedding"]
                        new_person_embedding = result["embedding"]
                        distance = np.sqrt(np.sum((face_bank_person_embedding - new_person_embedding)**2))
                        if distance < self.threshold:
                            access = True
                            print("you can access to App")
                            break
                    else:
                        access = False
                        print("Your can't access to App")
                if len(resultg)>0:
                    break
            return access
        else:
            return "No Camera"



parser = argparse.ArgumentParser()
parser.add_argument('--update', action='store_true', help='Update face_bank')
parser.add_argument('--npyfile', default="face_bank.npy", help='Npy face_bank file path')
opt = parser.parse_args()

if __name__ == "__main__":
    faceidentification = FaceIdentification()
    if opt.update:
        facebank = AddUser()
        facebank.update_face_bank(opt.npyfile)
    faceidentification.face_identification( opt.npyfile)