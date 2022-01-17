from cv2 import cv2
img=cv2.imread('Capture001.png')
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image',img)
cv2.imshow('B/W',gray_img)
cv2.waitKey(0)
