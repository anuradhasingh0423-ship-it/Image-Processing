import cv2 as cv
import numpy as np
import os

cam = cv.VideoCapture(0)

# ✅ Proper logo loading
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

    # ---------------- LOGO SIZE ----------------
    logo_height = int(ht * 0.07)  # 7% height
    aspect_ratio = logo_original.shape[1] / logo_original.shape[0]
    logo_width = int(logo_height * aspect_ratio)

    logo = cv.resize(logo_original, (logo_width, logo_height))

    # ---------------- MARGINS ----------------
    margin_top = int(ht * 0.01)
    margin_bottom = int(ht * 0.01)
    margin_left = int(wt * 0.005)
    margin_right = int(wt * 0.005)

    # ---------------- TOP LEFT ----------------
    img[margin_top:margin_top + logo_height,
        margin_left:margin_left + logo_width] = logo

    # ---------------- TOP RIGHT ----------------
    img[margin_top:margin_top + logo_height,
        wt - logo_width - margin_right:wt - margin_right] = logo

    # ---------------- BOTTOM LEFT ----------------
    img[ht - logo_height - margin_bottom:ht - margin_bottom,
        margin_left:margin_left + logo_width] = logo

    # ---------------- BOTTOM RIGHT ----------------
    img[ht - logo_height - margin_bottom:ht - margin_bottom,
        wt - logo_width - margin_right:wt - margin_right] = logo

    cv.imshow("Frame", img)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()