import cv2

image = cv2.imread('KarisCalibrate.5Optics.jpg')
resized_img = image[30:258, 60:240]
cv2.imshow("Resize", resized_img)
cv2.waitKey(0)

