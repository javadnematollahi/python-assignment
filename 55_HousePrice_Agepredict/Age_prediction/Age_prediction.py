import cv2
from face_alignment import align_face
from landmarks_detector import LandmarksDetector

landmarks_detector = LandmarksDetector('assets/shape_predictor_68_face_landmarks.dat')
loaded_model = tf.keras.models.load_model('assets/Age_prediction.h5')

def predict(image_path):
  all_face_landmarks = landmarks_detector.get_landmarks(image_path)
  for i, face_landmarks in enumerate(all_face_landmarks):
    image = align_face(image_path, face_landmarks)
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  image_edit = cv2.resize(image, (128, 128))
  image_data=image_edit.reshape(1,128,128,3)
  image_data = image_data / 255.0
  preds = loaded_model.predict(image_data)
  return preds,image

age,image = predict('input/javad.jpg')
age_pred=round(age[0][0], 2)
plt.title("Your age is about\n {:.2f}".format(age[0][0]),fontsize = 30)
plt.imshow(image)