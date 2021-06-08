from gpiozero import MotionSensor
from picamera import PiCamera
import RPi.GPIO as GPIO
import time

pir = MotionSensor(17)
camera = PiCamera()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.HIGH)
GPIO.setup(18, GPIO.LOW)

while True:
    if GPIO.input(17) == 1:
       camera.start_preview()
       filename = "/home/pi/Desktop/images/" + (time.strftime("%y%b%d_%H:%M:%S")) + ".jpg"
       camera.capture(filename)
       print("motion detected!")
       GPIO.output(18,1)
       time.sleep(3)
    else:
        print("no motion detected!")
        GPIO.output(18,0)
        time.sleep(3)
        camera.stop_preview()


