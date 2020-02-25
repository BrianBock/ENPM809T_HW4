# Brian Bock
# ENPM809T
# HW 4

# import the necessary packages
# from picamera.array import PiRGBArray
# from picamera import PiCamera
# import time
import datetime
from datetime import datetime
import cv2
# from imutils.video import VideoStream
import imutils
import numpy as np
from functions import*

# Record the start time so we can compute run time at the end
start = datetime.now()

#import image
imgPath="downarrow3.jpg"
frame=cv2.imread(imgPath)

if frame is None:
	print("Unable to import '"+imgPath+"'. Quitting.")
	exit()

orientation=ArrowOrientation(frame)


#Write orientation to the image
# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
  
# orgin 
org = (100, 275) 
  
# fontScale 
fontScale = 10
   
# Blue color in BGR 
color = (255, 0, 255) 
  
# Line thickness of 2 px 
thickness = 15
   
# Using cv2.putText() method 
image = cv2.putText(frame, orientation, org, font, fontScale, color, thickness, cv2.LINE_AA)


imagesmall=imutils.resize(image,width=640)
cv2.imshow("Corners and Orientation", imagesmall)
cv2.waitKey(0)
# if cv2.waitKey(1) == ord('q'):
# 	break



