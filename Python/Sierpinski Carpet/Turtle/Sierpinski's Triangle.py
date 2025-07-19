from tkinter.constants import CENTER
from turtle import Turtle
import random as r
import time
import math

t = Turtle()
t.speed(0)
t.screen.title('Triangle maxxing')
t.screen.colormode(255)
xSize = 300
ySize = 300
resolution = 50
TriSize = 750
t.screen.screensize(xSize*2,ySize*2)

def getColor(x,y):
    # -TriSize/2 to TriSize/2
    # -(((3**(1/2)) / 2) * TriSize)/2 to (((3**(1/2)) / 2) * TriSize)/2
    xScale = min(max(abs(x)/(TriSize/2),0),1)
    yScale = min(max(abs(y)/((((3**(1/2)) / 2) * TriSize)/2),0),1)
    r = 255 - int(min(max(255 * xScale,0),100))
    b = int(min(max(255 * yScale,100),255))
    g = 255 - int(min(max(255 * ((r+b)/(255*2)),55),150))
    print(r,g,b, f"{(r+g+b)/(255*3)}")
    return (r,g,b)

def draw_sierpinski(length):
    if length<resolution:
        t.color(getColor(t.pos()[0], t.pos()[1]))
        t.begin_fill()
        t.down()
        for i in range(0,3):
            t.fd(length)
            t.left(120)
        t.end_fill()
        t.up()
    else:
        draw_sierpinski(length/2)
        t.fd(length/2)
        draw_sierpinski(length/2)
        t.bk(length/2)
        t.left(60)
        t.fd(length/2)
        t.right(60)
        draw_sierpinski(length/2)
        t.left(60)
        t.bk(length/2)
        t.right(60)


t.up()
t.goto(-TriSize/2, -(((3**(1/2)) / 2) * TriSize)/2)
t.down()
draw_sierpinski(TriSize)
t.up()
t.goto(0, 0)
t.screen.mainloop()