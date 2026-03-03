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

    face_crop = None

    if len(faces) > 0:

        # Select largest face based on area
        largest_face = max(faces, key=lambda f: f[2] * f[3])
        x, y, w, h = largest_face

        cv.rectangle(img, (x, y), (x+w, y+h), (0, 180, 0), 2)

        face_crop = img[y:y+h, x:x+w]
        face_crop = cv.resize(face_crop, (256, 256))

    cv.imshow('Frame', img)

    if face_crop is not None:
        cv.imshow('Face', face_crop)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()