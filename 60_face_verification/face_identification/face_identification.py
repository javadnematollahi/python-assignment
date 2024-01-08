import cv2
import matplotlib.pyplot as plt
from insightface.app import FaceAnalysis
import numpy as np
import argparse
from creat_face_bank import FaceBank


class FaceIdentification:
    def __init__(self, threshold=25) :
        self.app = FaceAnalysis(providers=['CPUExecutionProvider'], name='buffalo_s')
        self.app.prepare(ctx_id=0, det_size=(640, 640))
        self.threshold = threshold

    def face_identification(self, image_path, npy_face_bank_path, save_result=False):
        face_bank = np.load(npy_face_bank_path, allow_pickle=True)
        input_image = cv2.imread(image_path)
        image_g = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
        resultg = self.app.get(image_g)
        for result in resultg:
            cv2.rectangle(image_g,(int(result.bbox[0]), int(result.bbox[1])),(int(result.bbox[2]) , int(result.bbox[3])), color=(255, 0, 0) ,thickness=4)
            for person in face_bank:
                face_bank_person_embedding = person["embedding"]
                new_person_embedding = result["embedding"]
                distance = np.sqrt(np.sum((face_bank_person_embedding - new_person_embedding)**2))
                if distance < self.threshold:
                    image_g = cv2.putText(image_g, person["name"], (int(result.bbox[0])-5, int(result.bbox[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (20, 0, 255) ,1 )
                    break
            else:
                image_g = cv2.putText(image_g, "unknown", (int(result.bbox[0])-5, int(result.bbox[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (20, 0, 255) ,1 )
        plt.imshow(image_g)
        if save_result == True:
            plt.savefig("face_detected.jpg")
        plt.show()

parser = argparse.ArgumentParser()
parser.add_argument('--image', type=str,default="sample.jpg", help='Image path')
parser.add_argument('--update', action='store_true', help='Update face_bank')
parser.add_argument('--npyfile', default="face_bank.npy", help='Npy face_bank file path')
parser.add_argument('--facebank', default="face_bank", help='face_bank path')
parser.add_argument('--save', type=bool, default=False, help='Save the result')
opt = parser.parse_args()

if __name__ == "__main__":
    faceidentification = FaceIdentification()
    if opt.update:
        facebank = FaceBank()
        facebank.update_face_bank(opt.npyfile, opt.facebank)
    faceidentification.face_identification(opt.image, opt.npyfile, opt.save)