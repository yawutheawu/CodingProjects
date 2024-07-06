import pygame
from pygame.locals import QUIT, K_LEFT, K_RIGHT, K_SPACE, KEYDOWN
from random import randint
import sys, time




FPS = 60 # frames per second
ACC = 0.5
FRIC = -0.12
GRAV = 0.5
SCREEN_SIZE = (WIDTH, HEIGHT) = (400, 450)

PLAYER_SPEED = 5

PLAYER_COLOR = (40, 127, 152)
RED = (180, 40, 49)
BLACK = (0, 0, 0)


score = 0

pygame.init()
Vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill(PLAYER_COLOR)
        self.rect = self.surf.get_rect(center = (10, 360))
        self.pos = Vec((10, 360))
        self.vel = Vec(0, 0)
        self.acc = Vec(0, 0)
        
    def move(self): 
        
        self.acc = Vec(0, 0)
        
        self.acc.y = GRAV
        
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x -= ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x += ACC
            
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        if self.pos.x > WIDTH + 15:
            self.pos.x = -15
        if self.pos.x < -15 :
            self.pos.x = WIDTH + 15
            
        self.rect.midbottom = self.pos

    def update(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if self.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0
                
    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -15
        
class Platform(pygame.sprite.Sprite):
    
    def __init__(self, floor=False):
        super().__init__()
        if floor:
            self.surf = pygame.Surface((WIDTH, 12))
            self.surf.fill(RED)
            self.rect = self.surf.get_rect()
            self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT-10))
        else:
            self.surf = pygame.Surface((randint(50, 100), 12))
            self.surf.fill(RED)
            self.rect = self.surf.get_rect()
            self.rect = self.surf.get_rect(center = (randint(0, WIDTH-10), (randint(0,HEIGHT-30))))

# ---------- Main code -----------=


clock = pygame.time.Clock()

displaysurface = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Blocky Jump')
floor = Platform(floor=True)
player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(floor)
platforms = pygame.sprite.Group()
platforms.add(floor)

for i in range(randint(5, 6)):
    pl = Platform()
    platforms.add(pl)
    all_sprites.add(pl)

# Game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.jump()
        
    
    
    displaysurface.fill(BLACK)
    
    player.update()
    
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        
    player.move()
# update the display and wait until next tick
    pygame.display.update()
    clock.tick(FPS)