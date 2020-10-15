#perform some basic operation on images(arithematic operation)
import cv2
import numpy as np

img=cv2.imread('Picture1-1.jpg',1)
# img2=cv2.imread('ex.jpg',1)
cv2.imshow("img",img)

# print(img)
# print()

print(img.shape)# it return no of coloum and row  and channel in tuple formate
print(img.size)#total no of pixel is accessed
print(img.dtype)#return image data type is obtained

b,g,r=cv2.split(img)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)

image_RGB=cv2.merge((r,g,b))
cv2.imshow("image_RGB",image_RGB)

region=img[200:250, 200:250]
print(region)

# img[100:150,100:150]=region
# cv2.imshow("blueq",img)

# print(b)
# print(g)
# print(r)

#ROI(REGION OF INTRESET)
# img=cv2.resize(img,(512,512))
# img2=cv2.resize(img2,(512,512))

# dst=cv2.add(img,img2)
# dst2=cv2.addWeighted(img,.9,img2,.1,0)
# cv2.imshow('image',dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()