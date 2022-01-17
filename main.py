from cv2 import cv2
img=cv2.imread('Capture001.png',cv2.IMREAD_UNCHANGED)
print("Original",img.shape)
scale_percent=20
width=int(img.shape[1]*scale_percent/100)
height=int(img.shape[0]*scale_percent/100)
dim=(width,height)
resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print("Resized",resized.shape)
cv2.imshow("Resized",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()