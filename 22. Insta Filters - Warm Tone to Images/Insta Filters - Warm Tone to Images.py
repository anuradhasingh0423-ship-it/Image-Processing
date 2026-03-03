import cv2 as cv
import numpy as np


# Adding tone
def add_tone(img_path, color, a, b):

    img = cv.imread(img_path)

    if img is None:
        print("Image not found at:", img_path)
        return

    rows, cols = img.shape[:2]

    background = np.full((rows, cols, 3), color, dtype=np.uint8)

    final = cv.addWeighted(img, a, background, b, 0)

    #  Resize both images (50% smaller)
    small_original = cv.resize(img, (0, 0), fx=0.5, fy=0.5)
    small_final = cv.resize(final, (0, 0), fx=0.5, fy=0.5)

    cv.imshow('Original', small_original)
    cv.imshow('Processed', small_final)

    cv.waitKey(0)
    cv.destroyAllWindows()



import os

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "img_1.jpg")

add_tone(image_path, [80,20,200], .5, .5)
add_tone(image_path, [200,20,80], .5, .5)