import cv2 as cv

# Use OpenCV built-in cascade path (very important)
classifier = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cam = cv.VideoCapture(0)

while True:
    
    ret, img = cam.read()
    if not ret:
        break

    img = cv.flip(img, 1)

    # Convert to grayscale (VERY IMPORTANT)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Better detection parameters
    faces = classifier.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv.imshow('Frame', img)

    if cv.waitKey(1) == 27:
        break

cam.release()
cv.destroyAllWindows()