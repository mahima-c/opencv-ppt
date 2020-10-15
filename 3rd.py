#..............capture livestream from camera.............................#

# This time we create a VideoWriter object. We should specify 
# the output file name (eg: output.avi). Then we should specify the 
# FourCC code (details in next paragraph). Then number of frames per second (fps) 
# and frame size should be passed. And last one is isColor flag. If it is True, 
# encoder expect color frame, otherwise it works with grayscale frame.

# FourCC is a 4-byte code used to specify the video codec.
import cv2

#if we want to read viedo from anyfile then give filename as parameter of viedocapture
#for read from camera give the index 0 or some device have -1 also and if we have multiple camera then we use index as 1,2,3 as.

cap= cv2.VideoCapture(0);
#create class for write viedo      fourcc code which is specify for viedo codec ,identify the data formate
# Define the codec and create VideoWriter object

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(True):
    #for capture
    ret,frame = cap.read()
    #if frame is available then ret is ture otherwise false

    if ret ==True:
        
        # write the flipped frame
        out.write(frame)
        
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',gray)
        
        #IF user press q then quit the window
        #waitkey is that wait whenever user give any input
        if cv2.waitKey(1) == ord('q'):
            break

    else:
        break
# Release everything if job is finished

cap.release()
out.release()

cv2.destroyAllWindows()   