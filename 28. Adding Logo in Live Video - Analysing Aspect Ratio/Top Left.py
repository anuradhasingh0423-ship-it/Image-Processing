# Height (1% = Margin | 7% = Logo | 92% = Vacant) 720

# Width (.5% = Margin | 4% = Logo | 95.5% = Vacant) 1280


import cv2 as cv
import numpy as np
import os

cam = cv.VideoCapture(0)

# ✅ Proper logo path
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
    margin_top  = int(ht * 0.01)     # 1%
    margin_left = int(wt * 0.005)    # 0.5%

    logo_height = int(ht * 0.07)     # 7% of height

    # Maintain aspect ratio
    aspect_ratio = logo_original.shape[1] / logo_original.shape[0]
    logo_width = int(logo_height * aspect_ratio)

    logo = cv.resize(logo_original, (logo_width, logo_height))

    # Place logo (Top Left)
    img[margin_top:margin_top + logo_height,
        margin_left:margin_left + logo_width] = logo

    cv.imshow("Frame", img)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()