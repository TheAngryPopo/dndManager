#Joel Harder
#November 27, 2019
#finalProject.py
#Submarine diving game

import pygame
import random

#initialize pygame  
pygame.init()

screenWidth = 1000
screenHeight = 1000
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

font = pygame.font.Font('freesansbold.ttf', 20)
fontL = pygame.font.Font('freesansbold.ttf', 35)
fontXL = pygame.font.Font('freesansbold.ttf', 50)

gameOver = False
gameLoop = False
mainMenu = True

prevPressed1 = False

class Sprite:
    def __init__(self,x,y,width,height): 
        
        self.x=x
        self.y=y
        self.width=width
        self.height=height
  
    def render(self):
        global prevSubImg
        global fishSchoolImg
        
        pygame.draw.rect(window,black,(self.x,self.y,self.width,self.height))

Sprite1 = Sprite(100,100,100,100)

def hoverDetection(x,y,w,h):
    global prevPressed1
    mouse = pygame.mouse.get_pos()
    pressed1,pressed2,pressed3 = pygame.mouse.get_pressed()
    
    if x <= mouse[0] <= x+w and y <= mouse[1] <= y+h: #if hovering over with mouse
        return True
    else:
        return False

    prevPressed1 = pressed1

def gridLines(num):
    for i in range(0,screenWidth,int(screenWidth/num)):
        pygame.draw.rect(window,black,(i,0,1,screenHeight))

    for i in range(0,screenHeight,int(screenHeight/num)):
        pygame.draw.rect(window,black,(0,i,screenWidth,1))

def guiButton(text,x,y,w,h):
    mouse = pygame.mouse.get_pos()

    if x <= mouse[0] <= x+w and y <= mouse[1] <= y+h: #if hovering over with mouse
        pygame.draw.rect(window,green,(x,y,w,h))
        text = font.render(text,True,black)
        textRect = text.get_rect()
        window.blit(text,(int((x+w/2)-(textRect.width/2)),int(40-textRect.height/2)))
        return True
    else:
        pygame.draw.rect(window,red,(x,y,w,h))
        text = font.render(text,True,black)
        textRect = text.get_rect()
        window.blit(text,(int((x+w/2)-(textRect.width/2)),int(40-textRect.height/2)))
        return False

def GameLoop():
    #variable assignment (probably a more efficient way to import all but I couldnt find any)
    global gameLoop
    global gameOver
    gridSnap = True
    gridNum = 25
    
    Sprite1.width=screenWidth/gridNum
    Sprite1.height=screenHeight/gridNum
    
    start_ticks = pygame.time.get_ticks()
    prevPressed1 = False
    
    while gameLoop:
        mouse = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():
            if (event.type==pygame.QUIT): 
                pygame.quit()
        
        window.fill(white)
        if guiButton("Snap",screenWidth-110,10,100,60) == True:#text,x,y,w,h
            if pressed1 == False and prevPressed1 == True:
                if gridSnap == True:
                    gridSnap = False
                else:
                    gridSnap = True
        
        gridLines(gridNum)

        if gridSnap == True:
            if pressed1 == False and prevPressed1 == True:
                Sprite1.x = (screenWidth/gridNum) * round((mouse[0]-(Sprite1.width/2))/(screenWidth/gridNum))
                Sprite1.y = (screenHeight/gridNum) * round((mouse[1]-(Sprite1.height/2))/(screenHeight/gridNum))
        else:
            if pressed1 == False and prevPressed1 == True:
                Sprite1.x = mouse[0]-(Sprite1.width/2)
                Sprite1.y = mouse[1]-(Sprite1.height/2)
        
        Sprite1.render()

        prevPressed1 = pressed1
        
        pygame.display.flip()
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
