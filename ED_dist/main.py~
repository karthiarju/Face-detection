from skimage import io
import processing as p
from sklearn.externals import joblib
import cv2

def detect(path):

	input_image = io.imread(path)
	gnb = joblib.load('/home/qburst/Desktop/Emotion_detection/ED_dist/Classifier/gnb.pkl')
	face_count, features, faces = p.feature_extraction(input_image)
	if face_count:
		emotions = gnb.predict(features)
		print emotions
		for d, emotion in zip(faces, emotions):
			print d, emotion
			if emotion == 0:
				cv2.rectangle(input_image, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 0), 2)

			elif emotion == 1:
                                cv2.rectangle(input_image, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 3)


			elif emotion == 2:
                                cv2.rectangle(input_image, (d.left(), d.top()), (d.right(), d.bottom()), (255, 255, 0), 3)


			elif emotion == 3:
				cv2.rectangle(input_image, (d.left(), d.top()), (d.right(), d.bottom()), (255, 0, 0), 3)

				
		io.imsave('Detected/emotion.jpg', input_image)
		return face_count, 'Detected/emotion.jpg'
	else:
	 	return face_count, 'err'
		
		
		
	


