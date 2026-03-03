import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

while True:
    ret, img = cam.read()
    if not ret:
        break

    img = cv.flip(img, 1)

    # Warm color (BGR format!)
    yellow = [108, 222, 249]

    # Create background SAME SIZE as frame
    background = np.full(img.shape, yellow, dtype=np.uint8)

    # Merge
    merged = cv.addWeighted(img, 0.90, background, 0.10, 0)

    cv.imshow("Original", img)
    cv.imshow("Warm Filter", merged)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()