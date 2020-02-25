# Brian Bock
# ENPM809T
# HW 3

#https://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
#https://www.pyimagesearch.com/2016/02/22/writing-to-video-with-opencv/
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import datetime
from datetime import datetime
import cv2
from imutils.video import VideoStream
import imutils
from functions import*


start = datetime.now()
# Create dataFile.txt file, which will house all of the timing we record
dataFile=open("dataFile.txt","a+") #a+ for append. Be sure to delete the file from previous runs before starting



# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (1920, 1088)
camera.framerate = 2
rawCapture = PiRGBArray(camera, size=(1920, 1088))

#Define the codec
today = time.strftime("%Y%m%d-%H%M%S")
fps_out = 2
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(today + ".avi", fourcc, fps_out, (1920, 1088))



# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera
for myframe in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	frame = myframe.array

	
	orientation=ArrowOrientation(frame)
	if orientation is None:
		orientation="Unknown"


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




	# show the frame
	imagesmall=imutils.resize(image,width=640)
	cv2.imshow("Frame", imagesmall)
	cv2.waitKey(60)
	key = cv2.waitKey(60) & 0xFF

	#save the frame to a file
	out.write(image)
	end = datetime.now()
	warptime=end-start
	print("Finished warp in "+str(warptime)+" (hours:min:sec)")
	dataFile.write(str(warptime)+"\n")

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break