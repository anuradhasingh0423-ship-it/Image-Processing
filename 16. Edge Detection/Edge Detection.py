import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    _, img = cam.read()
    img = cv.flip(img, 1)

    edge_1 = cv.Canny(img, 100, 200)
    edge_2 = cv.Canny(img, 150, 250)

    cv.imshow("Frame", img)
    cv.imshow("Edges-1", edge_1)
    cv.imshow("Edges-2", edge_2)

    if cv.waitKey(10) == 27:  # ESC key to exit
        cam.release()
       
        break