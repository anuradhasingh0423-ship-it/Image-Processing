import cv2 as cv

cam = cv.VideoCapture(0)
while True:
    _, img = cam.read()
    img = cv.flip(img, 1)

    blur_1 = cv.blur(img, (2,2))
    blur_2 = cv.blur(img, (4,4))
    blur_3 = cv.blur(img, (8,8))
    blur_4 = cv.blur(img, (16,16))
    blur_5 = cv.blur(img, (32,32))


    cv.imshow("Frame", img)
    cv.imshow("Blur-1", blur_1)
    cv.imshow("Blur-2", blur_2)
    cv.imshow("Blur-3", blur_3)
    cv.imshow("Blur-4", blur_4)
    cv.imshow("Blur-5", blur_5)
    
    if cv.waitKey(10) == 27:  # ESC key to exit
        cam.release()
        break