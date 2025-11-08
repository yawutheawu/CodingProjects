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
resolution = 3

startCol = (250,40,5)
endCol = (0,250,120)

t.screen.screensize(xSize*2,ySize*2)
def Triangle(Size, triangles=0, max = 500,startColor = (255,255,255),endColor = (0,0,0)):
    step = ((endColor[0]-startColor[0])/max, (endColor[1]-startColor[1])/max, (endColor[2]-startColor[2])/max)
    if Size < resolution:
        pass
    else:
        t.color(((round(startColor[0] + (step[0]*(triangles+1)))),round((startColor[1] + (step[1]*(triangles+1)))),round((startColor[2] + (step[2]*(triangles+1))))))
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
        Triangle(Size/1.2,triangles+1,max,startColor,endColor)

triangles = 0
size = ((xSize*2) * (ySize*2)) * 5
     
while size > resolution:
        triangles += 1
        size /= 1.2

Triangle(((xSize*2) * (ySize*2)) * 5,0,triangles,startCol,endCol)
t.penup()
t.goto(((xSize*2) * (ySize*2)) * 5,((xSize*2) * (ySize*2)) * 5)
t.screen.mainloop()