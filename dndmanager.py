#!/usr/bin/env python3
# dndmanager.py
# Title: DnD Battle Manager
# Lead developer: Joel Harder
# Project start date: February 2020
#
# Template code: 
#   Submarine diving game
#   finalProject.py
#   by Joel Harder November 27, 2019

import pygame
import random
import shelve  # used to save game state files
from datetime import datetime

# initialize pygame
pygame.init()

displayInfo = pygame.display.Info()

screenWidth = int(round(displayInfo.current_h/1.107,-2))
screenHeight = int(round(displayInfo.current_h/1.107,-2))
window = pygame.display.set_mode((screenWidth,screenHeight)) 

pygame.display.set_caption("D&D Battle Manager")

# colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 25, 25)
green = (25, 255, 25)
blue = (25, 25, 255)
aqua = (0, 255, 255)
grey = (100, 100, 100)

mainMenuBack = (0, 162, 168)

scroll_y = 0

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 20)
fontL = pygame.font.Font('freesansbold.ttf', 35)
fontXL = pygame.font.Font('freesansbold.ttf', 50)

global gameOver
global gameLoop
# global mainMenu, loadGame
gameOver = False
gameLoop = False
mainMenu = True
# loadGame = False

gridNum = 25

prevPressed1 = False


class Sprite:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def render(self, img):
        img = pygame.transform.scale(img, (int(self.width), int(self.height)))
        window.blit(img, (self.x, self.y))


Char1 = Sprite(0, 0, 100, 100)
imgElf1 = pygame.image.load('img/icon-Elf1.png')

global spriteList
global imgList
spriteList = [Char1]
imgList = [imgElf1]
imgPathList = ['img/icon-Elf1.png']    # File path of the object's image file


def hoverDetection(x, y, w, h):
    global prevPressed1
    mouse = pygame.mouse.get_pos()
    pressed1,pressed2,pressed3 = pygame.mouse.get_pressed()
    
    if x <= mouse[0] <= x+w and y <= mouse[1] <= y+h:  # if hovering over with mouse
        return True
    else:
        return False

    prevPressed1 = pressed1


def gridLines(num):
    for i in range(0,screenWidth,int(screenWidth/num)):
        pygame.draw.rect(window, black, (i, 0, 1, screenHeight))

    for i in range(0,screenHeight,int(screenHeight/num)):
        pygame.draw.rect(window, black, (0, i, screenWidth, 1))


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
            
    else:  # zoom out
        if gridNum == 5:
            gridNum = 10
        elif gridNum == 10:
            gridNum = 25
        elif gridNum == 25:
            gridNum = 50
        elif gridNum == 50:
            print("Cannot zoom out any more")


def guiButton(message,x,y,w,h,isOn=False,isScroll=False): #message can be an img or string
    global scroll_y
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
        if isScroll and (y < 80 or y > 600):
            None #this doesnt display them if they go out of bounds
        else:
            message = pygame.transform.scale(message,(w,h))
            window.blit(message,(x,y))
            if x <= mouse[0] <= x+w and y <= mouse[1] <= y+h: #if hovering over with mouse
                return True
            else:
                return False


def guiText(string,x,y,f,centerX=False,centerY=False): #f is font (font,fontL,fontXL)
    string = f.render(string,True,black)
    rect = string.get_rect()
    txtBackground = pygame.image.load('img/txtBackground.png')
    txtBackground = pygame.transform.scale(txtBackground,(rect.width+10,rect.height+10))
    
    if centerX == True:
        x = (screenWidth/2)-(rect.width/2)
    if centerY == True:
        y = (screenHeight/2)-(rect.height/2)
    window.blit(txtBackground,(x-5,y-5))
    window.blit(string,(x,y))


def addChar(img, path):  # adds a new character (char)
    global spriteList
    global gridNum

    newSprite = Sprite(0, 0, screenWidth/gridNum, screenHeight/gridNum)
    spriteList.append(newSprite)
    imgList.append(img)
    imgPathList.append(path)


