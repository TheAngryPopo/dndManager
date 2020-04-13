#Joel Harder
#November 27, 2019
#finalProject.py
#Submarine diving game

import pygame
import random

#initialize pygame  
pygame.init()

screenWidth = 800
screenHeight = 600
window = pygame.display.set_mode((screenWidth,screenHeight)) 
  
pygame.display.set_caption("Submarine Dive")

#colours
black = (0,0,0) 
white = (255,255,255) 
red = (255,25,25)
green = (25,255,25)
blue = (25,25,255)

mainMenuBack = (0,162,168)
  
clock = pygame.time.Clock()

prevPressed1 = False

def hoverDetection(x,y,w,h):
    global prevPressed1
    mouse = pygame.mouse.get_pos()
    pressed1,pressed2,pressed3 = pygame.mouse.get_pressed()
    
    if x <= mouse[0] <= x+w and y <= mouse[1] <= y+h: #if hovering over with mouse
        return True
    else:
        return False

    prevPressed1 = pressed1

class Sprite:
    def __init__(self,x,y,width,height): 
        
        self.x=x
        self.y=y
        self.width=width
        self.height=height
  
    def render(self,moveX,moveY):
        global prevSubImg
        global fishSchoolImg
        global Sprite1
        global obstacles
        for i in obstacles:
            x1 = self.x
            y1 = self.y
            w1 = self.width
            h1 = self.height
            if(i.x+i.width>=x1>=i.x and i.y+i.height>=y1>=i.y): #top left of self touches
                if self.x <= i.x+(100-(abs(moveX)+1)):
                    self.y = i.y+i.height
                elif self.y <= i.y+(100-(abs(moveY)+1)):
                    self.x = i.x+self.width
            elif(i.x+i.width>=x1+w1>=i.x and i.y+i.height>=y1>=i.y): #top right of self touches
                if self.x >= i.x-(100-(abs(moveX)+1)-random.randint(1,5)):
                    self.y = i.y+i.height
                elif self.y <= i.y+(100-(abs(moveY)+1)):
                    self.x = i.x-self.width
            elif(i.x+i.width>=x1>=i.x and i.y+i.height>=y1+h1>=i.y): #bottom left of self touches
                if self.x <= i.x+(100-(abs(moveX)+1)):
                    self.y = i.y-self.height
                elif self.y <= i.y+(100-(abs(moveY)+1)):
                    self.x = i.x+self.width
            elif(i.x+i.width>=x1+w1>=i.x and i.y+i.height>=y1+h1>=i.y): #bottom right of self touches
                if self.x >= i.x-(100-(abs(moveX)+1)-random.randint(1,5)):
                    self.y = i.y-self.height
                elif self.y <= i.y+(100-(abs(moveY)+1)):
                    self.x = i.x-self.width

Sprite1 = Sprite(100,100,100,100)
Sprite2 = Sprite(500,500,100,100)

obstacles = {Sprite2}

font = pygame.font.Font('freesansbold.ttf', 20)
fontL = pygame.font.Font('freesansbold.ttf', 35)
fontXL = pygame.font.Font('freesansbold.ttf', 50)

gameOver = False
gameLoop = False
mainMenu = True

def GameLoop():
    #variable assignment (probably a more efficient way to import all but I couldnt find any)
    global gameLoop
    global gameOver
    global obsacles
    
    start_ticks = pygame.time.get_ticks()
    
    while gameLoop:
        for event in pygame.event.get():
            if (event.type==pygame.QUIT): 
                pygame.quit()
##            if gameOver == False:
##                if (event.type==pygame.KEYDOWN): #Movement
##                    if (event.key==pygame.K_LEFT):
##                        moveX = -playerSpeed
##                        left = True
##                    if (event.key==pygame.K_RIGHT): 
##                        moveX = playerSpeed
##                        right = True
##                    if (event.key==pygame.K_UP): 
##                        moveY = -playerSpeed
##                        up = True
##                    if (event.key==pygame.K_DOWN): 
##                        moveY = playerSpeed
##                        down = True
##            if (event.type==pygame.KEYUP): 
##                if (event.key==pygame.K_LEFT):
##                    moveX=0
##                    left = False
##                if (event.key==pygame.K_RIGHT): 
##                    moveX=0
##                    right = False
##                if (event.key==pygame.K_UP): 
##                    moveY=0
##                    up = False
##                if (event.key==pygame.K_DOWN): 
##                    moveY=0
##                    down = False


        

        window.fill(white)
        
        #collisions = detectCollisions(Sprite1.x,Sprite1.y,Sprite1.width,Sprite1.height)#,Sprite2.x,Sprite2.y,Sprite2.width,Sprite2.height

        Sprite1.render(100,100)
        
        clock.tick(50)

    titleScreen()

def titleScreen():
    global gameLoop
    global gameOver
    global mainMenu
    
    mainMenu = True
    prevPressed1 = False
    
    while mainMenu:
        for event in pygame.event.get():
            if (event.type==pygame.QUIT): 
                pygame.quit()
        
        mouse = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        window.fill(mainMenuBack)

        titleTxt = fontXL.render('D&D Battle Manager',True,black)
        titleRect = titleTxt.get_rect()
        window.blit(titleTxt,(int((screenWidth/2)-(titleRect.width/2)),25))
        
        #Play Button
        if hoverDetection((screenWidth/2)-100,(screenHeight/2)-200,200,100) == True: #if hovering over with mouse
            pygame.draw.rect(window,green,(int(screenWidth/2-100),int(screenHeight/2-200),200,100))
            playBtnTxt = fontL.render('Start',True,black)
            playBtnRect = playBtnTxt.get_rect()
            window.blit(playBtnTxt,(int((screenWidth/2)-(playBtnRect.width/2)),int(screenHeight/2-170)))
            if prevPressed1 == True and pressed1 == False:
                mainMenu = False
        else:
            pygame.draw.rect(window,white,(int((screenWidth/2)-100),int((screenHeight/2)-200),200,100))
            playBtnTxt = fontL.render('Start',True,black)
            playBtnRect = playBtnTxt.get_rect()
            window.blit(playBtnTxt,(int((screenWidth/2)-(playBtnRect.width/2)),int(screenHeight/2-170)))
        
        prevPressed1 = pressed1

        pygame.display.flip()
        clock.tick(50)
        
    gameLoop = True
    gameOver = False
    GameLoop()

titleScreen()
