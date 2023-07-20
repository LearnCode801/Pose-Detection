import numpy
import cv2
import mediapipe as mp
import numpy as np

mpose=mp.solutions.pose
mpDraw=mp.solutions.drawing_utils
pose=mpose.Pose()

cap=cv2.VideoCapture(0)
# cap=cv2.VideoCapture('pose dectect.mp4')
s1=mpDraw.DrawingSpec(thickness=2,circle_radius=3,color=(0,0,255))
s2=mpDraw.DrawingSpec(thickness=2,circle_radius=3,color=(0,255,0))

while True:
    success,img=cap.read()
    img=cv2.resize(img,(600,500))

    result=pose.process(img)
    h, w, c = img.shape
    imgBlank = np.zeros([h, w, c])
    imgBlank.fill(255)

    mpDraw.draw_landmarks(imgBlank,result.pose_landmarks,mpose.POSE_CONNECTIONS,s1,s2)
    mpDraw.draw_landmarks(img, result.pose_landmarks, mpose.POSE_CONNECTIONS, s1, s2)

    cv2.imshow('pose-detection',img)
    cv2.imshow('blank convas', imgBlank)
    cv2.waitKey(1)


