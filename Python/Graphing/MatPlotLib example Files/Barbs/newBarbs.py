"""
=================
barbs(X, Y, U, V)
=================
Plot a 2D field of wind barbs.

See `~matplotlib.axes.Axes.barbs`.
"""
import matplotlib.pyplot as plt
import random as r
import numpy as np

plt.style.use('_mpl-gallery-nogrid')
DIMENSIONS = [10,60]
# make data:
rng = np.random.default_rng()
X, Y = np.meshgrid([i for i in range(1,DIMENSIONS[0]+1)], [i for i in range(1,DIMENSIONS[1]+1)])
vals = rng.normal(32,50,size=(len(Y), len(Y[0])))
vals = np.where(vals<0,360-vals,vals)
angle = np.pi / 180 *vals
newVals = rng.normal(17,8,size=(len(Y), len(Y[0])))
amplitude = np.abs(newVals)
U = amplitude * np.sin(angle)
V = amplitude * np.cos(angle)
# plot:
fig, ax = plt.subplots()

ax.barbs(X, Y, U, V, barbcolor='C0', flagcolor='C0', length=7, linewidth=1.5)
ax.set(xlim=(-7, len(X[0])+7), ylim=(-7, len(Y)+7))

plt.show()
