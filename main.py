import numpy as np
from cv2 import cv2

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow('gray',gray)
    cv2.imshow('color',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows
