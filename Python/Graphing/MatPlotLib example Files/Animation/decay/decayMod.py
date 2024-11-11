"""
=====
Decay
=====

This example showcases:

- using a generator to drive an animation,
- changing axes limits during an animation.

Output generated via `matplotlib.animation.Animation.to_jshtml`.
"""

import itertools

import matplotlib.pyplot as plt
import numpy as np

import matplotlib.animation as animation


def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)


def init():
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []


def run(data):
    # update the data
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    ymin, ymax = ax.get_ylim()
    if t >= xmax:
        if len(xdata) >= 15:
            ax.set_xlim(min(xdata[-5:]), max(xdata[-5:])+min(xdata[-5:]))
        if len(ydata) >= 20:
            if max(ydata[-20:]) <= ymax/2 or min(ydata[-20:]) >= ymin/2:
                ax.set_ylim(min(ydata[-20:]), max(ydata[-20:]))
        ax.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,

# Only save last 100 frames, but run forever
ani = animation.FuncAnimation(fig, run, data_gen, interval=1, init_func=init,
                              save_count=1000)
plt.show()
