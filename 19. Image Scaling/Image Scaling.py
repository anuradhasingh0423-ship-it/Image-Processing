import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    _, img = cam.read()
    img = cv.flip(img, 1)

    resized_1 = cv.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
    resized_2 = cv.resize(img, (int(img.shape[1]/4), int(img.shape[0]/4)))

    cv.imshow("original", img)
    cv.imshow("resized-1", resized_1)
    cv.imshow("resized-2", resized_2)
    if cv.waitKey(10) == 27:  # ESC key to exit
        cam.release()
        break