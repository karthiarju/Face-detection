from skimage import io
import processing as p
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
import numpy as np


input_image_path = '/home/qburst/Desktop/2 emotions test.jpg'

input_image = io.imread(input_image_path)

##x = np.load('/home/qburst/Desktop/Emotion classification with angle/Np arrays/dist_angle_x.npy')
##y = np.load('/home/qburst/Desktop/Emotion classification with angle/Np arrays/dist_angle_y.npy')
##
####initializing a NB classifier
##gnb = GaussianNB()
##gnb.fit(x, y)
##
##joblib.dump(gnb, '/home/qburst/Desktop/Emotion classification with angle/TrainedGNB.pkl')

gnb = joblib.load('/home/qburst/Desktop/Emotion classification with angle/TrainedGNB.pkl')

face_count, features, faces = p.feature_extraction(input_image)

emotions = gnb.predict(features)
print emotions

##for count, face in enumerate(faces):
##     gnb.predict(features[0])


