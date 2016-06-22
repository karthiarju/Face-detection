from skimage import io
import processing as p
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
from sklearn.metrics import accuracy_score
import numpy as np
import os

test_path = '/home/qburst/Desktop/Emotiondetectiontest/Testingset'

def accuracy_perc(classifier, test_set_features, test_set_labels):

    test_set_predict_labels = classifier.predict(test_set_features)
    return accuracy_score(test_set_labels, test_set_predict_labels) * 100



x = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
y = []

#Convert to numpy array
y = np.asarray(y, dtype = np.int32)
x = np.asarray(x)

count = 0


#Extracting features
for emotion_folder in os.listdir(test_path):
    print emotion_folder
    for img_file in os.listdir(test_path + '/' + emotion_folder):
        count += 1
        print count, img_file
        img = io.imread(test_path + '/' + emotion_folder + '/' + img_file)

        face_count, feature, faces = p.feature_extraction(img)
        x = np.vstack((x, feature[0]))

        #Assigning code to each emotion
        if emotion_folder == 'sad':
            y = np.append(y, 0)
        elif emotion_folder == 'surprise':
            y = np.append(y, 1)
        elif emotion_folder == 'happy':
            y = np.append(y, 2)
	elif emotion_folder == 'angry':
	    y = np.append(y, 3)

x = np.delete(x, 0, 0)

gnb = joblib.load('/home/qburst/Desktop/Emotiondetectiontest/EmotionClassification/Classifiers/gnb.pk1')
svc = joblib.load('/home/qburst/Desktop/Emotiondetectiontest/EmotionClassification/Classifiers/svc.pk1')
linear_svc = joblib.load('/home/qburst/Desktop/Emotiondetectiontest/EmotionClassification/Classifiers/linear_svc.pk1')

print accuracy_perc(gnb, x, y)
print accuracy_perc(svc, x, y)
print accuracy_perc(linear_svc, x, y)
