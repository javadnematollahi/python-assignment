from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model.train(data="398_data_pelak.yaml")
best_model = YOLO("weights/best.pt")

result = best_model("assets/398_pelak_images/test/images/photo_2023-11-07_14-34-47_jpg.rf.bcd55d35872394242ddd40645d7294cb.jpg", save=True)