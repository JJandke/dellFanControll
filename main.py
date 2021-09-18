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
    logging.info("{0}CPU Temperature: {1}".format(log_time, cpu))

    if cpu.temperature < lim10:
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x02 0xff 0xA")
        logging.info("{0}CPU Temperature: {1}".format(log_time, cpu_str))
        sleep(timer)

    # 20%
    elif lim10 <= cpu.temperature < lim20:
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x02 0xff 0x14")
        logging.info("{0}CPU Temperature: {1}".format(log_time, cpu_str))
        sleep(timer)

    # 30%
    elif lim20 <= cpu.temperature < lim30:
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x02 0xff 0x1E")
        logging.info("{0}CPU Temperature: {1}".format(log_time, cpu_str))
        sleep(timer)

    # 40%
    elif lim30 <= cpu.temperature < lim40:
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x02 0xff 0x28")
        logging.info("{0}CPU Temperature: {1}".format(log_time, cpu_str))
        sleep(timer)

    # 50%
    elif lim40 <= cpu.temperature < lim50:
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x02 0xff 0x32")
        logging.info("{0}CPU Temperature: {1}".format(log_time, cpu_str))
        sleep(timer)

    # 60%
    elif lim50 <= cpu.temperature < lim60:
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x02 0xff 0x3C")
        logging.info("{0}CPU Temperature: {1}".format(log_time, cpu_str))
        sleep(timer)

    # 70%
    elif lim60 <= cpu.temperature < lim70:
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x02 0xff 0x46")
        logging.info("{0}CPU Temperature: {1}".format(log_time, cpu_str))
        sleep(timer)

    # 80%
    elif lim70 <= cpu.temperature < lim80:
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x02 0xff 0x50")
        logging.info("{0}CPU Temperature: {1}".format(log_time, cpu_str))
        sleep(timer)

    # 90%
    elif lim80 <= cpu.temperature < lim90:
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x02 0xff 0x5A")
        logging.warning("{0}CPU Temperature: {1}".format(log_time, cpu_str))
        sleep(timer)

    # 100%
    elif lim90 <= cpu.temperature < lim100:
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x02 0xff 0x64")
        logging.warning("{0}CPU Temperature: {1}".format(log_time, cpu_str))
        sleep(timer)

    # 100% for twice the time
    elif cpu.temperature > lim100:
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x02 0xff 0x64")
        logging.critical("{0}CPU Temperature: {1}".format(log_time, cpu_str))
        sleep(timer*2)

    # ERROR. Something is broken or I am too stupid to write code
    else:
        logging.error("{0}Temperature does not match to any given case.\n{1}CPU Temperature: {2}".format(log_time, log_time, cpu_str))
        # setting fan speed to 100% just for case
        os.system("ipmitool -I lanplus -H 192.168.188.189 -U FanManagement -P 'keF78488479c%' raw 0x30 0x30 0x02 0xff 0x64")
        # Waiting the pre-set time anyway (otherwise the logfile will be spammed). Hopefully nothing burns down
        sleep(timer)
