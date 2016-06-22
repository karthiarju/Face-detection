from skimage import io
import processing as p
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
import numpy as np


input_image_path = '/home/qburst/Desktop/Test images/testsaveopencvimg without resize.jpg'

input_image = io.imread(input_image_path)

##x = np.load('/home/qburst/Desktop/Emotion Classification/Numpy arrays with only distances/dist_only_x.npy')
##y = np.load('/home/qburst/Desktop/Emotion Classification/Numpy arrays with only distances/y.npy')

###initializing a NB classifier
##gnb = GaussianNB()
##gnb.fit(x, y)

##joblib.dump(gnb, '/home/qburst/Desktop/TrainedGNB.pkl')

gnb = joblib.load('/home/qburst/Desktop/TrainedGNB.pkl')

face_count, features, faces = p.feature_extraction(input_image)

emotions = gnb.predict(features)
print emotions

##for count, face in enumerate(faces):
##     gnb.predict(features[0])


