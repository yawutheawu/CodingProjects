from tkinter.constants import CENTER
from turtle import Turtle
import random as r
import time
import math

t = Turtle()
t.speed(0)
t.screen.title('Triangle Tunnel')
t.screen.colormode(255)
xSize = 300
ySize = 300
resolution = 5
t.screen.screensize(xSize*2,ySize*2)

def Triangle(Size):
    if Size < resolution:
        pass
    else:
        t.color((r.randint(0,255), r.randint(0,255), r.randint(0,255)))
        t.penup()
        t.goto(0,0)
        side = (2/3) * (3 **(3/4)) * math.sqrt(Size)
        t.seth(90)
        t.back(((math.sqrt(3)/2) * side)/2)
        t.seth(0)
        t.forward(side/2)
        t.seth(180)
        t.begin_fill()
        t.pendown()
        t.forward(side)
        t.right(120)
        t.forward(side)
        t.right(120)
        t.forward(side)
        t.end_fill()
        t.penup()
        t.goto(0,0)
        Triangle(Size/1.2)
Triangle(9000000)
t.screen.mainloop()