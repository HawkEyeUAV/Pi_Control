#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
import os
import cv2
from search_face import setup1
  
def face_test():
    
  
    while 1:
        print "lik"
       # break
        aa=0
       # mm=setup1()
       # if mm==68:
       #    print "mm 68";
       #    break
        
        cmd = 'python search_face.py '    #必须转义'\'
        aa= os.system(cmd)
  
       # mm = setup1()
       # print "shibie break"
       # mm=setup1()
       # print "MM"%mm
        if aa==0:
           print "mm:68"
           break
        else:
           print aa
       #    continue
       # break
       # time.sleep(1)
    return 888888    
if __name__ == '__main__':
    
   a= face_test()
  
   print a
