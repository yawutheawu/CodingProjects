import matplotlib.pyplot as plt
import numpy as np
import pandas

datapoints = 10000
windowMin = -100
windowMax = 100
deltaX = (abs(windowMax) + abs(windowMin))/datapoints
a = 125
b= 1
c = 12

plt.style.use('_mpl-gallery')
x = [windowMin]
y = []

# ax^2 + bx + c

for i in range(1,datapoints+1):
    temp = a*((x[i-1])**2)+b*(x[i-1])+c
    y.append(temp)
    x.append(round(x[i-1]+deltaX,10))

x.remove(-1)

fig, ax = plt.subplots()

ax.plot(x,y, linewidth=2.0)
plt.show()
