import random as rand

def x():
    print("I am function x")
    
x()

(lambda x: print("I am lambda with no name, with value", x))(rand.randrange(1, 100))