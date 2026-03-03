import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)

while True:
    ret, img = cam.read()
    if not ret:
        break

    img = cv.flip(img, 1)

    # BGR colors
    yellow = [108, 222, 249]
    blue   = [247, 206, 139]

    # Create background SAME SIZE as frame
    yellow_background = np.full(img.shape, yellow, dtype=np.uint8)
    blue_background   = np.full(img.shape, blue, dtype=np.uint8)

    print("Image:", img.shape)
    print("Yellow:", yellow_background.shape)

    merged_yellow = cv.addWeighted(img, 0.9, yellow_background, 0.1, 0)
    merged_blue   = cv.addWeighted(img, 0.9, blue_background, 0.1, 0)

    cv.imshow("Original", img)
    cv.imshow("Warm Filter", merged_yellow)
    cv.imshow("Cool Filter", merged_blue)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()