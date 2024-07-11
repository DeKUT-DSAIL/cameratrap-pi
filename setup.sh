sudo apt-get update -y && sudo apt-get upgrade -y
git clone https://github.com/DeKUT-DSAIL/powering-raspberrypi.git
git clone https://github.com/DeKUT-DSAIL/cameratrap-pi.git
cd powering-raspberrypi
./requirements_setup.sh
cd
cd cameratrap-pi
chmod +x power.sh
chmod +x timeset.sh
chmod +x cameratrap.sh
cd
# Add the desired commands to the crontab
(crontab -l ; echo "@reboot /home/pi/cameratrap-pi/power.sh") | crontab -
(crontab -l ; echo "@reboot /home/pi/cameratrap-pi/timeset.sh") | crontab -
(crontab -l ; echo "@reboot /home/pi/cameratrap-pi/cameratrap.sh") | crontab -
