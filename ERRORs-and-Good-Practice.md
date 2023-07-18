# Good Practice
1. Run setup while you have a good internet connection (MBps range rather than kbps). It may take 10-20 minutes with fast internet connection 
# Errors
1. Camera is not enabled issue yet running on sudo raspi-config shows enabled camera:
   -Reason : Raspberry Pi OS image based on debian Bulleye does not support Picamera and raspicam apps. Raspberry Pi's driver in (debian) to access camera modules has
   been replaced with libcamera. For more information on this have a look at [Bullseye camera system](https://www.raspberrypi.com/news/bullseye-camera-system/).

   - Best Solution : use Raspberry Pi OS Buster.
   - Other solution: find out how to use camera in Raspberry Pi Bullseye
  
   - To check you raspberry pi version: run `lsb_release -irdc`
