## watering_scheduler

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Quick-n-dirty script to manage my garden's irrigation system.

I use a Raspberry Pi Zero W to open and close a 
[3/4" sprinkler valve](https://www.homedepot.com/p/Orbit-3-4-in-FPT-Auto-Inline-Valve-57280/300642253) 
connected to some drip lines. Currently, I use cron to schedule when I turn it on and off.  In the future, 
I'd like to add a moisture sensor to help save water.

Note: I'm using [raspbian](https://www.raspberrypi.org/downloads/raspbian/), which includes [RPi.GPIO](https://pypi.org/project/RPi.GPIO/).  
If you are not, you will have to install it separately. [This post](https://raspberrypi.stackexchange.com/questions/8220/how-to-correctly-install-the-python-rpi-gpio-library)
should give you some help. 




MIT License<br> 
Copyright 2019 Alexander Potts
