import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    _,img = cam.read()
    img = cv.flip(img, 1)

    gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

    cv.imshow("Frame", img)

    key = cv.waitKey(20)
    if (key == 13):
        cv.imwrite('Selfie.png', img)
        cv.imwrite('Selfie_Gray.png', gray)
        cv.imwrite('Selfie_HSV.png', hsv)
        cam.release()
        break

    cv.waitKey(0)