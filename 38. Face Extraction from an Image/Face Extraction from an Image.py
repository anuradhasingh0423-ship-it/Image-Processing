import os
import cv2 as cv
import numpy as np

# Get correct directory
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "group.png")

img = cv.imread(image_path)

if img is None:
    print("Image not found!")
    exit()

classifier = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = classifier.detectMultiScale(gray, 1.1, 5)

os.makedirs('People', exist_ok=True)

def save(frame, folder_name): 
    name_img = len(os.listdir(folder_name)) + 1
    name_img = folder_name + "/IMG_" + str(name_img) + '.png'
    cv.imwrite(name_img, frame)
    print(name_img, 'is exported')

for (x, y, w, h) in faces:

    face = img[y:y+h, x:x+w]
    cv.imshow('Face', face)

    key = cv.waitKey(0)

    if key == 13:
        save(face, 'People')

    elif key == 127:
        print("Skipped")

cv.destroyAllWindows()