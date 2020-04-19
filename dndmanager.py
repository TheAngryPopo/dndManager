#Joel Harder
#November 27, 2019
#finalProject.py
#Submarine diving game

import pygame
import random

#initialize pygame  
pygame.init()

displayInfo = pygame.display.Info()

screenWidth = int(round(displayInfo.current_h/1.107,-2))
screenHeight = int(round(displayInfo.current_h/1.107,-2))
window = pygame.display.set_mode((screenWidth,screenHeight)) 
  
pygame.display.set_caption("D&D Battle Manager")

#colours
black = (0,0,0) 
white = (255,255,255) 
red = (255,25,25)
green = (25,255,25)
blue = (25,25,255)
aqua = (0,255,255)
grey = (100,100,100)

mainMenuBack = (0,162,168)

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 20)
fontL = pygame.font.Font('freesansbold.ttf', 35)
fontXL = pygame.font.Font('freesansbold.ttf', 50)

gameOver = False
gameLoop = False
mainMenu = True

gridNum = 25

prevPressed1 = False

class Sprite:
    def __init__(self,x,y,width,height): 
        
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    
    def render(self,img):
        img = pygame.transform.scale(img, (int(self.width),int(self.height)))
        window.blit(img,(self.x,self.y))

Char1 = Sprite(0,0,100,100)

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

def zoom(direction): #direction: 1 will zoom in -1 will zoom out
    global gridNum
    
    if direction > 0: #zoom in
        if gridNum == 5:
            print("Cannot zoom in any more")
        elif gridNum == 10:
            gridNum = 5
        elif gridNum == 25:
            gridNum = 10
        elif gridNum == 50:
            gridNum = 25
            
    else: #zoom out
        if gridNum == 5:
            gridNum = 10
        elif gridNum == 10:
            gridNum = 25
        elif gridNum == 25:
            gridNum = 50
        elif gridNum == 50:
            print("Cannot zoom out any more")

def guiButton(message,x,y,w,h,isOn=False): #message can be an img or string
    mouse = pygame.mouse.get_pos()

    if type(message) == str:
        if x <= mouse[0] <= x+w and y <= mouse[1] <= y+h: #if hovering over with mouse
            pygame.draw.rect(window,aqua,(x,y,w,h))
            message = font.render(message,True,black)
            messageRect = message.get_rect()
            window.blit(message,(int((x+w/2)-(messageRect.width/2)),int((y+h/2)-messageRect.height/2)))
            return True
        else:
            pygame.draw.rect(window,green if isOn else red,(x,y,w,h))  # if item is enabled make green and if off show as red
            message = font.render(message,True,black)
            messageRect = message.get_rect()
            window.blit(message,(int((x+w/2)-(messageRect.width/2)),int((y+h/2)-messageRect.height/2)))
            return False
    else:
        message = pygame.transform.scale(message,(w,h))
        window.blit(message,(x,y))
        if x <= mouse[0] <= x+w and y <= mouse[1] <= y+h: #if hovering over with mouse
            return True
        else:
            return False

def GameLoop():
    #variable assignment (probably a more efficient way to import all but I couldnt find any)
    global gameLoop
    global gameOver
    global gridNum

    settingsIcon = pygame.image.load('settings.png')
    plusIcon = pygame.image.load('plusSign.png')
    minusIcon = pygame.image.load('minusSign.png')
    charAddIcon = pygame.image.load('charMenu.png')
    imgElf1 = pygame.image.load('img/icons8-elf-50.png')

    objList = [Char1]
    selectedObjNum = 0
    draggingObj = False
    
    gridSnap = True

    snapBtnHover = False
    settingsBtnHover = False
    zoomInBtnHover = False
    zoomOutBtnHover = False
    charBtnHover = False

    settingsGuiVisible = False
    charGuiVisible = False
    
    start_ticks = pygame.time.get_ticks()
    prevPressed1 = False
    #End of variable assignment
    
    while gameLoop: #main loop
        mouse = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        Char1.width=screenWidth/gridNum
        Char1.height=screenHeight/gridNum
        
        for event in pygame.event.get():
            if (event.type==pygame.QUIT): 
                pygame.quit()
        
        window.fill(white) #Clears the screen (put anything to display after this line)
        
        gridLines(gridNum)

        if snapBtnHover == False and settingsBtnHover == False and zoomInBtnHover == False and zoomOutBtnHover == False:
            for i in objList:
                if pressed1 == True and prevPressed1 == False and hoverDetection(i.x,i.y,i.width,i.height):
                    selectedObjNum = objList.index(i)
                    draggingObj = True
            
            if pressed1 == True and prevPressed1 == True and draggingObj == True:
                objList[selectedObjNum].x = mouse[0]-(Char1.width/2)
                objList[selectedObjNum].y = mouse[1]-(Char1.height/2)
                
            if pressed1 == False and prevPressed1 == True and draggingObj == True:
                if gridSnap == True:
                    objList[selectedObjNum].x = (screenWidth/gridNum) * round((mouse[0]-(objList[selectedObjNum].width/2))/(screenWidth/gridNum))
                    objList[selectedObjNum].y = (screenHeight/gridNum) * round((mouse[1]-(objList[selectedObjNum].height/2))/(screenHeight/gridNum))
                    draggingObj = False
                else:
                    objList[selectedObjNum].x = mouse[0]-(objList[selectedObjNum].width/2)
                    objList[selectedObjNum].y = mouse[1]-(objList[selectedObjNum].height/2)
                    draggingObj = False
                    
        #selectImgResized = cv2.resize(selectedImg, (Char1.width,Char1.length))
        
        Char1.render(imgElf1)



        
        #GUI v
        if guiButton(settingsIcon,5,screenHeight-65,60,60): #opens/closes settings
            settingsBtnHover = True
            if pressed1 == False and prevPressed1 == True:
                if settingsGuiVisible == True:
                    settingsGuiVisible = False
                else:
                    settingsGuiVisible = True
                    print("opened settings")
        else:
            settingsBtnHover = False

        if settingsGuiVisible == True: #only shows when settings are open
            if guiButton("Snap",5,screenHeight-120,100,60,gridSnap) == True:#text,x,y,w,h
                snapBtnHover = True
                if pressed1 == False and prevPressed1 == True:
                    if gridSnap == True:
                        gridSnap = False
                    else:
                        gridSnap = True
            else:
                snapBtnHover = False


        if charGuiVisible:
            pygame.draw.rect(window,grey,(()))
        
        if guiButton(charAddIcon,screenWidth-65,5,60,60): #opens/closes character menu
            charBtnHover = True
            if pressed1 == False and prevPressed1 == True:
                if charGuiVisible == True:
                    charGuiVisible = False
                else:
                    charGuiVisible = True
                    print("opened character menu")
        else:
            charBtnHover = False
        

        if guiButton(plusIcon,screenWidth-30,screenHeight-60,25,25) == True: #zoom in button
            zoomInBtnHover = True
            if pressed1 == False and prevPressed1 == True:
                zoom(1) #1 will zoom in -1 will zoom out
        else:
            zoomInBtnHover = False
        
        if guiButton(minusIcon,screenWidth-30,screenHeight-30,25,25) == True: #zoom out button
            zoomOutBtnHover = True
            if pressed1 == False and prevPressed1 == True:
                zoom(-1) #1 will zoom in -1 will zoom out
        else:
            zoomOutBtnHover = False
        #GUI ^


        
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
