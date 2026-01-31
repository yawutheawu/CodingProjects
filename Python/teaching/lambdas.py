import random as rand

def x():
    print("I am function x")
    
x()

(lambda x: print("I am lambda with no name, with value", x))(rand.randrange(1, 100))

sortList = [["John", 25], ["Alice", 30], ["Bob", 20], ["Diana", 35], ["Charlie", 28], ["Eve", 22], ["Frank", 27], ["Grace", 24], ["Hank", 29], ["Ivy", 23]]
