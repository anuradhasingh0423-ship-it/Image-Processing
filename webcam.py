import cv2 as cv

cam = cv.VideoCapture(0)

cam.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

if not cam.isOpened():
    print("Camera failed to open")
    exit()

while True:
    ret, frame = cam.read()

    if not ret:
        print("Failed to grab frame")
        break

    cv.imshow("Zebronics Webcam", frame)

    if cv.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

cam.release()
cv.destroyAllWindows()