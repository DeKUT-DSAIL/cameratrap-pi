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
