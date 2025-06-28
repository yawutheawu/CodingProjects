from tkinter.constants import CENTER
from turtle import Turtle
import random as r
import time
import math

t = Turtle()
t.speed(0)
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
    
def triangle(tringlePos:tuple = (0,0),tringleBottomLen:int = 10, width:int = 5,color:tuple = (150,150,150)):
       t.penup()
       t.width(width)
       t.color(color)
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
'''
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
''' 

cols = 10
square(0,0,xSize*ySize,(0,0,0),(0,0,0),1)

SideInc = (t.screen.window_width())/cols
lineWidth = 1

#Top left
#square(-t.screen.window_width()/2,t.screen.window_height()/2)
#Bottom Right
#square(t.screen.window_width()/2,-t.screen.window_height()/2)
#Top Right
#square(t.screen.window_width()/2,t.screen.window_height()/2)
#Bottom Left
#square(-t.screen.window_width()/2,-t.screen.window_height()/2)
#Center:
#square(0,0)
t.color(255,255,255)
for i in range(0,cols+1):
       t.penup()
       t.setpos(-t.screen.window_width()/2,(t.screen.window_height()/2) - (SideInc * i))
       t.pendown()
       t.setpos(t.screen.window_width()/2,(t.screen.window_height()/2) - (SideInc * i))
for i in range(0,cols+1):
       t.penup()
       t.setpos((-t.screen.window_width()/2) + (SideInc * i),t.screen.window_height()/2)
       t.pendown()
       t.setpos((-t.screen.window_width()/2) + (SideInc * i),(-t.screen.window_height()/2)-(SideInc/1.7))
print("done")
t.screen.mainloop()