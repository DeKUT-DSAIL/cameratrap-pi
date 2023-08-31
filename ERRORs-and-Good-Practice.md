# Good Practice
1. Run setup while you have a good internet connection (MBps range rather than kbps). It may take 30 minutes with fast internet connection

2. Raspberry Pi pinout diagram
   ![image](https://github.com/DeKUT-DSAIL/cameratrap-pi/assets/54037190/03cc3a34-3fc1-4ddc-9315-74a0712d01c2)
3. Accessing Raspberry Pi Remotely.
   
   a. Obtain IP address (given your raspberry pi is connected to the same network as your device.
   - Open `Putty` and add `raspberrypi.local` to it's SSH hostname/ipaddress, port 22 `default`.
   - Login
   - `hostname -I`
   - You now have the IP address.
   
   b. Open VNC Viewer
   - Input ip address in VNC connect.
   - You've now accessed your Raspberry Pi remotely.

   c. `forget a saved wifi network on a Raspberry Pi`
   -In the terminal type: sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
   -Delete the relevant wifi network block (including the ‘network=’ and opening/closing braces.
   -Press ctrl-x followed by ‘y’ and enter to save the file.
   -You’re done!

# Errors
1. Camera is not enabled issue yet running on sudo raspi-config shows enabled camera:
   -Reason : Raspberry Pi OS image based on debian Bulleye does not support Picamera and raspicam apps. Raspberry Pi's driver in (debian) to access camera modules has
   been replaced with libcamera. For more information on this have a look at [Bullseye camera system](https://www.raspberrypi.com/news/bullseye-camera-system/).

   - Best Solution : use Raspberry Pi OS Buster (legacy) 2023-05-03.
   - Other solution: find out how to use camera in Raspberry Pi Bullseye
  
   - To check you raspberry pi version: run `lsb_release -irdc`
   - Alternative Solutions [Using Bulleye Camera](https://www.tomshardware.com/how-to/use-raspberry-pi-camera-with-bullseye) and [The Raspberry Pi Camera With Python In 2023](https://raspberrytips.com/picamera2-raspberry-pi/)
