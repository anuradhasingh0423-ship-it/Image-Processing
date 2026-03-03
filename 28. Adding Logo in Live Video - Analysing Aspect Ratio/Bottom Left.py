import cv2 as cv
import numpy as np
import os

cam = cv.VideoCapture(0)

# Proper logo path
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

    # Percentages
    logo_height = int(ht * 0.07)        # 7%
    margin_bottom = int(ht * 0.01)      # 1%
    margin_left = int(wt * 0.005)       # 0.5%

    # Maintain aspect ratio
    aspect_ratio = logo_original.shape[1] / logo_original.shape[0]
    logo_width = int(logo_height * aspect_ratio)

    logo = cv.resize(logo_original, (logo_width, logo_height))

    # Bottom-left coordinates
    y_start = ht - logo_height - margin_bottom
    x_start = margin_left

    img[y_start:y_start + logo_height,
        x_start:x_start + logo_width] = logo

    cv.imshow("Frame", img)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()