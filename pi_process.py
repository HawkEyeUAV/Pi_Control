#!
# -*- coding: utf-8 -*-   
from picamera.array import PiRGBArray
from picamera import PiCamera
from functools import partial
from Search import search
import argparse
import warnings
import datetime
import cv2
import multiprocessing as mp
import urllib2
import urllib
import re
import paho.mqtt.client as mqtt  
import os
import time
import multiprocessing
import pi_control
from multiprocessing import Pool,Pipe,Queue,Manager
import random
from mqtt_sub import on_connect,on_message
from dronekit import connect, VehicleMode, LocationGlobalRelative
import serial
import json
from pymavlink import mavutil
from face_final import face_test

   
    

def mosquitto_pub(q):

    print"process mosquitto_pub starting"
    while True:
           num=q.get()
           print num 
           os.system("mosquitto_pub -t uav_plane -h 139.199.24.250 -m %s"%(num))
           time.sleep(1)

def mosquitto_sub(qq):
    print"process mosquitto_sub starting"
    def on_connect(client,userdata,flags,rc):
        print ("Connected with result code"+str(rc))
        client.subscribe("uav_cloud")
    def on_message(client,userdata,msg):
        
        print(str(msg.payload))
        qq.put(str(msg.payload))
       # global data_sub=0

       # data_sub= msg.payload
       # return data_sub
       # print data_sub

    client=mqtt.Client()
    client.on_connect=on_connect
   # data=on_message()
    
    client.on_message=on_message
   # kk=client.on_message()
   # print "the receiveing data:%s"%(kk)
    try:
         client.connect("139.199.24.250",1883,60)
         client.loop_forever()
    except KeyboardInterrupt:
         client.disconnect()
    
def mqtt_server():
    os.system("mosquitto -v")    
def pi_con(q,lock,qq):
    
    print"process pi_con starting"
    print"Testing face......"
   # face_test()
   # print"ssd"
   # print face_test()
   # num1=qq.get()
   # print num1
    arm_data=face_test()
   
    if arm_data==888888:
        print"The test passes, ready to arm"
        vehicle = connect("/dev/ttyACM0", wait_ready=True)
        print "\nConnecting to vehicle on: %s" % vehicle
        lock.acquire()
        i="uav"
        q.put(i)
        num1=qq.get()
        print "get:"+ num1
        exec "%s"%(num1)
        vehicle.wait_ready('autopilot_version')
   # v_attributes()
#    data=v_attributes()
   # like=666666
   # q.put(like)
    #pipb.send(like)
        arm()
   # GUIDED_Mode()
   # RTL_Mode()
        print "Close vehicle object"
        vehicle.close()


if __name__ == "__main__":
     pool = Pool(3)
     manager = multiprocessing.Manager()
     q = manager.Queue()
     lock = manager.Lock()
     qq=manager.Queue()
    # function_list=  [mosquitto_pub, mosquitto_sub, pi_con] 
    # for func in function_list:
    #     pool.apply_async(func,)
     pool.apply_async(pi_con,args=(q,lock,qq))
     pool.apply_async(mosquitto_pub,args=(q,))
     pool.apply_async(mosquitto_sub,args=(qq,))

     pool.close()  
    
     pool.join()
    # print"waiting......"   
          
