# import cv2 as cv

# cam = cv.VideoCapture(0)

# while True:

#     _, img = cam.read()
    
#     img = cv.flip(img, 1) 
   
#     img = cv.rectangle(img,(300,100),(800,600), (255,0,0),3)
#     img = cv.rectangle(img,(395,95) ,(805,605), (0,255,0),3)
#     img = cv.rectangle(img,(390,90) ,(810,610), (0,0,255),3)

#     cv.imshow("Frame",img)
    
#     key = cv.waitKey(10)
    
#     if (key == 27):                                       
#         cam.release()
#         break



import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    ret, img = cam.read()

    if not ret:
        break

    img = cv.flip(img, 1)

    # Safe rectangle positions inside 640x480
    img = cv.rectangle(img,(200,100),(500,400),(255,0,0),3)
    img = cv.rectangle(img,(210,110),(490,390),(0,255,0),3)
    img = cv.rectangle(img,(220,120),(480,380),(0,0,255),3)

    cv.imshow("Frame", img)

    key = cv.waitKey(10)

    if key == 27:
        break

cam.release()
cv.destroyAllWindows()