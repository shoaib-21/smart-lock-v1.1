import cv2
import face_recognition
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import os
import lcd_display
def headshots(personName):
#personName = 'shaik sharfuddin' #replace with your name
    parentDir = "/home/pi/facial-recognition-main/dataset/"
    path = os.path.join(parentDir,personName)
    os.mkdir(path)
    cam = PiCamera()
    cam.resolution = (640,480)#modified from 512, 304
    cam.framerate = 20
    rawCapture = PiRGBArray(cam, size=(640, 480))
        
    img_counter = 0
    timeout_start = time.time()
    while True:
        for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            boxes = face_recognition.face_locations(image)
            detectedFaces = len(boxes)
            cv2.imshow("be in a frame ", image)
            rawCapture.truncate(0)
            
            k = cv2.waitKey(1)
            rawCapture.truncate(0)
            if detectedFaces == 1:
                img_name = "/home/pi/facial-recognition-main/dataset/"+ personName +"/image_{}.jpg".format(img_counter)
                cv2.imwrite(img_name, image)
                print("{} written!".format(img_name))
                #lcd_display.display_msg(f'TAKEN {img_counter}',' IMAGES SUCCESSFULLY ')
                img_counter += 1
                
            elif detectedFaces>1:
                print("more than one person detected!!!")
                #lcd_display.display_msg('MORE THAN ONE ',' PERSON DETECTED ')
                time.sleep(0.2)
            else:
                print("no faces detected!!! please come in frame")
                #lcd_display.display_msg('NO FACE DETECTED',' BE IN A FRAME ')
                time.sleep(0.2)
            #time.sleep(0.20)
            if img_counter ==  10:
                print(time.time()-timeout_start)
                break
        if img_counter ==  10:
            break
        
    cam.close()#modified
    cv2.destroyAllWindows()
    return True
#headshots('mn')