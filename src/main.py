import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import sys
import subprocess 

fig = None
ax1 = None
host = None
seconds = 0 
xar = []
yar = []

def usage():
    print("Usage: python3 main.py <hostname>")
    quit(1)

def ping(hostname):
    status, result = subprocess.getstatusoutput("ping -c1 " + str(hostname))

    if(status == 0):
        print("HOST IS UP")
        time_string = result.split("time=")[1]
        time = float(time_string.split(" ")[0])
        return time

    else:
        print("HOST IS DOWN")
        return -1

def animate(i):
    global seconds

    time = ping(host)
    yar.append(time)
    xar.append(seconds)
    ax1.clear()
    ax1.plot(xar,yar)
    
    seconds += 1

def main():
    global fig, ax1, host

    if(len(sys.argv) != 2):
        usage() 

    host = sys.argv[1]
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)

    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()

if __name__ == "__main__":
    main()
