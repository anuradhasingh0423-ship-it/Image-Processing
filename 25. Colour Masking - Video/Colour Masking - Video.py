import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
camera = cv.VideoCapture(0)

lower = np.array([0,0,0])
upper = np.array([60,60,60])

while True:
    
    _ , img = camera.read()
    img = cv.flip(img,1)    
    
    mask = cv.blur(img, (4,4))
    mask = cv.inRange(mask, lower, upper)
    
    cv.imshow("Frame" , img)
    cv.imshow("Mask"  , mask)
    
    if (cv.waitKey(1) == 27):
        camera.release()
        break
        
camera.release()    