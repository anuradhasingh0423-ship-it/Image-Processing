import cv2 as cv
import numpy as np
import os


def show_image(name, image, max_width=700):
    h, w = image.shape[:2]

    if w > max_width:
        scale = max_width / w
        image = cv.resize(image, (int(w * scale), int(h * scale)))

    cv.imshow(name, image)


def apply_filter(image_path, filter_path, alpha):

    img = cv.imread(image_path)
    filter_img = cv.imread(filter_path)

    if img is None:
        print("Main image not found")
        return

    if filter_img is None:
        print("Filter image not found")
        return

    # Resize filter to match main image
    filter_img = cv.resize(filter_img, (img.shape[1], img.shape[0]))

    # Blend
    result = cv.addWeighted(img, 1 - alpha, filter_img, alpha, 0)

    show_image("Original", img)
    show_image("Filtered Output", result)

    cv.waitKey(0)
    cv.destroyAllWindows()


current_dir = os.path.dirname(os.path.abspath(__file__))

anu = os.path.join(current_dir, "anu.jpg")
blue_filter = os.path.join(current_dir, "b1.jpeg")

apply_filter(anu, blue_filter, 0.25)