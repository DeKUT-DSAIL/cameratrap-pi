# Camera trap 

## Background
Having up to date information about the location and behaviour of animals in the wild will improve our ability to study and better conserve natural ecosystems. It will also help us mange and protect these ecosystems. 

Motion sensor cameras in natural habitats offer an inexpensive opportunity to gather data on animals.


## Introduction

This project has been deployed in Dedan Kimathi University's conservancy in Kenya. 
The camera trap is being used to collect images of animals in the conservancy with the aim of identifying predators, which is a problem the rangers have.
It is based on a passive infrared (PIR) MOTION sensor and a raspberry pi with a pi camera, running on a python program. 
It is set in such a way that once motion is detected, the camera captures images and saves them in an SD card. 
A solar panel is used to recharge batteries. Our current powering system enables our camera trap to stay in the field for a week, after which batteries are recharged and SD cards changed. We currently have 3 camera traps in the conservancy.

![21Jul09_17_49_24-2](https://user-images.githubusercontent.com/74656615/134635155-9b8b6b24-b332-453f-801c-2ae9e726c07a.jpg)



## Our Data
Our data is in the form of images saved in jpg format. They are saved in the format YY-MM-DD-H-M-S.
The animals included in our dataset are Impalas, monkeys, warthogs, bushbucks, waterbucks and zebras.

##Raspberrypi Ssetup process

1. Clone the following folders containing environment setup, and necessary python files.

      git clone https://github.com/DeKUT-DSAIL/powering-raspberrypi.git
      git clone https://github.com/DeKUT-DSAIL/cameratrap-pi.git
      git clone https://github.com/kiariegabriel/rpi-.git
2. on the terminal, run the following lines one after the other to setup the environment and install required modules.

    cd powering-raspberrypi
    ./env-setup-bash
2. Change permission for the bash files we will use to make our cameratrap work.

    cd
    cd cameratrap-pi
    chmod +x cameratrap-bash.sh
    chmod +x power-management-bash.sh
    
3. Set crontab for the bash files to run @reboot
    
    crontab -l
    
    chmod +x time-set-bash.sh





