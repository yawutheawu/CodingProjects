import pygame
import os
import random
global loseflag, winflag

pygame.init()

Gameboard = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]

pygame.font.init()
loseflag = False
winflag = False
font=pygame.font.SysFont('Comic Sans MS',50)

height = 286
width = 286

clock = pygame.time.Clock()
screen=pygame.display.set_mode((width, height))

counter = 2


colors = {}
while counter<=2048:
    colors[str(counter)]=(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    counter = counter*2

def checkblocks(grid,x1,y1,x2,y2):
    if grid[y1][x1]==grid[y2][x2]:
        return True
    else:
        return False
    
def mergeblocks(grid,x1,y1,x2,y2):
    grid[y2][x2]=grid[y2][x2]+grid[y1][x1]
    
def move(grid,direction):
    global loseflag
    if direction=='UP':
        for i in range(1,len(grid)):
            for j in range(0,len(grid[i])):
                lookback=0
                flag=True
                while (i-(lookback+1)>=0) and flag:
                    if grid[i-lookback][j]==grid[i-(lookback+1)][j]:
                        mergeblocks(grid,j,i-lookback,j,i-(lookback+1))
                        grid[i-lookback][j]=0
                        flag = False
                    elif grid[i-(lookback+1)][j]==0:
                        grid[i-(lookback+1)][j]=grid[i-lookback][j]
                        grid[i-lookback][j]=0
                    lookback+=1
                    
    if direction=='DOWN':
        for i in range(len(grid)-2,-1,-1):
            for j in range(0,len(grid[i])):
                lookback=0
                flag=True
                while (i+(lookback+1)<=(len(grid)-1)) and flag:
                    if grid[i+lookback][j]==grid[i+(lookback+1)][j]:
                        mergeblocks(grid,j,i+lookback,j,i+(lookback+1))
                        grid[i+lookback][j]=0
                        flag = False
                    elif grid[i+(lookback+1)][j]==0:
                        grid[i+(lookback+1)][j]=grid[i+lookback][j]
                        grid[i+lookback][j]=0
                    lookback+=1
    if direction=='RIGHT':
        for i in range(0,len(grid)):
            for j in range(len(grid[i])-2,-1,-1):
                lookback=0
                flag=True
                while (j+(lookback+1)<=len(grid)-1) and flag:
                    if grid[i][j+lookback]==grid[i][j+(lookback+1)]:
                        mergeblocks(grid,j+lookback,i,j+(lookback+1),i)
                        grid[i][j+lookback]=0
                        flag = False
                    elif grid[i][j+(lookback+1)]==0:
                        grid[i][j+(lookback+1)]=grid[i][j+lookback]
                        grid[i][j+lookback]=0
                    lookback+=1
    if direction=='LEFT':
        for i in range(0,len(grid)):
            for j in range(1,len(grid[i])):
                lookback=0
                flag=True
                while (j-(lookback+1)>=0) and flag:
                    if grid[i][j-(lookback)]==grid[i][j-(lookback+1)]:
                        mergeblocks(grid,j-lookback,i,j-(lookback+1),i)
                        grid[i][j-(lookback)]=0
                        flag = False
                    elif grid[i][j-(lookback+1)]==0:
                        grid[i][j-(lookback+1)]=grid[i][j-(lookback)]
                        grid[i][j-(lookback)]=0
                    lookback+=1
    emptyflag = False
    loseflag = True
    for i in Gameboard:
        for j in i:
            if j==0:
                loseflag=False
    while not emptyflag and not loseflag:
        Randx = random.randrange(0,len(Gameboard[0]))
        Randy = random.randrange(0,len(Gameboard))
        if Gameboard[Randy][Randx]==0:
            Gameboard[Randy][Randx]=2
            emptyflag = True
        
    
def addblock(grid):
    twoadded=False
    for i in grid:
        for j in range(0,len(i)):
            if i[j]==0 and not twoadded:
                i[j]=2
                twoadded = True
os.chdir('images')
background = pygame.image.load('2048bg.jpg')
addblock (Gameboard)
shifty=67
shiftx=67
shiftytxt=67
shiftxtxt=67
print(Gameboard)
while True:
    keys = pygame.key.get_pressed()
    screen.blit(background,(0,0))
    for i in range(0,len(Gameboard)):
        for j in range(0,len(Gameboard[i])):
            if Gameboard[i][j]>0:

                pygame.draw.rect(screen,colors[str(Gameboard[i][j])],pygame.Rect(14+(shiftx*j),14+(shifty*i),56,56))
                Font=pygame.font.SysFont('arial',30)
                text=Font.render(str(Gameboard[i][j]),True,(0,0,0))
                screen.blit(text,(33+(shiftxtxt*j),25+(shiftytxt*i)))
    events = pygame.event.get()
    for event in events:
        if event.type==pygame.KEYDOWN and (not loseflag and not winflag):
            if event.key==pygame.K_LEFT:
                move(Gameboard,'LEFT')
            if event.key==pygame.K_RIGHT:
                move(Gameboard,'RIGHT')
            if event.key==pygame.K_DOWN:
                move(Gameboard,'DOWN')
            if event.key==pygame.K_UP:
                move(Gameboard,'UP')
                
    for i in Gameboard:
        for j in i:
            if j==2048:
                winflag = True
    if winflag == True:
        text=font.render("You Win!", False, (255,0,0))
        screen.blit(text,(width/6, height/3))
    if loseflag == True:
        text=font.render("You Lose!", False, (255,0,0))
        screen.blit(text,(width/6, height/3))

    pygame.display.update()