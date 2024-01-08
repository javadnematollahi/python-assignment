import os
import cv2
import matplotlib.pyplot as plt
from insightface.app import FaceAnalysis
import numpy as np

class FaceBank:
    def __init__(self) -> None:
        self.app = FaceAnalysis(providers=['CPUExecutionProvider'], name='buffalo_s')
        self.app.prepare(ctx_id=0, det_size=(640, 640))

    def creat_face_bank(self, face_bank_path, update=False):
        face_bank = []
        person_counter = 0
        for person_name in os.listdir(face_bank_path):
            file_path = os.path.join(face_bank_path, person_name)
            if os.path.isdir(file_path):
                person_counter += 1
                for image_name in os.listdir(file_path):
                    image_name = image_name.lower()
                    # print(image_name)
                    if image_name.endswith(".jpg") or image_name.endswith(".png") or image_name.endswith(".jpeg"):
                        image_path = os.path.join(file_path, image_name)
                        image_1 = cv2.imread(image_path)
                        image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2RGB)
                        result = self.app.get(image_1)
                        if len(result) > 1:
                            print("warning: more than one face detected in image")
                            continue
                        if len(result)==1:
                            embedding = result[0]['embedding']
                            my_dict = {'name': person_name, "embedding": embedding}
                            face_bank.append(my_dict)
        if update == False:
            print(f"Face bank created and {person_counter} different person added to it.")
            np.save("face_bank.npy", face_bank)
        else:
            return face_bank

    def update_face_bank(self, last_npy_facebank_path, new_facebank_path):
        facebank = np.load(last_npy_facebank_path , allow_pickle=True)
        newfacebank = self.creat_face_bank(new_facebank_path, update=True)
        for new in newfacebank:
            for face in facebank:
                if np.array_equal(face['embedding'], new['embedding']):
                    break
            else:
                facebank = np.append(facebank,np.array([{'name': new['name'], "embedding": new['embedding']}]))
        np.save(last_npy_facebank_path, facebank)
        print(len(facebank))
        for i in facebank:
            print(i['name'])

if __name__ == "__main__":
    create = FaceBank()
    create.creat_face_bank("face_bank")


