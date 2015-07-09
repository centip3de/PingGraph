import subprocess
import time

from IPC import *

def ping(hostname, interval):
    while True:
        status, result  = subprocess.getstatusoutput("ping -c1 " + str(hostname))

        if(status == 0):
            time_string = result.split("time=")[1]
            pingTime    = float(time_string.split(" ")[0])

            IPC.sendToAll(pingTime)
            time.sleep(float(interval))

        else:
            return -1