def GameLoop():
    # variable assignment (probably a more efficient way to import all but I couldnt find any)
    global gameLoop
    global gameOver
    global gridNum
    global spriteList
    global imgPathList
    global imgList
    global imgPathCollection
    global scroll_y
    global loadGame  # try this here

    # img v
    settingsIcon = pygame.image.load('img/settings.png')
    plusIcon = pygame.image.load('img/plusSign.png')
    minusIcon = pygame.image.load('img/minusSign.png')
    charAddIcon = pygame.image.load('img/charMenu.png')
    guiBackground = pygame.image.load('img/guiBackground.png')
    selectionOutline = pygame.image.load('img/selectionOutline.png')

    #imgElf1 = pygame.image.load('img/elf1.png')
    #imgElf2 = pygame.image.load('img/elf2.png')
    #imgElf3 = pygame.image.load('img/elf3.png')
    #imgDwarf1 = pygame.image.load('img/dwarf1.png')
    #imgDwarf2 = pygame.image.load('img/dwarf2.png')
    #imgLeprechaun1 = pygame.image.load('img/leprechaun1.png')
    #imgLeprechaun2 = pygame.image.load('img/leprechaun2.png')
    #imgOrc1 = pygame.image.load('img/orc1.png')
    #imgRanger1 = pygame.image.load('img/ranger1.png')
    #imgRanger2 = pygame.image.load('img/ranger2.png')
    #imgWitch1 = pygame.image.load('img/witch1.png')
    #imgWizard1 = pygame.image.load('img/wizard1.png')
    #imgWizard2 = pygame.image.load('img/wizard2.png')
    #imgDragon1 = pygame.image.load('img/dragon1.png')
    # imgPathCollection = ['img/elf1.png','img/elf2.png','img/elf3.png','img/dwarf1.png','img/dwarf2.png','img/leprechaun1.png',
    #                     'img/leprechaun2.png','img/orc1.png','img/ranger1.png','img/ranger2.png','img/witch1.png','img/wizard1.png',
    #                     'img/wizard2.png','img/dragon1.png','img/barbarian1.png','img/barbarian2.png','img/bard1.png']
    
    # Gather the icon file paths into a list
    # using the glob module, as it does pattern matching and expansion.
    # Reference https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
    import glob
    imgPathCollection = []  # List of all icon image file paths
    for file in glob.glob("img/icon-*"):
        imgPathCollection.append(file)
    # print(imgPathCollection)

    
    imgCollection = []
    for path in imgPathCollection:
        imgCollection.append(pygame.image.load(path))  # List of character images

    # img ^

    selectedObjNum = 0
    draggingObj = False
    selectingObj = False

    originPos = [0,0]
    dist = 0

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
    prevPressed3 = False

    if loadGame:
        stateFile = shelve.open('savegame/autosave')
        # load up variables from the shelve file into your game variables
        gridNum = stateFile['gridNum']
        spriteList = stateFile['spriteList']
        imgPathList = stateFile['imgPathList']
        imgList = []
        print(imgPathList[0])
        for path in imgPathList:
            print(path)
            imgList.append(pygame.image.load(path))
        stateFile.close()
    else:
        spriteList = [Char1]
    # End of variable assignment
    
    def AutoSave():
        stateFile = shelve.open('savegame/autosave')
        # save game variables into the shelve file
        stateFile['gridNum'] = gridNum
        stateFile['spriteList'] = spriteList
        stateFile['imgPathList'] = imgPathList
        stateFile.close()
        
    AUTOSAVEEVENT = pygame.USEREVENT+1  # Create a new timer id for AutoSave event
    pygame.time.set_timer(AUTOSAVEEVENT, 30000)  # trigger autosave every x ms
    
    while gameLoop:  # main loop
        mouse = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        for i in spriteList:
            spriteList[spriteList.index(i)].width = screenWidth/gridNum
            spriteList[spriteList.index(i)].height = screenHeight/gridNum
            spriteList[spriteList.index(i)].x = (screenWidth/gridNum) * round(spriteList[spriteList.index(i)].x/(screenWidth/gridNum))
            spriteList[spriteList.index(i)].y = (screenWidth/gridNum) * round(spriteList[spriteList.index(i)].y/(screenWidth/gridNum))
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                print('User quit game.')
                gameLoop = False  # pygame.quit()
            elif (event.type == AUTOSAVEEVENT):
                AutoSave()
                print('Autosaving...')
                print('Game state autosaved at ', datetime.now())
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    scroll_y = min(scroll_y + 15, 0)
                if event.button == 5:
                    scroll_y = max(scroll_y - 15, -600)

        window.fill(white)  # Clears the screen (put anything to display after this line)

        gridLines(gridNum)

        if pressed3 and not prevPressed3:
            selectingObj = False

        if snapBtnHover == False and settingsBtnHover == False and zoomInBtnHover == False and zoomOutBtnHover == False:
            for i in spriteList:  # this loop might cause lag with lots of characters????
                if pressed1 == True and prevPressed1 == False and hoverDetection(i.x,i.y,i.width,i.height) and selectingObj == False:
                    originPos = [int(i.x/(screenHeight/gridNum)),int(i.y/(screenHeight/gridNum))]
                    print(originPos)
                    selectedObjNum = spriteList.index(i)
                    draggingObj = True
                    print("here")
                if pressed3 == True and prevPressed3 == False and hoverDetection(i.x, i.y, i.width, i.height) and draggingObj == False:
                    originPos = [int(i.x/(screenWidth/gridNum)), int(i.y/(screenHeight/gridNum))]
                    selectedObjNum = spriteList.index(i)
                    selectingObj = True
                    
            if selectingObj:
                selectionOutline = pygame.transform.scale(selectionOutline, (int(spriteList[selectedObjNum].width),int(spriteList[selectedObjNum].height)))
                window.blit(selectionOutline,(int(spriteList[selectedObjNum].x), int(spriteList[selectedObjNum].y)))
                if abs(originPos[0]-int(mouse[0]/(screenHeight/gridNum))) >= abs(originPos[1]-int(mouse[1]/(screenHeight/gridNum))):
                    dist = abs(originPos[0]-int(mouse[0]/(screenHeight/gridNum)))*5
                else:
                    dist = abs(originPos[1]-int(mouse[1]/(screenHeight/gridNum)))*5

                pygame.draw.line(window, black,(originPos[0]*(screenWidth/gridNum)+spriteList[selectedObjNum].width/2, originPos[1]*(screenHeight/gridNum)+spriteList[selectedObjNum].height/2),(mouse[0], mouse[1]))
                guiText(str(dist)+' ft', 0, screenHeight-60,font, True)
                
            if pressed1 == True and prevPressed1 == True and draggingObj == True:
                if abs(originPos[0]-int(mouse[0]/(screenHeight/gridNum))) >= abs(originPos[1]-int(mouse[1]/(screenHeight/gridNum))):
                    dist = abs(originPos[0]-int(mouse[0]/(screenHeight/gridNum)))*5
                else:
                    dist = abs(originPos[1]-int(mouse[1]/(screenHeight/gridNum)))*5
                guiText(str(dist)+' ft',0,screenHeight-60,font,True)
                spriteList[selectedObjNum].x = mouse[0]-(spriteList[selectedObjNum].width/2)
                spriteList[selectedObjNum].y = mouse[1]-(spriteList[selectedObjNum].height/2)
                
            if pressed1 == False and prevPressed1 == True and draggingObj == True:
                if gridSnap == True:
                    spriteList[selectedObjNum].x = (screenWidth/gridNum) * round((mouse[0]-(spriteList[selectedObjNum].width/2))/(screenWidth/gridNum))
                    spriteList[selectedObjNum].y = (screenHeight/gridNum) * round((mouse[1]-(spriteList[selectedObjNum].height/2))/(screenHeight/gridNum))
                    draggingObj = False
                else:
                    spriteList[selectedObjNum].x = mouse[0]-(spriteList[selectedObjNum].width/2)
                    spriteList[selectedObjNum].y = mouse[1]-(spriteList[selectedObjNum].height/2)
                    draggingObj = False

        for i in spriteList:
            spriteList[spriteList.index(i)].render(imgList[spriteList.index(i)])

        # GUI v
        if guiButton(settingsIcon,5,screenHeight-65,60,60):  # opens/closes settings
            settingsBtnHover = True
            if pressed1 == False and prevPressed1 == True:
                if settingsGuiVisible:
                    settingsGuiVisible = False
                else:
                    settingsGuiVisible = True
                    print("opened settings")
        else:
            settingsBtnHover = False

        if settingsGuiVisible:  # only shows when settings are open
            if guiButton("Snap", 5, screenHeight-120, 100, 60, gridSnap) == True:  # text,x,y,w,h
                snapBtnHover = True
                if not pressed1 and prevPressed1:
                    if gridSnap:
                        gridSnap = False
                    else:
                        gridSnap = True
            else:
                snapBtnHover = False

        if charGuiVisible:
            guiBackground = pygame.transform.scale(guiBackground,(120,555))#plan on making each img 50x50 with 5 gap
            window.blit(guiBackground,(screenWidth-120,80))

            # add images to imgCollection to add them to this
            startX = screenWidth-115
            startY = 85
            for i in range(0,len(imgCollection)):
                if guiButton(imgCollection[i],startX,scroll_y+startY,50,50,False,True) and pressed1 == False and prevPressed1 == True:
                    #addChar(i)
                    addChar(imgCollection[i],imgPathCollection[i])
                if imgCollection.index(imgCollection[i])%2 == 0:
                    startX = screenWidth-65
                else:
                    startX = screenWidth-115
                    startY += 55
        
        if guiButton(charAddIcon,screenWidth-65,5,60,60):  # opens/closes character menu
            charBtnHover = True
            if pressed1 == False and prevPressed1 == True:
                if charGuiVisible == True:
                    charGuiVisible = False
                else:
                    charGuiVisible = True
                    print("opened character menu")
        else:
            charBtnHover = False
        

        if guiButton(plusIcon,screenWidth-30,screenHeight-60,25,25) == True:  # zoom in button
            zoomInBtnHover = True
            if pressed1 == False and prevPressed1 == True:
                zoom(1)  # 1 will zoom in -1 will zoom out
        else:
            zoomInBtnHover = False
        
        if guiButton(minusIcon,screenWidth-30,screenHeight-30,25,25) == True:  # zoom out button
            zoomOutBtnHover = True
            if pressed1 == False and prevPressed1 == True:
                zoom(-1) #1 will zoom in -1 will zoom out
        else:
            zoomOutBtnHover = False
        # GUI ^

        prevPressed1 = pressed1
        prevPressed3 = pressed3

        pygame.display.flip()
        clock.tick(50)

    titleScreen()


