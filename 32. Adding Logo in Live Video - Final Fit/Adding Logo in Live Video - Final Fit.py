import cv2 as cv
import numpy as np
import os

cam = cv.VideoCapture(0)

# -------- Load Logo Properly --------
current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "download.png")

logo_original = cv.imread(logo_path)

if logo_original is None:
    print("Logo not found!")
    exit()

while True:
    
    ret, img = cam.read()
    if not ret:
        break

    img = cv.flip(img, 1)

    ht, wt = img.shape[:2]

    # -------- Layout Percentages --------
    margin_top  = int(ht * 0.01)      # 1%
    margin_right = int(wt * 0.005)    # 0.5%

    logo_height = int(ht * 0.07)      # 7% of height
    logo_width  = int(wt * 0.04)      # 4% of width

    # Make square fit
    side = min(logo_height, logo_width)

    logo = cv.resize(logo_original, (side, side))

    # -------- Top Right Placement --------
    y_start = margin_top
    x_start = wt - side - margin_right

    img[y_start:y_start + side,
        x_start:x_start + side] = logo

    cv.imshow('Frame', img)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()