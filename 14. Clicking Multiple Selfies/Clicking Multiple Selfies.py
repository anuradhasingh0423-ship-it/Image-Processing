# import cv2 as cv

# cam = cv.VideoCapture(0)
# c  = 0
# while True:
#     _, img = cam.read()
#     img = cv.flip(img, 1)
#     cv.imshow("Frame", img)
#     key = cv.waitKey(20)
#     if (key == 13):               # Click selfie if Enter is pressed
#         cv.imwrite('Selfie/Selfie_'+ str(c) +'.png', img)
#         c += 1
#     if (key == 27):             # Exit if ESC is pressed
#         cam.release()
#         break



import cv2 as cv
import os

cam = cv.VideoCapture(0)

# Create folder if not exists
if not os.path.exists("Selfie"):
    os.makedirs("Selfie")

c = 0   # ✅ Initialize counter

while True:
    ret, img = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    img = cv.flip(img, 1)
    cv.imshow("Frame", img)

    key = cv.waitKey(20)

    if key == 13:  # Enter key
        cv.imwrite('Selfie/Selfie_' + str(c) + '.png', img)
        print("Selfie saved:", c)
        c += 1

    if key == 27:  # ESC key
        break

cam.release()
cv.destroyAllWindows()