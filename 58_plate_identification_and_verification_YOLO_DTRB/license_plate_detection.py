from ultralytics import YOLO
import cv2

detector_path = "weights/yolov8-detector/yolov8-detector.pt"
plate_detector = YOLO(detector_path)

results = plate_detector.predict("io/input-plate")
# print(results[0].path.split("\\")[-1])
for j,result in enumerate(results):
    image = cv2.imread(result.path)
    for i in range(len(result.boxes.xyxy)):
        if result.boxes.conf[i] > 0.7:
            bbox_tensor = result.boxes.xyxy[i]
            bbox_ndarray = bbox_tensor.cpu().detach().numpy().astype(int)
            x1, y1, x2, y2 = bbox_ndarray
            plate_image = image[y1:y2, x1:x2].copy()

            cv2.imwrite(f"io/output/plate_image_result_{j}{i}.jpg", plate_image)
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 4)

    cv2.imwrite(f"io/input/image_result_{j}.jpg", image)