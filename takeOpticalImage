import cv2
import os
import time
import cv2
tic = time.time()
camera_port = 0
camera = cv2.VideoCapture(camera_port)
time.sleep(0.1)
return_value, image = camera.read()
cv2.imwrite("opencv.jpg", image)
toc = time.time()
print(toc-tic)
image = cv2.imread('/home/pi/PycharmProjects/seniordesign/opencv.jpg')
#resized_img = image[30:258, 60:240]
#cv2.imshow("Resize", resized_img)
#cv2.waitKey(0)
print(image)
