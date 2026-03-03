import cv2 as cv
import numpy as np
import os

cam = cv.VideoCapture(0)

# Proper logo loading (only once!)
current_dir = os.path.dirname(os.path.abspath(__file__))
logo_path = os.path.join(current_dir, "download.png")

logo_original = cv.imread(logo_path)

if logo_original is None:
    print("Logo not found!")
    exit()

r = 1280  # initial crop width

while True:
    
    ret, img = cam.read()
    if not ret:
        break

    img = cv.flip(img, 1)

    ht, wt = img.shape[:2]

    # Clamp r safely
    r = max(200, min(r, wt))
    img = img[:, :r]

    ht, wt = img.shape[:2]

    # ---- Logo size ----
    logo_height = int(ht * 0.07)
    aspect_ratio = logo_original.shape[1] / logo_original.shape[0]
    logo_width = int(logo_height * aspect_ratio)

    logo = cv.resize(logo_original, (logo_width, logo_height))

    margin_top = int(ht * 0.01)
    margin_right = int(wt * 0.005)

    # Top-right placement
    img[margin_top:margin_top + logo_height,
        wt - logo_width - margin_right:wt - margin_right] = logo

    cv.imshow('Frame', img)

    key = cv.waitKey(1)

    if key == ord('s'):      # shrink width
        r -= 20

    elif key == ord('w'):    # expand width
        r += 20

    elif key == 27:          # ESC
        break

cam.release()
cv.destroyAllWindows()