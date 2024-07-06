import pgzrun
from pgzhelper import *
import random

WIDTH=800
HEIGHT=600

player=Actor('player')
player.x=400
player.y=500

bullets=[]

bullet_delay=0


background_images=['background1','background2','background3']
backgrounds=[]

background=Actor(random.choice(background_images))
background.x=400
background.y=300
backgrounds.append(background)
background=Actor(random.choice(background_images))
background.x=400
background.y=-300
backgrounds.append(background)

enemies=[]

explosions=[]

enemy_bullets=[]

powerups=[]
powerup_images=['powerup1','powerup2','powerup3']

def update():
    global bullet_delay
    if keyboard.right:
        player.x+=5
    if keyboard.left:
        player.x-=5
    if keyboard.up:
        player.y-=5
    if keyboard.down:
        player.y+=5
    if player.x<25:
        player.x=25
    if player.x>775:
        player.x=775
    if player.y<25:
        player.y=25
    if player.y>575:
        player.y=575
    if keyboard.space and bullet_delay==0:
        bullet_delay=5
        bullet=Actor('player_bullet')
        bullet.x=player.x
        bullet.y=player.y
        bullet.angle=90
        bullets.append(bullet)
    if bullet_delay>0:
        bullet_delay-=1
    for bullet in bullets:
        bullet.move_forward(15)
    for background in backgrounds:
        background.y+=3
        if background.y>900:
            background.y-=1200
            background.image=random.choice(background_images)
    if random.randint(0,1000)>950:
        enemy=Actor('enemy1_1')
        enemy.images=['enemy1_1','enemy1_2']
        enemy.fps=5
        enemy.y-50
        enemy.x=random.randint(100,700)
        enemy.direction=random.randint(-100,-80)
        enemies.append(enemy)
    for enemy in enemies:
        enemy.move_in_direction(4)
        enemy.animate()
        if enemy.y>700:
            enemies.remove(enemy)
    for bullet in bullets:
        hit=bullet.collidelist(enemies)
        if hit !=-1:
            bullets.remove(bullet)
            explosion=Actor('explosion1')
            explosion.x=enemies[hit].x
            explosion.y=enemies[hit].y
            explosion.images=['explosion1','explosion2']
            explosion.fps=8
            explosion.life=15
            explosions.append(explosion)
            enemies.remove(enemies[hit])
                           
    for explosion in explosions:
        explosion.animate()
        explosion.life-=1
        if explosion.life==0:
            explosions.remove(explosion)
            
    if random.randint(0,1000)>990:
        bullet=Actor('enemy_bullet')
        bullet.x=enemy.x
        bullet.y=enemy.y
        bullet.angle=random.randint(0,359)
        enemy_bullets.append(bullet)
    for bullet in enemy_bullets:
        bullet.move_forward(5)
        if bullet.x<0 or bullet.x>800 or bullet.y<0 or bullet.y>600:
           enemy_bullets.remove(bullet)
    
    if random.randint(0,1000)>998:
        powerup=Actor('powerup1')
        powerup.y=-50
        powerup.x=random.randint(100,700)
        powerups.append(powerup)
    for powerup in powerups:
        powerup.y+=4
    for powerup in powerups:
        hit=powerup.collidelist(bullets)
        if hit !=-1:
            powerup.y-=40
            powerup.image=random.choice(powerup_images)
            bullets.remove(bullets[hit])
    hit=player.collidelist(powerups)
    if hit !=-1:
        powerups.remove(powerups[hit])
        
def draw():
    for background in backgrounds:
        background.draw()
    player.draw()
    for powerup in powerups:
        powerup.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for explosion in explosions:
        explosion.draw()
    for bullet in enemy_bullets:
        bullet.draw()
    
pgzrun.go()