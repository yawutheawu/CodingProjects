import matplotlib.pyplot as plt
import numpy as np
import random as r
import scipy

datapoints = 2500
theoryM = 1.5
theoryB = 10

randUpper = 100
randLower = -100

rng = np.random.default_rng()


x = [x for x in range(datapoints)]
y = [rng.normal(loc=theoryM * x + theoryB, scale=1000.0, size=None) for x in range(datapoints)]
#y = [r.randrange(randLower, randUpper) for x in range(datapoints)]

linRegression = scipy.stats.linregress(x, y)

m = linRegression.slope
b = linRegression.intercept

print(f"y = {m}x + {b}")

def predict(x):
    return m * x + b

plt.scatter(x, y)
plt.plot(x, list(map(predict, x)), color='red')
plt.show()