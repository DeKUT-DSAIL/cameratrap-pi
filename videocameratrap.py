'''
This program will be used on raspberrypi to capture
images using a picamera once motion is detected.
'''

from gpiozero import MotionSensor
from picamera import PiCamera
import RPi.GPIO as GPIO
import logging
import os
import time
from subprocess import call

time.sleep(30)

logging.basicConfig(filename='cameratrap.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

if not os.path.exists("/home/pi/cameratrap"):
    os.mkdir("/home/pi/cameratrap")

try:
    #set GPIO pin 17 as input from the Motion Sensor
    #set GPIO pin 27 as an output for the LED
    pir = MotionSensor(17) 
    camera = PiCamera()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.HIGH)
    GPIO.setup(27, GPIO.LOW) 

    while True:
        if GPIO.input(17):
           print("Motion detected!")           
           camera.start_preview()
           #filename = "/home/pi/cameratrap/" + (time.strftime("%Y-%m-%d-%H-%M-%S")) + ".jpg"
           filename_h264 = "/home/pi/cameratrap/" + (time.strftime("%Y-%m-%d-%H-%M-%S")) + ".h264"
           filename_mp4 = "/home/pi/cameratrap/" + (time.strftime("%Y-%m-%d-%H-%M-%S")) + ".mp4"
           #camera.stop_preview()
           #Capture video
           GPIO.output(27,1)
           camera.start_recording(filename_h264)
           camera.wait_recording(10)
           camera.stop_recording()
           #print("Motion detected!")
           time.sleep(2)
           #Convert video from h264 to mp4
           #MP$Box is installed by 'sudo apt-get install gpac'
           #command = "MP4Box -add " + filename_h264 + " " + filename_mp4
           #call([command], shell=True)
           #print("Converted H264 to MP4! \r\n")
        else:
            print("No motion detected!")
            GPIO.output(27,0)
            time.sleep(2)
            
except Exception as err:
    logging.info(str(err))
    print('Error')


