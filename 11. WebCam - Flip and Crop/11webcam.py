# Crop and Flip
import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    ret, img = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    img = cv.flip(img, 1)

    # Make sure crop area is inside 640x480
    frame = img[100:400, 200:500]

    cv.imshow('Frame', img)
    cv.imshow('Cropped', frame)

    key = cv.waitKey(20)  # Capital K

    if key == 27:  # ESC
        break

cam.release()
cv.destroyAllWindows()