import pgzrun, random

WIDTH = 1024
HEIGHT = 1024

images = ['uncolored_castle.png', 'uncolored_desert.png',
          'uncolored_forest.png', 'uncolored_hills.png']

background1 = Actor(random.choice(images))
background1.topleft = 0, 0
background2 = Actor(random.choice(images))
background2.topleft = WIDTH, 0

backgrounds = [background1, background2]

def update():
    for bg in backgrounds:
        bg.x -= 2
        if bg.right < 2:
            bg.right += 2 * WIDTH
            bg.image = random.choice(images)
        
def draw():
    screen.fill((128, 0, 0))
    for bg in backgrounds:
        bg.draw()

pgzrun.go()
