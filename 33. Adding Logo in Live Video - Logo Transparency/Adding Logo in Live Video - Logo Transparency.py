import cv2 as cv
import numpy as np
import os

cam = cv.VideoCapture(0)

# -------- Load Logo Once --------
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

    logo_height = int(ht * 0.07)      # 7%
    logo_width  = int(wt * 0.04)      # 4%

    side = min(logo_height, logo_width)

    # Resize logo
    logo = cv.resize(logo_original, (side, side))

    # Top-right position
    y_start = margin_top
    x_start = wt - side - margin_right

    # Extract background ROI
    bg = img[y_start:y_start + side,
             x_start:x_start + side].copy()

    # Transparency blending
    final_logo = cv.addWeighted(bg, 0.3, logo, 0.7, 0)

    # Put blended result back
    img[y_start:y_start + side,
        x_start:x_start + side] = final_logo

    cv.imshow('Frame', img)
    cv.imshow('BG', bg)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()