#from pyimagesearch.tempimage import TempImage
from picamera.array import PiRGBArray
from picamera import PiCamera
from functools import partial
#from creat_faceID import creat_faceid
from Search import search
#from send_message import send
import argparse
import warnings
import datetime
#import imutils
import json
import time
import cv2
import os
import multiprocessing as mp
import urllib2
import urllib
import re
import urlparse

### Setup #####################################################################

def setup1():
# Setup the camera
    camera = PiCamera()
    camera.resolution = ( 320, 240 )
    camera.framerate =16
    rawCapture = PiRGBArray( camera, size=( 320, 240 ) )

# Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier( '/home/pi/opencv-3.1.0/data/lbpcascades/lbpcascade_frontalface.xml' ) 

    t_start = time.time()
    fps = 0


### Main ######################################################################

# Capture frames from the camera
    for frame in camera.capture_continuous( rawCapture, format="bgr", use_video_port=True ):
        confidence=0
        image = frame.array
        gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )
        faces = face_cascade.detectMultiScale( gray )

        print "Found " + str( len( faces ) ) + " face(s)"
        str_face=str(len(faces))
        int_face=int(str_face)
        print (int_face,type(int_face))
        if int_face!=0:
            camera.capture('/home/pi/Pictures/face.jpg')
            print "Searching......"
            time.sleep(2)
            (a,b)=search()
            print (a,b)
            time.sleep(1)        
            c=float(a)
            d=b
            print d,type(d)
            if c>70:
                print"i know him"
                confidence=68
                break
            else:
                print "He(She) is a stranger"    
                confidence=0
   # for ( x, y, w, h ) in faces:

    #    cv2.rectangle( image, ( x, y ), ( x + w, y + h ), ( 100, 255, 100 ), 2 )
       # cv2.putText( image, "Face No." + str( len( faces ) ), ( x, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )

            
    # Calculate and show the FPS
        fps = fps + 1
        sfps = fps / ( time.time() - t_start )
   # cv2.putText( image, "FPS : " + str( int( sfps ) ), ( 10, 10 ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, ( 0, 0, 255 ), 2 )    

    # Show the frame
   # cv2.imshow( "Frame", image )
   # cv2.waitKey( 1 )
       # if key == ord("q"):
       #     break   
    # Clear the stream in preparation for the next frame
        rawCapture.truncate( 0 )
#def setup1()
   # mm=100
   # print mm
    return confidence    
if  __name__=="__main__":
    setup1()
   # a= setup1()
   # a=test()
   # print a
