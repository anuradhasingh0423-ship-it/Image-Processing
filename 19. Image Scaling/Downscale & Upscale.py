import cv2 as cv


cam = cv.VideoCapture(0)

while True:
    
    _, img = cam.read()
    
    img = cv.flip(img,1)                
    
    resized_1 = cv.resize(img      , (int(img.shape[1]/4) ,int(img.shape[0]/4)))
    resized_2 = cv.resize(resized_1, (int(resized_1.shape[1]*4) ,int(resized_1.shape[0]*4)))
    
    
    cv.imshow("Original", img)
    cv.imshow("Resized-1", resized_1)
    cv.imshow("Upscaled", resized_2)
    
    if cv.waitKey(10) == 27:
        cam.release()
        break