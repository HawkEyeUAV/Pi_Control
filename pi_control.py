#!/usr/bin/env python
# -*- coding: utf-8 -*-


from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import serial
import json
import os
from pymavlink import mavutil
##import argparse


def argparse(): 
    import argparse 
    parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
    parser.add_argument('--connect', 
                       help="Vehicle connection target string. If not specified, SITL automatically started and used.")
    args = vars(parser.parse_args())
   # args = parser.parse_args()
    conf = json.load(open(args["connect"]))
    print conf
    connection_str = conf["address"]
    sitl = None
    return connection_str
#Start SITL if no connection string specified
def connection():
    connection_string=argparse()
    if not connection_string:
        import dronekit_sitl
        sitl = dronekit_sitl.start_default()
        connection_string = sitl.connection_string()
# Connect to the Vehicle. 
#   Set `wait_ready=True` to ensure default attributes are populated before `connect()` returns.
    return connection_string
def v_attributes():
    # Get some vehicle attributes (state)
    data=[]
    fun_list=[vehicle.gps_0,vehicle.battery,vehicle.groundspeed,
             vehicle.version,vehicle.location.global_frame,
             vehicle.location.global_relative_frame,vehicle.location.local_frame, 
             vehicle.attitude,vehicle.velocity,vehicle.airspeed,
             vehicle.gimbal,vehicle.ekf_ok,vehicle.heading,
             vehicle.is_armable,vehicle.mode.name                                  


             ]
    # vehicle is an instance of the Vehicle class
    print "Autopilot Firmware version: %s" % vehicle.version
    print "Autopilot capabilities (supports ftp): %s" % vehicle.capabilities.ftp
    print "Global Location: %s" % vehicle.location.global_frame
    print "Global Location (relative altitude): %s" % vehicle.location.global_relative_frame
    print "Local Location: %s" % vehicle.location.local_frame    #NED
    print "Attitude: %s" % vehicle.attitude
    print "Velocity: %s" % vehicle.velocity
    print "GPS: %s" % vehicle.gps_0
    print "Groundspeed: %s" % vehicle.groundspeed
    print "Airspeed: %s" % vehicle.airspeed
    print "Gimbal status: %s" % vehicle.gimbal
    print "Battery: %s" % vehicle.battery
    print "EKF OK?: %s" % vehicle.ekf_ok
    print "Last Heartbeat: %s" % vehicle.last_heartbeat
    print "Rangefinder: %s" % vehicle.rangefinder
    print "Rangefinder distance: %s" % vehicle.rangefinder.distance
    print "Rangefinder voltage: %s" % vehicle.rangefinder.voltage
    print "Heading: %s" % vehicle.heading
    print "Is Armable?: %s" % vehicle.is_armable
    print "System status: %s" % vehicle.system_status.state
    print "Mode: %s" % vehicle.mode.name    # settable
    print "Armed: %s" % vehicle.armed    # settable
    for name in fun_list:
        deta.append(name)
        print data
    # Close vehicle object before exiting script
   # vehicle.close()
    # print 'Connecting to vehicle on: %s' %vehicle
    #vehicle = connect(connection_string, wait_ready=True)

    return data
def arm():
    print "Basic pre-arm checks"
    # Don't try to arm until autopilot is ready
    
    while not vehicle.is_armable:
       print " Waiting for vehicle to initialise..."
       time.sleep(2)
    print "Arming motors"
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("STABILIZE")
    vehicle.armed = True    
    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:      
        print " Waiting for arming..."
        time.sleep(5)
  #      for i in range(6):
  #          vehicle.armed=True
  #          time.sleep(3)
        break
    if vehicle.armed !=None:
        print("Vehicle is armed,CurrentMode:%s")%vehicle.mode
def GUIDED_Mode(aTargetAltitude):
    vehicle.airspeed = 3
    print "Taking off!"
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt 
        #Break and return from function just below target altitude.        
        if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95: 
            print "Reached target altitude"
            break
        time.sleep(1)
    print "Going towards first point for 30 seconds ..."
    point1 = LocationGlobalRelative(-35.361354, 149.165218, 20)
    vehicle.simple_goto(point1)
    time.sleep(30)
    print "Going towards second point for 30 seconds (groundspeed set to 10 m/s) ..."
    point2 = LocationGlobalRelative(-35.363244, 149.168801, 20)
    vehicle.simple_goto(point2, groundspeed=10)

    # sleep so we can see the change in map
    time.sleep(30)

    print "Reaching the targetpoint"

def RTL_Mode():


    print("PreRTL......")
    vehicle.mode = VehicleMode("RTL")

    #Close vehicle object before exiting script
if __name__=="__main__":
    argparse()
    connection_string1=connection()
   
    vehicle = connect(connection_string1, wait_ready=True)
#        global vehicle
    print "\nConnecting to vehicle on: %s" % connection_string1

    vehicle.wait_ready('autopilot_version')

    v_attributes()
    arm()
   # GUIDED_Mode()
   # RTL_Mode()
    print "Close vehicle object"
    vehicle.close()

# Shut down simulator if it was started.
    if sitl is not None:
        sitl.stop()
