import cv2 as cv
import numpy as np

# Load cascade properly
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

        face = img[y:y+h, x:x+w]

        # Better blur
        blurred_face = cv.GaussianBlur(face, (51, 51), 0)

        img[y:y+h, x:x+w] = blurred_face

        face_crop = blurred_face

    cv.imshow('Frame', img)

    if face_crop is not None:
        cv.imshow('Face', face_crop)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()