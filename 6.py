# ...........................bitwise_xor
import cv2
import numpy as np

img1=cv2.imread('image1.png')
img1=cv2.resize(img1,(500,250))

# img1=np.zeros((250,500,3),np.uint8)
# img1=cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
# img2=cv2.imread('Picture1-1.jpg')
img2=cv2.imread('image2.png')

img2=cv2.resize(img2,(500,250))
print(img2.shape)
Bitwisexor=cv2.bitwise_xor(img2,img1)

add_img=cv2.add(img1,img2)
cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.imshow('Bitwisexor',Bitwisexor)
cv2.imshow('addition_img',add_img)


cv2.waitKey(0)
cv2.destroyAllWindows()