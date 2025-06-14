from tkinter.constants import CENTER
from turtle import Turtle
import random as r
import time
import math

t = Turtle()
t.speed(25)
t.screen.title('Turtle Testing')
t.screen.colormode(255)
xSize = 300
ySize = 300
resolution = 5
t.screen.screensize(xSize*2,ySize*2)

def square(centerX:int = 0,
           centerY:int = 0,
           size:int = 50,
           lineColor:tuple = (0,0,0),
           fillColor:tuple = (255,255,255),
           lineWidth:int = 1):
    t.penup()
    t.setpos(centerX,centerY)
    t.pendown()
    t.color(lineColor)
    t.fillcolor(fillColor)
    t.width(lineWidth)
    t.penup()
    t.forward(size/2)
    t.left(90)
    t.forward(size/2)
    t.left(90)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
square(r.randint(-xSize,xSize),
       r.randint(-ySize,ySize),
       200,
       (r.randint(0,255),r.randint(0,255),r.randint(0,255)),
       (r.randint(0,255),r.randint(0,255),r.randint(0,255)),
       r.randint(1,10))
square(r.randint(-xSize,xSize),
       r.randint(-ySize,ySize),
       300,
       (r.randint(0,255),r.randint(0,255),r.randint(0,255)),
       (r.randint(0,255),r.randint(0,255),r.randint(0,255)),
       r.randint(1,10))
square(r.randint(-xSize,xSize),
       r.randint(-ySize,ySize),
       150,
       (r.randint(0,255),r.randint(0,255),r.randint(0,255)),
       (r.randint(0,255),r.randint(0,255),r.randint(0,255)),
       r.randint(1,10))
for i in range(25):
    tringlePos = (r.randint(-xSize,xSize),r.randint(-xSize,xSize))
    tringleBottomLen = r.randint(0,100)
    t.penup()
    t.width(r.randint(1,10))
    t.color((r.randint(0,255),r.randint(0,255),r.randint(0,255)),(r.randint(0,255),r.randint(0,255),r.randint(0,255)))
    t.setpos(tringlePos[0],tringlePos[1])
    t.seth(0)
    t.pendown()
    t.begin_fill()
    t.shape("turtle")
    t.forward(tringleBottomLen/2)
    t.left(180)
    t.forward(tringleBottomLen)
    t.setpos(tringlePos[0],tringleBottomLen)
    t.setpos(tringlePos[0] + tringleBottomLen/2,tringlePos[1])
    t.end_fill()


t.screen.mainloop()