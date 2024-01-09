import os
import cv2
import matplotlib.pyplot as plt
from insightface.app import FaceAnalysis
import numpy as np
import time

class AddUser:
    def __init__(self):
        self.app = FaceAnalysis(providers=['CPUExecutionProvider'], name='buffalo_s')
        self.app.prepare(ctx_id=0, det_size=(640, 640))
        self.url='http://192.168.229.162:8080/video'

    def creat_face_bank(self, update=False):
        face_bank = []
        recognize = 0 
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
            face_ok = False
            start = time.time()
            while True:
                ok,frame = video.read()

                if not ok:
                    break
                result = self.app.get(frame)
                if len(result) > 1:
                    print("warning: more than one face detected in image")
                    continue
                if len(result)==1:
                    face_ok = True
                    embedding = result[0]['embedding']
                    my_dict = {"embedding": embedding}
                    face_bank.append(my_dict)
                    break
                finish = time.time()
                if finish - start>30:
                    recognize = 1
                    break
            if update == False and face_ok == True:
                print(f"Your face is set as Login Face.")
                np.save("face_bank.npy", face_bank)
            elif recognize == 1:
                print(f"Next time put your face in front of camera. ")
                return False
            else:
                return face_bank
        else:
            return True

    def update_face_bank(self, last_npy_facebank_path):
        facebank = np.load(last_npy_facebank_path , allow_pickle=True)
        newfacebank = self.creat_face_bank(update=True)
        if isinstance(newfacebank, list):
            facebank = np.append(facebank,np.array([{"embedding": newfacebank[0]['embedding']}]))
            np.save(last_npy_facebank_path, facebank)
            print(len(facebank))
            print("Your face is added to login users.")
        elif newfacebank == True:
            print("No camera detected")
        elif newfacebank == False:
            print("There is no face in the camera.")

if __name__ == "__main__":
    create = AddUser()
    create.creat_face_bank()


