import cv2 as cv
import numpy as np

blue = [247,206,139]

cam = cv.VideoCapture(0)

while True:
    ret, img = cam.read()
    if not ret:
        break

    img = cv.flip(img, 1)

    # 🔹 Create background same size as image
    background = np.full(img.shape, blue, dtype=np.uint8)

    # 🔹 Merge
    merged = cv.addWeighted(img, 0.85, background, 0.15, 0)

    cv.imshow("Original", img)
    cv.imshow("Merged", merged)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()