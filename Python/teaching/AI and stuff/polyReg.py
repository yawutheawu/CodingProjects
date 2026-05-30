import numpy as np
import matplotlib.pyplot as plt

datapoints = 100
# theoryM = 1.5
# theoryB = 10

# randUpper = 100
# randLower = -100

# \sin\left(\frac{1000}{x}\right)\cdot x

rng = np.random.default_rng()

x = [x for x in range(1,datapoints+1)]
y = [rng.normal(loc=5*np.log(x), scale=2.0, size=None) for x in range(1,datapoints+1)]
mymodel = np.poly1d(np.polyfit(x, y, 3))

myline = np.linspace(1, datapoints, 100 * datapoints)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline), color='red')
plt.show()