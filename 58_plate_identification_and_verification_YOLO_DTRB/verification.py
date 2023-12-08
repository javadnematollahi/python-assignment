import argparse
import cv2
import os
import numpy as np
from ultralytics import YOLO
from dtrb.my_dtrb import DTRB
from database import Database
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

parser = argparse.ArgumentParser()
# parser.add_argument('--image_folder', required=True, help='path to image_folder which contains text images')
parser.add_argument('--workers', type=int, help='number of data loading workers', default=0)
parser.add_argument('--batch_size', type=int, default=192, help='input batch size')
# parser.add_argument('--saved_model', required=True, help="path to saved_model to evaluation")
""" Data processing """
parser.add_argument('--batch_max_length', type=int, default=25, help='maximum-label-length')
parser.add_argument('--imgH', type=int, default=32, help='the height of the input image')
parser.add_argument('--imgW', type=int, default=100, help='the width of the input image')
parser.add_argument('--rgb', action='store_true', help='use rgb input')
parser.add_argument('--character', type=str, default='0123456789abcdefghijklmnopqrstuvwxyz', help='character label')
parser.add_argument('--sensitive', action='store_true', help='for sensitive character mode')
parser.add_argument('--PAD', action='store_true', help='whether to keep ratio then pad for image resize')
""" Model Architecture """
parser.add_argument('--Transformation', type=str, default="TPS", help='Transformation stage. None|TPS')
parser.add_argument('--FeatureExtraction', type=str, default="ResNet", help='FeatureExtraction stage. VGG|RCNN|ResNet')
parser.add_argument('--SequenceModeling', type=str, default="BiLSTM", help='SequenceModeling stage. None|BiLSTM')
parser.add_argument('--Prediction', type=str, default="Attn", help='Prediction stage. CTC|Attn')
parser.add_argument('--num_fiducial', type=int, default=20, help='number of fiducial points of TPS-STN')
parser.add_argument('--input_channel', type=int, default=1, help='the number of input channel of Feature extractor')
parser.add_argument('--output_channel', type=int, default=512,
                    help='the number of output channel of Feature extractor')
parser.add_argument('--hidden_size', type=int, default=256, help='the size of the LSTM hidden state')
parser.add_argument("--detector-weights", type=str, default="weights/yolov8-detector/yolov8-detector.pt")
parser.add_argument("--recognizer-weights", type=str, default="weights/dtrb-recognizer/best_accuracy.pth")
parser.add_argument("--input-images", type=str, default="io/input-plate")
parser.add_argument("--threshold", type=float, default=0.7)
opt = parser.parse_args()


header_image = np.ones((100, 1000,3), dtype=np.uint8)*255
font = cv2.FONT_HERSHEY_SIMPLEX 
fontScale = 0.8
color = (255, 0, 0) 
thickness = 2
cv2.putText(header_image, 'image_path', (5, 50)  , font, fontScale, color, thickness, cv2.LINE_AA) 
cv2.putText(header_image, 'predicted_labels', (255, 50)  , font, fontScale, color, thickness, cv2.LINE_AA) 
cv2.putText(header_image, 'confidence_score', (505, 50)  , font, fontScale, color, thickness, cv2.LINE_AA) 
cv2.putText(header_image, 'Exist in Database', (755, 50)  , font, fontScale, color, thickness, cv2.LINE_AA) 
plate_detector = YOLO(opt.detector_weights)
plate_recognizer = DTRB(opt.recognizer_weights, opt)
plate_database = Database()

plate_database.add_default_plate()
plates = plate_database.get_plates()

results = plate_detector.predict(opt.input_images)

dashed_line = '-' * 120
head = f'{"image_path":25s}\t{"predicted_labels":25s}\t{"confidence_score":25s}\tExist in Database'
print(f'{dashed_line}\n{head}\n{dashed_line}')
# print(results[0].path.split("\\")[-1])
for j,result in enumerate(results):
    image = cv2.imread(result.path)
    for i in range(len(result.boxes.xyxy)):
        if result.boxes.conf[i] > 0.7:
            bbox_tensor = result.boxes.xyxy[i]
            bbox_ndarray = bbox_tensor.cpu().detach().numpy().astype(int)
            x1, y1, x2, y2 = bbox_ndarray
            plate_image = image[y1:y2, x1:x2].copy()
            plate_image = cv2.resize(plate_image, (100, 32))
            result_image = np.ones((100, 1000,3), dtype=np.uint8)*255
            for_show = cv2.resize(plate_image, (240, 90))
            result_image[5:for_show.shape[0]+5,5:for_show.shape[1]+5] = for_show
            plate_image = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)
            image_name = result.path.split('\\')[-1].split('.')[0]
            name, plate, confidence = plate_recognizer.predict(plate_image, opt, [f'{image_name}_{i}'])
            cv2.putText(result_image, f'{plate}', (255, 50) , font, fontScale, color, thickness, cv2.LINE_AA) 
            cv2.putText(result_image, f'{confidence:0.4f}', (505, 50)  , font, fontScale, color, thickness, cv2.LINE_AA) 
            for database_plate in plates:
                if similar(database_plate[2], plate) > 0.8:
                    print(f'{" " * 25}\t{True}')
                    exist_check = True
                    break
            else:
                print(f'{" " * 25}\t{False}')
                exist_check = False
            cv2.putText(result_image, f'{exist_check}', (755, 50)  , font, fontScale, color, thickness, cv2.LINE_AA) 
            cv2.imwrite(f"io/output/plate_{image_name}_{i}.jpg", plate_image)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 4)
            a = result_image.copy()
            header_image = np.vstack([header_image, a])


    cv2.imwrite(f"io/input/result_{image_name}.jpg", image)
cv2.imshow("Verification", header_image)
cv2.imwrite("io/output/Verification.jpg", header_image)
cv2.waitKey()