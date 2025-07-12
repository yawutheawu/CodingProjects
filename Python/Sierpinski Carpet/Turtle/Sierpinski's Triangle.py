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
resolution = 30
TriSize = 500
t.screen.screensize(xSize*2,ySize*2)

def draw_sierpinski(length):
    if length<resolution:
        for i in range(0,3):
            t.fd(length)
            t.left(120)
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