#...........Scaling................#
import cv2
import numpy as np

img = cv2.imread('Picture1-1.jpg')

# res = cv2.resize(img,None,fx=2, fy=2)
cv2.imshow("befor",img)
# cv2.imshow("befo",res)

#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height))
cv2.imshow("After",res)

h=cv2.waitKey(0)#when you anykey its store in h,27 is for q
if h==ord('q'):
    cv2.destroyAllWindows()
