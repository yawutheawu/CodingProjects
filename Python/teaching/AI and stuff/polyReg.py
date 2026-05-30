import numpy as np
import matplotlib.pyplot as plt

datapoints = 1000

rng = np.random.default_rng()

x = [x for x in range(1,datapoints+1)]
y = [rng.normal(loc=5*np.log(x), scale=2.0, size=None) for x in range(1,datapoints+1)]

mymodel = np.poly1d(np.polyfit(x, y, 2))

myline = np.linspace(1, datapoints, 100 * datapoints)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline), color='red')
plt.show()