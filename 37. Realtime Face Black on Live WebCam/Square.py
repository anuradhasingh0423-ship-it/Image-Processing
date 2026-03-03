import cv2 as cv
import numpy as np

classifier = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cam = cv.VideoCapture(0)

while True:

    ret, img = cam.read()
    if not ret:
        break

    img = cv.flip(img, 1)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = classifier.detectMultiScale(gray, 1.1, 5)

    if len(faces) > 0:

        # Select largest face
        largest = max(faces, key=lambda f: f[2] * f[3])
        x, y, w, h = largest

        # Black square
        img[y:y+h, x:x+w] = np.zeros((h, w, 3), dtype=np.uint8)

    cv.imshow("Frame", img)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()