def titleScreen():
    global gameLoop
    global gameOver
    global mainMenu, loadGame

    mainMenu = True
    loadGame = False
    prevPressed1 = False

    while mainMenu:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()

        mouse = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        window.fill(mainMenuBack)

        titleTxt = fontXL.render('D&D Battle Manager', True, black)
        titleRect = titleTxt.get_rect()
        window.blit(titleTxt, (int((screenWidth/2)-(titleRect.width/2)), 25))

        # Play Buttonwindow
        if guiButton("Start New Game", (screenWidth/2)-100, (screenHeight/2)-200, 200, 100, True) and prevPressed1 and not pressed1: 
            mainMenu = False

        # Load Game Button
        if guiButton("Load Saved Game", (screenWidth/2)-100, (screenHeight/2)-50, 200, 100, True) and prevPressed1 and not pressed1:
            loadGame = True
            mainMenu = False

        # Quit Button
        if guiButton("Quit", (screenWidth/2)-100, (screenHeight/2)+100, 200, 100, True) and prevPressed1 and not pressed1:
            loadGame = False
            mainMenu = False
            return

        prevPressed1 = pressed1
        clock.tick(150)  # new testing delay
        pygame.display.flip()
        clock.tick(150)  # testing, was 50

    gameLoop = True
    gameOver = False
    GameLoop()


titleScreen()
pygame.display.quit()  # quit pygame window
pygame.quit() # end pygame

