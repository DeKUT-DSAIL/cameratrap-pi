'''
This program will be used on raspberrypi to capture
images using a picamera once motion is detected.
'''

from gpiozero import MotionSensor
from picamera import PiCamera
import RPi.GPIO as GPIO
import time

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
       camera.start_preview()
       filename = "/home/pi/Desktop/images/" + (time.strftime("%y%b%d_%H:%M:%S")) + ".jpg"
       camera.capture(filename)
       print("motion detected!")
       GPIO.output(27,1)
       time.sleep(3)
    else:
        print("no motion detected!")
        GPIO.output(27,0)
        time.sleep(3)
        camera.stop_preview()


