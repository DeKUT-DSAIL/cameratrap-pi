'''
This program will be used on raspberrypi to capture
images using a picamera once motion is detected.
'''

from gpiozero import MotionSensor
from picamera2 import PiCamera2
import RPi.GPIO as GPIO
import logging
import os
import time

time.sleep(30)

logging.basicConfig(filename='cameratrap.log', level=logging.DEBUG, 
                    format='%(asctime)s:%(levelname)s:%(message)s')

if not os.path.exists("/home/pi/cameratrap"):
    os.mkdir("/home/pi/cameratrap")

try:
    #set GPIO pin 17 as input from the Motion Sensor
    #set GPIO pin 27 as an output for the LED
    pir = MotionSensor(17) 
    camera = PiCamera2()
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.HIGH)
    GPIO.setup(27, GPIO.LOW) 

    while True:
        if GPIO.input(17):
           camera.start_preview()
           filename = "/home/pi/cameratrap/" + (time.strftime("%Y-%m-%d-%H-%M-%S")) + ".jpg"
           camera.capture(filename)
           camera.stop_preview()
           print("Motion detected!")
           GPIO.output(27,1)
           time.sleep(2)
        else:
            print("No motion detected!")
            GPIO.output(27,0)
            time.sleep(2)
            
except Exception as err:
    logging.info(str(err))


