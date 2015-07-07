import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import sys
import subprocess 

from IPC import *

class Graph():

    def __init__(self, host, fig, ax1):
        self.fig        = fig 
        self.ax1        = ax1 
        self.host       = host 
        self.seconds    = 0 
        self.xar        = []
        self.yar        = []

        IPC.add(self)

    def ping(self, hostname):
        status, result  = subprocess.getstatusoutput("ping -c1 " + str(hostname))

        if(status == 0):
            time_string = result.split("time=")[1]
            time        = float(time_string.split(" ")[0])
            return time

        else:
            return -1

    def animate(self, i):

        time = self.ping(self.host)
        self.yar.append(time)
        self.xar.append(self.seconds)
        self.ax1.clear()
        self.ax1.plot(self.xar, self.yar)
        
        self.seconds += 1

    def draw(self):
        ani         = animation.FuncAnimation(self.fig, self.animate, interval=1000)
        plt.show()

if __name__ == "__main__":

    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <hostname>")
        quit(1)

    host    = sys.argv[1]
    fig     = plt.figure()
    ax1     = fig.add_subplot(1,1,1)
    graph   = Graph(host, fig, ax1)

    graph.draw()
