# Loading an image using OpenCV #

import cv2

img=cv2.imread('Picture1-1.jpg',1)#read a image 
print(img)
cv2.imshow("display",img)
h=cv2.waitKey(0)#when you anykey its store in h,27 is for q
if h==ord('q'):
    cv2.destroyAllWindows()
elif h== ord('s'):
    cv2.imwrite('hcopy.png',img)
    cv2.destroyAllWindows()
print("Image Properties")
print("- Number of Pixels: " + str(img.size))
print("- Shape/Dimensions: " + str(img.shape))
