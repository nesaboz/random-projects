import cv2
import sys
# img = cv2.imread(r'C:\supreme-engine\Python_mega_course\15_170_Moving object detection\galaxy.jpg', -1)
img = cv2.imread('galaxy.jpg', 0)
print(type(img))
print(img.ndim)

cv2.imshow("Galaxy", img)
cv2.waitKey(2000)