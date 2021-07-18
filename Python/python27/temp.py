# -*- coding: utf-8 -*-
import time
import sys

for i in range(10):
    sys.stdout.write('#'*(i+1)+'\r')
    sys.stdout.flush()
    time.sleep(1)
