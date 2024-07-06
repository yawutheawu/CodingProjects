import matplotlib.pyplot as plt
import numpy as np
import pandas

def fib(n):
    x=[0,1]
    if n <= 0:
        return []
    elif n == 1:
        return [x[0]]
    elif n ==2:
        return x[0:2]
    else:
        for i in range(1,n):
            x.append(x[i-1]+x[i])
        return x
def fibR(n):
    if n in (1,2):
        return 1
    elif n == 0:
        return 0
    else:
        return fibR(n-2)+fibR(n-1)

def addNumbers(n):
    if n == 0:
        return 0
    else:
        return n + addNumbers(n-1)
def addNumbersLoop(n):
    x = 0
    for i in range(0,n+1):
        x+=i
    return x
def addNumberGauss(start,stop,step):
    dist = (start+stop)/step
    if start == 0:
        dist += 1
    else:
        pass
    return (start+stop)*(dist/2)

plt.style.use('_mpl-gallery')

fig, ax = plt.subplots()

ax.plot(range(0,1001),fib(1000), linewidth=2.0)
plt.show()
