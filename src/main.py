import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import sys
import subprocess 
import threading
import ping
import argparse

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

    def animate(self, i):

        time = float(IPC.getMessages(self))
        self.yar.append(time)
        self.xar.append(self.seconds)
        self.ax1.clear()
        self.ax1.plot(self.xar, self.yar)
        self.seconds += 1

    def draw(self):
        ani         = animation.FuncAnimation(self.fig, self.animate, interval=1000)
        plt.show()

def main():
    parser = argparse.ArgumentParser(description = "The main file for running the graph.")
    parser.add_argument("host", help = "The host to ping.")
    parser.add_argument("interval", help = "The interval (in seconds) to ping.") 

    args        = parser.parse_args()
    host        = args.host
    interval    = args.interval

    fig         = plt.figure()
    ax1         = fig.add_subplot(1,1,1)
    graph       = Graph(host, fig, ax1)

    t           = threading.Thread(target=ping.ping, args=(host, interval,))
    t.daemon    = True
    t.start()

    graph.draw()

if __name__ == "__main__":
    main()


    
