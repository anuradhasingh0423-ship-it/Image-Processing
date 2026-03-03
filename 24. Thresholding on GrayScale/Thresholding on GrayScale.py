import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
cam = cv.VideoCapture(0)

while True:
    
    _ , img = cam.read()
    
    img = cv.resize(img , (int(1280/2), int(720/2)))
    img = cv.flip(img,1)
    
    gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
    
    gray_thr_1 = gray.copy()
    gray_thr_1[gray_thr_1 > 200] = 30        # Black Background
    
    gray_thr_2 = gray.copy()
    gray_thr_2[gray_thr_2 > 200] = 100       # White Background
    
    
    cv.imshow('Original'  ,img)
    cv.imshow('Gray'      ,gray)
    cv.imshow('Gray_Thr1' ,gray_thr_1)
    cv.imshow('Gray_Thr2' ,gray_thr_2)
    
    if cv.waitKey(1) == 27:
        
        cam.release()
        break

