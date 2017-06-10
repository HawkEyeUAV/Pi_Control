import os
import re
import paho.mqtt.client as mqtt
#import MySQLdb

def on_connect(client,userdata,flags,rc):
    print ("Connected with result code"+str(rc))
    client.subscribe("uav_cloud")
def on_message(client,userdata,msg):
    print(msg.topic+" "+str(msg.payload))
  #  return str(msg.payload)
   # print str(msg.payload)
   # aa=str(msg.payload)
   # bb=re.split('f',aa)
   # print bb[1],type(bb)
   # cc=re.split('a',bb[1])
   # print cc[0],cc[1],cc[2],type(cc[0])
   # cur.execute("insert into table1(id,wendu,shidu,distance,time) values(null,%$
   # conn.commit()
if __name__=='__main__':
    client=mqtt.Client()
    client.on_connect=on_connect
    client.on_message=on_message
    try:
         client.connect("139.199.24.250",1883,60)
         client.loop_forever()
    except KeyboardInterrupt:
         client.disconnect()


