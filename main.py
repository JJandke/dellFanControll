#!/usr/bin/env python3

import os
import logging
import datetime
from time import sleep


##
# set path for the log file to live
log_path = "./test.log"


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
log_time = day.strftime("%a-%d.%m.%Y-%H:%M:%S")
logging.info("{0}Set up time".format(log_time))