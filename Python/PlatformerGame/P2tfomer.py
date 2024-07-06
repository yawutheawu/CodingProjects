import pgzrun
import random
from pgzhelper import *
import os
import time
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,0)


WIDTH=1280
HEIGHT=720

spacing=520
timer=time.time()*1000
score = 0
scoredelay = 1600
lose = 0

touched = True

background_images=['background1-720', 'background2-720', 'background3-720']
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
backgrounds.append(background2)
lose=Actor('lose')
lose.x=0
lose.y=0

player=Actor('player')
player.x=400
player.y=200

plat=Actor('p0')
plat.x=0
plat.y=700

plat1=Actor('p1')
plat1.x=1200
plat1.y=400

plat2=Actor('p2')
plat2.x=plat1.x+spacing
plat2.y=500

plat3=Actor('p3')
plat3.x=plat2.x+spacing
plat3.y=350

plat4=Actor('p4')
plat4.x=plat3.x+spacing
plat4.y=300

plat5=Actor('p5')
plat5.x=plat4.x+spacing
plat5.y=500

platforms = [plat, plat1, plat2, plat3, plat4, plat5]
counter = 1

jump = False

accy = 200

upperbound = 250

lowerbound = -250

def update():
    if player.y<1000:
        
        global jump, counter, touched, score, timer, scoredelay, lose
        
        if keyboard.up:
            jump=True
        
        plat.x-=4
        if plat.x<-1000:
            pass
        plat1.x-=4
        if plat1.x<-640:
            plat1.x+=2560
            plat1.y=plat5.y+random.randrange(lowerbound,upperbound)
            if plat1.y>720:
                plat1.y=700
            if plat1.y<0:
                plat1.y=100
        plat2.x-=4
        if plat2.x<-640:
            plat2.x+=2560
            plat2.y=plat1.y+random.randrange(lowerbound,upperbound)
            if plat2.y>720:
                plat2.y=700
            if plat2.y<0:
                plat2.y=100
        plat3.x-=4
        if plat3.x<-640:
            plat3.x+=2560
            plat3.y=plat2.y+random.randrange(lowerbound,upperbound)
            if plat3.y>720:
                plat3.y=700
            if plat3.y<0:
                plat3.y=100
        plat4.x-=4
        if plat4.x<-640:
            plat4.x+=2560
            plat4.y=plat3.y+random.randrange(lowerbound,upperbound)
            if plat4.y>720:
                plat4.y=700
            if plat4.y<0:
                plat4.y=100
        plat5.x-=4
        if plat5.x<-640:
            plat5.x+=2560
            plat5.y=plat4.y+random.randrange(lowerbound,upperbound)
            if plat5.y>720:
                plat5.y=700
            if plat5.y<0:
                plat5.y=100
            
        if (player.bottom<=plat.top+15 and player.colliderect(plat)) or (player.bottom<=plat1.top+15 and player.colliderect(plat1)) or (player.bottom<=plat2.top+15 and player.colliderect(plat2)) or (player.bottom<=plat3.top+15 and player.colliderect(plat3)) or (player.bottom<=plat4.top+15 and player.colliderect(plat4)) or (player.bottom<=plat5.top+15 and player.colliderect(plat5)):
            if not touched:
                touched=True
                timer=time.time()*1000
                score+=1
        else:
            player.y+=10
        
        for p in platforms:
            if (player.bottom <= p.top + 15 and player.colliderect(plat)):
                print(player.bottom, p.top)
        if touched:
            if timer+scoredelay<time.time()*1000:
                touched=False
            
        if (jump and counter <= 100):
            player.y -= accy / (counter * 1.5)
            counter += 1  
        else:
            jump = False
            counter = 1
        
        for bg in backgrounds:
            bg.x-=4
            if bg.x<-640:
                bg.x+=2560
    else:
        lose=1


def draw():
    global lose
    background1.draw()
    background.draw()
    for p in platforms:
        p.draw()
    player.draw()
    screen.draw.text('score: '+str(score), color='light blue', topleft=(0,0))
    if lose==1:
        screen.draw.text("GAME OVER", center=(WIDTH/2, HEIGHT/2), color="orange", fontsize=100)
    


pgzrun.go()