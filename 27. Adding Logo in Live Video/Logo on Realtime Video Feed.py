import cv2 as cv
import numpy as np
import os

cam = cv.VideoCapture(0)

#  Proper logo path
current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "download.png")

logo = cv.imread(logo_path)

if logo is None:
    print("Logo not found!")
    exit()

logo = cv.resize(logo, (80, 80))

while True:
    
    ret, img = cam.read()
    if not ret:
        break

    img = cv.flip(img, 1)

    h_logo, w_logo = logo.shape[:2]
    h_frame, w_frame = img.shape[:2]

    # ✅ Top-right position automatically
    x_start = w_frame - w_logo - 10
    y_start = 10

    img[y_start:y_start+h_logo, x_start:x_start+w_logo] = logo

    cv.imshow('Frame', img)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()