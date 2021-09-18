#!/usr/bin/env python3

import os
import logging
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
