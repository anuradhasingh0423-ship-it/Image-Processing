import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    ret, img = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    cv.imshow('Frame', img)

    key = cv.waitKey(1)

    if key == 27:  # ESC key
        break

cam.release()
cv.destroyAllWindows()