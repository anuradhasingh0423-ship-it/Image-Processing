# import cv2 as cv

# cam = cv.VideoCapture(0)
# while True:
#     _, img = cam.read()
#     img = cv.flip(img, 1)  # orginal image
#     blr = cv.blur(img, (5,5))  # blurred image
#     edg = cv.Canny(img, 0,50)  # edge detection on original image
#     fin = cv.Canny(blr, 0, 50) # edge detection on blurred image

#     cv.imshow("Frame", img)
#     cv.imshow("Blurred", blr)
#     cv.imshow("Edges on original", edg)
#     cv.imshow("Edges on Blurred", fin)
#     if cv.waitKey(10) == 27:  # ESC key to exit
#         cam.release()
#         break


import cv2 as cv

cam = cv.VideoCapture(0)

while True:
    ret, img = cam.read()
    if not ret:
        break

    img = cv.flip(img, 1)

    blr = cv.blur(img, (5,5))
    edg = cv.Canny(img, 0, 50)
    fin = cv.Canny(blr, 0, 50)

    # 🔹 Resize images to smaller size (e.g., half)
    img_small = cv.resize(img, (320, 240))
    blr_small = cv.resize(blr, (320, 240))
    edg_small = cv.resize(edg, (320, 240))
    fin_small = cv.resize(fin, (320, 240))

    cv.imshow("Frame", img_small)
    cv.imshow("Blurred", blr_small)
    cv.imshow("Edges on original", edg_small)
    cv.imshow("Edges on Blurred", fin_small)

    if cv.waitKey(10) == 27:
        break

cam.release()
cv.destroyAllWindows()