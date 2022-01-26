import cv2

mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
# Read the input image
img = cv2.imread('JoshuaTest6Feet.jpg')
img2 = cv2.imread('JoshuaTest6Feet.jpg')
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
mouth = mouth_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in mouth:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
# Display the output

cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.waitKey()
