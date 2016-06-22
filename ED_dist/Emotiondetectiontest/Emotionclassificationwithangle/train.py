import os
import numpy as np
from skimage import io
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
import processing as p

train_path = '/home/qburst/Desktop/Training emotions'



#Initialising x and y as data and target value respectively for classifier(NB, SVM)
x = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
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
            
        

#Deleting the 1st element in x array
x = np.delete(x, 0, 0)

np.save('/home/qburst/Desktop/dist_angle_x', x)
np.save('/home/qburst/Desktop/dist_angle_y', y)


            

