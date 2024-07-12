sudo apt-get update -y && sudo apt-get upgrade -y
git clone https://github.com/DeKUT-DSAIL/powering-raspberrypi.git
git clone https://github.com/DeKUT-DSAIL/cameratrap-pi.git

echo "continue"
cd powering-raspberrypi
./requirements_setup.sh

echo "Install Python 3.10"
wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tar.xz
tar -xvf Python-3.10.0.tar.xz
cd Python-3.10.0
./configure --enable-optimizations
make -j 4
sudo make altinstall
python3.10 --version

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
