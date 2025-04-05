import pgzrun
from pgzhelper import *

WIDTH=1280
HEIGHT=720

background_images=['platfromer', 'platformer', 'paltformer']
backgrounds = []

background=Actor(background_images[0])
background.x=0
background.y=360
backgrounds.append(background)
background1=Actor(background_images[1])
background1.x=1280
background1.y=360
backgrounds.append(background1)
background2=Actor(background_images[2])
background2.x=2560
background2.y=360
backgrounds.append(background1)

player=Actor('player')
player.x=400
player.y=500



def update():
    
    background.x-=4
    if background.x<-640:
        background.x+=2560
        
    background1.x-=4
    if background1.x<-640:
        background1.x+=2560
        
    background2.x-=4
    if background2.x<-640:
        background2.x+=2560        
        
def draw():
    background1.draw()
    background.draw()
    player.draw()

pgzrun.go()