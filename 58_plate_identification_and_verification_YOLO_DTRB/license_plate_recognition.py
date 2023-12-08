import argparse
import cv2
import os
from ultralytics import YOLO
from dtrb.my_dtrb import DTRB


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
parser.add_argument("--input-images", type=str, default="io/output")
parser.add_argument("--threshold", type=float, default=0.7)
opt = parser.parse_args()

plate_recognizer = DTRB(opt.recognizer_weights, opt)

path = opt.input_images
dashed_line = '-' * 80
head = f'{"image_path":25s}\t{"predicted_labels":25s}\tconfidence score'
print(f'{dashed_line}\n{head}\n{dashed_line}')
for f in os.listdir(path):
    if f.startswith("plate"):
        new_path = os.path.join(path, f)
        plate_image = cv2.imread(new_path)
        plate_image = cv2.resize(plate_image, (100, 32))
        plate_image = cv2.cvtColor(plate_image, cv2.COLOR_BGR2GRAY)
        plate_recognizer.predict(plate_image, opt, [f])