import os
import numpy as np
from skimage import io
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn.externals import joblib
import processing as p

train_path = '/home/qburst/Desktop/Emotiondetectiontest/Trainingset'

x = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
y = []

#Convert to numpy array
y = np.asarray(y, dtype = np.int32)
x = np.asarray(x)

count = 0


#Extracting features
for emotion_folder in os.listdir(train_path):
    print emotion_folder
    for img_file in os.listdir(train_path + '/' + emotion_folder):
        count += 1
        print count, img_file
        img = io.imread(train_path + '/' + emotion_folder + '/' + img_file)

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
            
        

#Deleting the 1st element in x array
x = np.delete(x, 0, 0)

np.save('/home/qburst/Desktop/Emotiondetectiontest/EmotionClassification/Testnumpyarrays/Test_x_dist', x)
np.save('/home/qburst/Desktop/Emotiondetectiontest/EmotionClassification/Testnumpyarrays/Test_y_dist', y)

gnb = GaussianNB()
gnb.fit(x, y)
joblib.dump(gnb, '/home/qburst/Desktop/Emotiondetectiontest/EmotionClassification/Classifiers/gnb.pk1')
svc = svm.SVC(kernel='linear', C = 1.0)
svc.fit(x, y)
joblib.dump(gnb, '/home/qburst/Desktop/Emotiondetectiontest/EmotionClassification/Classifiers/svc.pk1')

linear_svc = svm.LinearSVC(penalty = 'l2', dual =True)
linear_svc.fit(x, y)
joblib.dump(gnb, '/home/qburst/Desktop/Emotiondetectiontest/EmotionClassification/Classifiers/linear_svc.pk1')
