import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    _, img = cam.read()
    img = cv.flip(img, 1)
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    r = img[:,:,0]
    g = img[:,:,1]
    b = img[:,:,2]

    h = hsv[:,:,0]
    s = hsv[:,:,1]
    v = hsv[:,:,2]

    cv.imshow("Frame", img)
    cv.imshow("Red", r)
    cv.imshow("Green", g)
    cv.imshow("Blue", b)

    cv.imshow("HSV", hsv)
    cv.imshow("Hue",h)
    cv.imshow("Saturation", s)
    cv.imshow("Value",v)

    key = cv.waitKey(20)

    if (key == 27):
        cam.release()
        break