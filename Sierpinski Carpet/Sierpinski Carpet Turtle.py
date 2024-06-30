from turtle import Turtle
from random import random
import math

t = Turtle()
t.screen.title('sierpinski carpet')
xSize = 300
ySize = 300
resolution = 1
t.screen.screensize(xSize*2,ySize*2)
def square(sideLength):
    t.up()
    t.seth(0)
    t.backward(sideLength/2)
    t.left(90)
    t.forward(sideLength/2)
    t.right(90)
    t.down()
    for i in range(4):
        t.forward(sideLength)
        t.right(90)
    t.up()
    t.forward(sideLength/2)
    t.right(90)
    t.forward(sideLength/2)
    t.left(90)

def Carpet(topLeft,bottomRight):
    #topLeft: (-900,900)
    #bottomRight: (900,-900)
    #End Condition: abs(topLeft[0]) + abs(bottomRight[0]) < resolution
    if (abs(topLeft[0])!=topLeft[0]) and (abs(bottomRight[0])!= bottomRight[0]):
        size = abs(topLeft[0]-bottomRight[0])/3
    elif (abs(topLeft[0])==topLeft[0]) and (abs(bottomRight[0])== bottomRight[0]):
        size = abs(topLeft[0]-bottomRight[0])/3
    else:
        size = (abs(topLeft[0])+abs(bottomRight[0]))/3
    t.up()
    t.setheading(0)
    t.goto((topLeft[0]+bottomRight[0])/2,
           (topLeft[1]+bottomRight[1])/2)
    if size < resolution:
        t.up()
        t.setpos((topLeft[0]+bottomRight[0])/2,(topLeft[1]+bottomRight[1])/2)
        square(size)
    else:
        t.up()
        t.setpos((topLeft[0]+bottomRight[0])/2,(topLeft[1]+bottomRight[1])/2)
        square(size)
        #Top Row
        Carpet(topLeft,
               (topLeft[0]+size,topLeft[1]-size))
        Carpet(
            (topLeft[0]+size,topLeft[1]),
               (topLeft[0]+(size*2),topLeft[1]-size))
        Carpet(
            (topLeft[0]+(size*2),topLeft[1]),
               (topLeft[0]+(size*3),topLeft[1]-size))
        #Middle Row
        Carpet(
            (topLeft[0],topLeft[1]-size),
            (topLeft[0]+size,topLeft[1]-(size*2)))
        Carpet(
            (topLeft[0]+(size*2),topLeft[1]-size),
            (topLeft[0]+(size*3),topLeft[1]-(size*2)))
        #Bottom Row
        Carpet(
            (topLeft[0],topLeft[1]-(size*2)),
            (topLeft[0]+size,topLeft[1]-(size*3)))
        Carpet(
            (topLeft[0]+size,topLeft[1]-(size*2)),
            (topLeft[0]+(size*2),topLeft[1]-(size*3)))
        Carpet(
            (topLeft[0]+(size*2),topLeft[1]-(size*2)),
            (topLeft[0]+(size*3),topLeft[1]-(size*3)))

Carpet((-xSize,xSize),
       (ySize,-ySize))

t.screen.mainloop()
