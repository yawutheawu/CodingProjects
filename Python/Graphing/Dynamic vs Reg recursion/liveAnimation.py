import itertools
import time
import matplotlib.pyplot as plt
import math
import numpy as np

import matplotlib.animation as animation

class TimeoutError(Exception):
    pass

def FibonacciMemo(n,memo={0:1,1:1}):
    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = FibonacciMemo(n-1,memo) + FibonacciMemo(n-2,memo)
        return memo[n]

def FibonacciRec(n):
    if n == 1 or n == 0 :
        return 1
    else:
        return FibonacciRec(n-1) + FibonacciRec(n-2)

def timeTakenRecorder(case,whichOne):
    if whichOne == "M":
        floatStart = time.process_time()
        nanoSecondStart = time.process_time_ns()
        FibonacciMemo(case)
        floatEnd = time.process_time()
        nanoSecondEnd = time.process_time_ns()
        return [floatEnd - floatStart,nanoSecondEnd - nanoSecondStart]
    else:
        floatStart = time.process_time()
        nanoSecondStart = time.process_time_ns()
        FibonacciRec(case)
        floatEnd = time.process_time()
        nanoSecondEnd = time.process_time_ns()
        return [floatEnd - floatStart,nanoSecondEnd - nanoSecondStart]


def data_gen():
    for cnt in itertools.count():
        t = math.floor(cnt / 10)
        yield t, [timeTakenRecorder(t,"M"),timeTakenRecorder(t,"R")]


def init():
    ax.set_ylim(-1, 5)
    ax.set_xlim(-1, 10)
    del xdata[:]
    del ydata1[:]
    del ydata2[:]
    line1.set_data(xdata, ydata1)
    line2.set_data(xdata, ydata2)
    return line1, line2,

fig, ax = plt.subplots()
line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata1,ydata2 = [],[],[]


def run(data):
    mode = 1 #0/1 for float or NS
    # update the data
    t, listDat = data
    y1, y2 = listDat
    y1 = y1[mode]
    y2 = y2[mode]
    xdata.append(t)
    ydata1.append(y1)
    ydata2.append(y2)
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    if t >= xmax:
        ax.set_xlim(xmin, max(xdata)*1.1)
        ax.figure.canvas.draw()
    if y1 >= ymax or y2 >= ymax:
        bigVal = max(max(ydata1)*1.1,max(ydata2)*1.1)
        ax.set_ylim(ymin, bigVal)
        ax.figure.canvas.draw()
    line1.set_data(xdata, ydata1)
    line2.set_data(xdata, ydata2)

    return line1, line2,

# Only save last 100 frames, but run forever
ani = animation.FuncAnimation(fig, run, data_gen, interval=1, init_func=init,
                              save_count=1000)
plt.show()
