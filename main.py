#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for the script gpiozero is needed.
# It can be installed using "sudo pip3 install gpiozero".


import os
import logging
import datetime
from time import sleep
from gpiozero import CPUTemperature

# - - - - - - - - - - - - - - - #
# Configure your settings here  #
# - - - - - - - - - - - - - - - #
# set path for the log file to live
log_path = "./test.log"

# set time to wait until temperature will be checked again (in seconds)
# 1min=60s; 2min=120s; 5min=300s; 10min=600s; 15min=900s; 20min=1200; 30min=1800
timer = 120

# temperature limits
#   |-fan speed in %
#   |    |-max temperature for fan speed in °C
#   |    |
lim10 = 30
lim20 = 40
lim30 = 50
lim40 = 60
lim50 = 65
lim60 = 70
lim70 = 73
lim80 = 76
lim90 = 80
lim100 = 90
# Example: The CPU temperature is 45°C, so the fan runs at 30% of its maximum speed

# check at boot, if logfile exists. If not, create one
if not os.path.isfile(log_path):
    f = open(log_path, "x")
    f.close()
else:
    print("logfile already exists")

# set up logging mode. Following modes are available:
# level     numeric value (if needed)
# CRITICAL  50
# ERROR     40
# WARNING   30
# INFO      20
# DEBUG     10
# NOTSET    0
logging.basicConfig(filename=log_path, level=logging.DEBUG)

# set formatted time for logging
day = datetime.datetime.now()
log_time = day.strftime("%a-%d.%m.%Y-%H:%M:%S ")
logging.info("{0}Set up time".format(log_time))

# activate manual fan controll


while True:
    day = datetime.datetime.now()
    log_time = day.strftime("%a-%d.%m.%Y-%H:%M:%S ")
    cpu = CPUTemperature
    cpu_str = str(cpu)
    logging.info("{0}CPU Temperature: {1}".format(log_time, cpu_temp))

    if cpu.temperature < lim10:
        logging.info("{0}Cpu Temperature: {1}".format(log_time, cpu_str))
        sleep(timer)

    elif lim10 <= cpu.temperature < lim20:
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x01 0x00")
        logging.info("{0}Cpu Temperature: {1}".format(log_time, cpu_str))
        sleep(timer)

