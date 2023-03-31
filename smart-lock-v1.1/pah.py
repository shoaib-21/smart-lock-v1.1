import paho.mqtt.client as mqtt
import time
import json
import userdb
import adduser
import os


def userexists(username):
    parentdir = r'/home/pi/facial-recognition-main/dataset'
    path = os.path.join(parentdir, username)
    return os.path.exists(path)
def on_log(client, userdata, level, buf):
    print("log: ",+buf)
    
def on_message(client, userdata,msg):
    m_decode = str(msg.payload.decode("utf-8","ignore"))
    m_json = json.loads(m_decode)
    print(m_json)
    time.sleep(2)
    op = m_json['operation']
    if op =='adduser':
        username = m_json['name']
        if userexists(username):
            #no enrollment
            print('user already exists')
        else :
            #enrollment
            adduser.enroll_new_user(m_json['name'],m_json['empId'])
            
    elif op == 'deluser':
        #delete a user
        print('del user')
        
    else:
        print('no operation')
         
     
    
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK rc = ",str(rc)," flags = ",str(flags))
        
    else:
        print("Bad connection returned code : ",rc)
        
def on_disconnect(client, userdata, flags, rc=0):
    print("disconnected result code:" +str(rc))
    

def connect_admin():
    
    broker_address='192.168.0.10'
    client = mqtt.Client('lkjui',transport='websockets') #create new instance
    client.on_connect = on_connect
    #client.on_disconnect = on_disconnect
    client.on_log = on_log
    client.on_message = on_message

    print("connecting to broker ",broker_address)
    client.username_pw_set("mna","mna0845")
    client.connect(broker_address,1901,150)#connect to broker
    client.loop_start()
    client.subscribe("admin",1,True)
    time.sleep(0.1)
    client.loop_stop()
    client.disconnect()

