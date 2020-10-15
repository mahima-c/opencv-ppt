#.................Changing Colorspaces......................#
# There are more than 150 color-space conversion methods available in OpenCV. 
# But we will look into only two which are most widely used ones, 
# BGR-Gray and BGR -HSV.
import cv2

img=cv2.imread('Picture1-1.jpg',1)#read a image 
cv2.imshow("original",img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

h=cv2.waitKey(0)#when you anykey its store in h,27 is for q
if h==ord('q'):
    cv2.destroyAllWindows()
elif h== ord('s'):
    cv2.imwrite('hcopy.png',img)
    cv2.destroyAllWindows()
print("Image Properties")
print("- Number of Pixels: " + str(img.size))
print("- Shape/Dimensions: " + str(img.shape))
print("- Number of Pixels gray: " + str(gray.size))
print("- Shape/Dimensions gray: " + str(gray.shape))