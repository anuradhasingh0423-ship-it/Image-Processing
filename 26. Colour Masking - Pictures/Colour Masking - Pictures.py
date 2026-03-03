import cv2 as cv
import numpy as np
import os

# Define color range
lower = np.array([200, 200, 200])
upper = np.array([255, 255, 255])

# Get correct path
current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "img_1.jpg")

img = cv.imread(image_path)

if img is None:
    print("Image not found!")
    exit()

# Blur image
blurred = cv.blur(img, (8, 8))

# Create mask
mask = cv.inRange(blurred, lower, upper)

cv.imshow("Original", img)
cv.imshow("Mask", mask)

cv.waitKey(0)
cv.destroyAllWindows()