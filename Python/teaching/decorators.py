import time

def timerDec(func):
    def wrapper(x):
        startTime = time.time()
        func(x)
        print(f"Took {round(time.time() - startTime,2)} seconds to run")
    return wrapper

@timerDec
def greet(x):
    print(x)

greet("Yo")

@timerDec
def factorial(x):
    output = x
    counter = x-1
    while counter > 0:
        output *= counter
        counter -= 1
    print(output)

factorial(1500)

@timerDec
def wait(x):
    time.sleep(x)
    print(f"Waited {x} seconds")


def passinDec(func):
    def wrapper(x):
        y = x * 2
        return func(x,y)
    return wrapper

@passinDec
def z(x,y=0):
    print(x,y)

z(5)

time.sleep(5)