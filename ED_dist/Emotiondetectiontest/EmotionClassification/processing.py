import dlib
import numpy as np
import dlib
import math
import cv2


#Function to change shape into an np array
def _shape_to_np(shape):
    xy = []
    for i in range(68):
        xy.append((shape.part(i).x, shape.part(i).y,))
    xy = np.asarray(xy, dtype='float32')
    return xy

#Function to calculate distances between two points
def find_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

#Function that returns distances
def distance(points):

    distances = []
    
    mouth_left_point = points[48]
    mouth_right_point = points[54]
    upper_lip_point = points[51]
    lower_lip_point = points[57]
    upper_lip_point_2 = points[62]
    lower_lip_point_2 = points[66]
    left_eye_top = points[37]
    left_eye_bottom = points[41]
    left_eye_left = points[36]
    left_eye_right = points[39]
    right_eye_top = points[44]
    right_eye_bottom = points[46]
    right_eye_left = points[42]
    right_eye_right = points[45]
    left_eye_brow_left = points[17]
    left_eye_brow_right = points[21]
    right_eye_brow_left = points[22]
    right_eye_brow_right = points[26]
    nose_top = points[27]
    nose_bottom = points[33]
        
    mouth_distance =  find_distance(mouth_left_point, mouth_right_point)
    upperlip_distance =  find_distance(upper_lip_point, lower_lip_point)
    lowerlip_distance =  find_distance(upper_lip_point_2, lower_lip_point_2)
    left_eye_distance =  find_distance(left_eye_top, left_eye_bottom)
    right_eye_distance =  find_distance(right_eye_top, right_eye_bottom)
    left_eyebrow_distance =  find_distance(left_eye_brow_left, left_eye_brow_right)
    right_eyebrow_distance =  find_distance(right_eye_brow_left, right_eye_brow_right)
    left_eye_eyebrow_left_distance = find_distance(left_eye_left, left_eye_brow_left)
    left_eye_eyebrow_right_distance = find_distance(left_eye_right, left_eye_brow_right)
    right_eye_eyebrow_left_distance = find_distance(right_eye_left, right_eye_brow_left)
    right_eye_eyebrow_right_distance = find_distance(right_eye_right, right_eye_brow_right)
    mouth_left_eye_left_distance = find_distance(mouth_left_point, left_eye_left)
    mouth_right_eye_right_distance = find_distance(mouth_right_point, right_eye_right)
    nose_distance = find_distance(nose_top, nose_bottom)
    

    distances.extend([mouth_distance, upperlip_distance, lowerlip_distance, left_eye_distance, right_eye_distance, left_eyebrow_distance, right_eyebrow_distance, left_eye_eyebrow_left_distance, left_eye_eyebrow_right_distance, right_eye_eyebrow_left_distance, right_eye_eyebrow_right_distance, mouth_left_eye_left_distance, mouth_right_eye_right_distance, nose_distance])
 
    add_value = reduce(lambda x, y : x + y, distances)
    distances = map(lambda x : x / add_value, distances)
    return distances

#Function that reads the image and returns the distances to another module

def feature_extraction(img):
    dist = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    dist = np.asarray(dist)

    #Loading the facial land mark pointer predictor
    predictor_path = '/home/qburst/Desktop/fd/shape_predictor_68_face_landmarks.dat'

    #Creating objects for frontal face detector and landmark point predictor
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(predictor_path)


    #'dets' has all the faces detected represented as rectangles, their co-ordinates are obtainable by using left(), top(),
    #right(), bottom(). 'dets' is iterable
    
    dets = detector(img, 1)
    
    for rect in dets:
    
        #'shape' has the 68 facial land mark points. Each of which can be accessed using shape.part().co-ordinate
        #eg: shape.part(1).x, shape.part(1).y for (x, y) of point 1. 'shape' is not iterable.
        shape = predictor(img, rect)
        points = _shape_to_np(shape)
        dist_as_np = np.asarray(distance(points))
        dist = np.vstack((dist, dist_as_np))

    dist = np.delete(dist, 0, 0)
    return len(dets), dist, dets        
        
        
