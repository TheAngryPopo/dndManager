#Joel Harder
#November 27, 2019
#finalProject.py
#Submarine diving game

# MadeEyePopo made this entry!!!!

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

depth1 = (23, 178, 235)
depth2 = (14, 136, 181)
depth3 = (17, 118, 207)
depth4 = (12, 87, 153)
depth5 = (0, 48, 120)
depth6 = (0, 20, 51)

depthColour = (depth1,depth2,depth3,depth4,depth5,depth6)
  
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
    
def detectCollisions(x1,y1,w1,h1):#,x2,y2,w2,h2
    global obstacles
    for i in obstacles:
        if(i.x+i.width>=x1>=i.x and i.y+i.height>=y1>=i.y):
            return True
        elif(i.x+i.width>=x1+w1>=i.x and i.y+i.height>=y1>=i.y):
            return True
        elif(i.x+i.width>=x1>=i.x and i.y+i.height>=y1+h1>=i.y):
            return True
        elif(i.x+i.width>=x1+w1>=i.x and i.y+i.height>=y1+h1>=i.y):
            return True
    return False

#sprite class ???
class Sprite:
    def __init__(self,x,y,width,height): 
        
        self.x=x
        self.y=y
        self.width=width
        self.height=height
  
    def render(self,collision,moveX,moveY):
        global prevSubImg
        global fishSchoolImg
        global Sprite1
        if(collision==True):
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
            if self == Sprite1:
                if moveX < 0 and moveX != 0:
                    window.blit(subImg,(int(self.x),int(self.y)))
                    prevSubImg = subImg
                elif moveX > 0 and moveX != 0:
                    window.blit(subImgFlip,(int(self.x),int(self.y)))
                    prevSubImg = subImgFlip
                else:
                    window.blit(prevSubImg,(int(self.x),int(self.y)))
        else:
            if self == Sprite1:
                if moveX < 0 and moveX != 0:
                    window.blit(subImg,(int(self.x),int(self.y)))
                    prevSubImg = subImg
                elif moveX > 0 and moveX != 0:
                    window.blit(subImgFlip,(int(self.x),int(self.y)))
                    prevSubImg = subImgFlip
                else:
                    window.blit(prevSubImg,(int(self.x),int(self.y)))
            else:
                window.blit(fishSchoolImg,(int(self.x),int(self.y)))

#Arrow Keys:
arrowLeftOff = pygame.image.load('arrowLeftOff.png')
arrowRightOff = pygame.image.load('arrowRightOff.png')
arrowUpOff = pygame.image.load('arrowUpOff.png')
arrowDownOff = pygame.image.load('arrowDownOff.png')

arrowLeftOn = pygame.image.load('arrowLeftOn.png')
arrowRightOn = pygame.image.load('arrowRightOn.png')
arrowUpOn = pygame.image.load('arrowUpOn.png')
arrowDownOn = pygame.image.load('arrowDownOn.png')

arrowLeftOff = pygame.transform.scale(arrowLeftOff,(50,50))
arrowRightOff = pygame.transform.scale(arrowRightOff,(50,50))
arrowUpOff = pygame.transform.scale(arrowUpOff,(50,50))
arrowDownOff = pygame.transform.scale(arrowDownOff,(50,50))

arrowLeftOn = pygame.transform.scale(arrowLeftOn,(50,50))
arrowRightOn = pygame.transform.scale(arrowRightOn,(50,50))
arrowUpOn = pygame.transform.scale(arrowUpOn,(50,50))
arrowDownOn = pygame.transform.scale(arrowDownOn,(50,50))
#End of Arrow Keys

#Sprites:
Sprite1 = Sprite(100,50,100,60)
MovingObstacle1 = Sprite(800,random.randint(0,500),100,100)
MovingObstacle2 = Sprite(800,random.randint(500,1000),100,100)
MovingObstacle3 = Sprite(800,random.randint(1000,1500),100,100)
chase = Sprite(random.randint(0,700),random.randint(1000,1500),100,100)
#End of Sprites

#Images:
heart = pygame.image.load('heart.png')
heart = pygame.transform.scale(heart,(25,25))
emptyHeart = pygame.image.load('emptyHeart.png')
emptyHeart = pygame.transform.scale(emptyHeart,(25,25))

fishImg = pygame.image.load('fish.png')

fishSchoolImg = pygame.image.load('fishSchool.png')
fishSchoolImg = pygame.transform.scale(fishSchoolImg,(MovingObstacle1.width,MovingObstacle1.height))

guiBackground = pygame.image.load('guiBackground.png')
guiBackground = pygame.transform.scale(guiBackground,(screenWidth-25,75))
guiBackground = pygame.transform.flip(guiBackground,False,True)

subImg = pygame.image.load('submarine.png')
subImg = pygame.transform.scale(subImg,(Sprite1.width,Sprite1.height))
subImgFlip = pygame.transform.flip(subImg,True,False)
subImgDown = pygame.transform.flip(subImg,True,True)
prevSubImg = pygame.transform.flip(subImg,False,False)

coinImg = pygame.image.load('coin.png')
coinImg = pygame.transform.scale(coinImg,(30,25))
#End of Images

font = pygame.font.Font('freesansbold.ttf', 20)
fontL = pygame.font.Font('freesansbold.ttf', 35)
fontXL = pygame.font.Font('freesansbold.ttf', 50)

totalCoins = 0

playerSpeed = 5

obstacles = (MovingObstacle1,MovingObstacle2,MovingObstacle3,chase)

timeLength = 60 #max length in seconds of round

maxHealth = 3

#Upgrade Costs:
speedUpCost = 50
healthUpCost = 250
timeUpCost = 50
#End of Upgrade Costs

gameOver = False
gameLoop = False
mainMenu = True

def GameLoop():
    #variable assignment (probably a more efficient way to import all but I couldnt find any)
    global gameLoop
    global gameOver
    global obstacles
    global fishImg
    global fishSchoolImg
    global subImg
    global Sprite1
    global MovingObstacle1
    global MovingObstacle2
    global MovingObstacle3
    global chase
    global totalCoins
    global playerSpeed
    global timeLength
    global maxHealth
    
    start_ticks = pygame.time.get_ticks()
    
    Sprite1 = Sprite(100,50,100,60)
    MovingObstacle1 = Sprite(800,random.randint(0,500),100,100)
    MovingObstacle2 = Sprite(800,random.randint(500,1000),100,100)
    MovingObstacle3 = Sprite(800,random.randint(1000,1500),100,100)
    chase = Sprite(random.randint(0,700),random.randint(1000,1500),100,100)

    obstacles = (MovingObstacle1,MovingObstacle2,MovingObstacle3,chase)

    fishImg = pygame.transform.scale(fishImg,(MovingObstacle1.width,MovingObstacle1.height))
    fishSchoolImg = pygame.transform.scale(fishSchoolImg,(MovingObstacle1.width,MovingObstacle1.height))

    subImg = pygame.transform.scale(subImg,(Sprite1.width,Sprite1.height))
    subImgFlip = pygame.transform.flip(subImg,True,False)
    subImgDown = pygame.transform.flip(subImg,True,True)
    prevSubImg = pygame.transform.flip(subImg,False,False)
    
    moveX,moveY=0,0

    depth = 0
    maxDepth = int(depth/25)*playerSpeed*timeLength

    ObstacleX1 = 800
    ObstacleX2 = random.randint(100,800)
    ObstacleX3 = random.randint(100,800)
    ObstacleXSpeed1 = random.randint(1,5)
    ObstacleXSpeed2 = random.randint(1,5)
    ObstacleXSpeed3 = random.randint(1,5)

    TimerBar = Sprite(220,10,425,50)
    seconds = 0
    timerBarWidth = 425
    
    prevCollisions = False
    
    #Arrow Keys
    left = False
    right = False
    up = False
    down = False
    #End of Arrow Keys
    
    health = maxHealth

    prevPressed1 = False

    curCoins = 0

    addCoins = True

    underwaterBackground = pygame.image.load('underwaterBackground.png')
    underwaterBackground2 = pygame.image.load('underwaterBackground2.png')
    underwaterBackground3 = pygame.transform.rotate(underwaterBackground2,180)

    reverseBackground = True

    underwaterBackground = pygame.transform.scale(underwaterBackground,(screenWidth,int((underwaterBackground.get_rect()).height*(screenWidth/(underwaterBackground.get_rect()).width))))
    underwaterBackground2 = pygame.transform.scale(underwaterBackground2,(screenWidth,int((underwaterBackground2.get_rect()).height*(screenWidth/(underwaterBackground2.get_rect()).width))))
    underwaterBackground3 = pygame.transform.scale(underwaterBackground3,(screenWidth,int((underwaterBackground3.get_rect()).height*(screenWidth/(underwaterBackground3.get_rect()).width))))
    
    underwaterBackgroundY = 0
    underwaterBackground2Y = underwaterBackground.get_rect().height + underwaterBackground3.get_rect().height
    underwaterBackground3Y = underwaterBackground.get_rect().height
    #end of variable assignment
    
    while gameLoop:
        
        for event in pygame.event.get():
            if (event.type==pygame.QUIT): 
                pygame.quit()
            if gameOver == False:
                if (event.type==pygame.KEYDOWN): #Movement
                    if (event.key==pygame.K_LEFT):
                        moveX = -playerSpeed
                        left = True
                    if (event.key==pygame.K_RIGHT): 
                        moveX = playerSpeed
                        right = True
                    if (event.key==pygame.K_UP): 
                        moveY = -playerSpeed
                        up = True
                    if (event.key==pygame.K_DOWN): 
                        moveY = playerSpeed
                        down = True
            if (event.type==pygame.KEYUP): 
                if (event.key==pygame.K_LEFT):
                    moveX=0
                    left = False
                if (event.key==pygame.K_RIGHT): 
                    moveX=0
                    right = False
                if (event.key==pygame.K_UP): 
                    moveY=0
                    up = False
                if (event.key==pygame.K_DOWN): 
                    moveY=0
                    down = False


        
        #clears everything and sets background
        underwaterBackground = pygame.transform.scale(underwaterBackground,(screenWidth,int((underwaterBackground.get_rect()).height*(screenWidth/(underwaterBackground.get_rect()).width))))
        underwaterBackground2 = pygame.transform.scale(underwaterBackground2,(screenWidth,int((underwaterBackground2.get_rect()).height*(screenWidth/(underwaterBackground2.get_rect()).width))))
        underwaterBackground3 = pygame.transform.scale(underwaterBackground3,(screenWidth,int((underwaterBackground3.get_rect()).height*(screenWidth/(underwaterBackground3.get_rect()).width))))
        
        window.fill(white)
        
        window.blit(underwaterBackground,(0,underwaterBackgroundY))
        window.blit(underwaterBackground2,(0,underwaterBackground2Y))
        window.blit(underwaterBackground3,(0,underwaterBackground3Y))
        #window.blit(underwaterBackground,(0,-int(depth/25)))

        if moveY > 0 and Sprite1.y == 400:
            underwaterBackgroundY -= int(playerSpeed/5)
            underwaterBackground2Y -= int(playerSpeed/5)
            underwaterBackground3Y -= int(playerSpeed/5)

        if underwaterBackground2Y <= -(underwaterBackground2.get_rect().height):
            underwaterBackground2Y += underwaterBackground3.get_rect().height + underwaterBackground2.get_rect().height

        if underwaterBackground3Y <= -(underwaterBackground3.get_rect().height):
            underwaterBackground3Y += underwaterBackground3.get_rect().height + underwaterBackground2.get_rect().height
        
        #for i in range(0,maxDepth,underwaterBackground2.get_rect().height):
        #if depth in range(0,maxDepth,underwaterBackground2.get_rect().height):
##        if reverseBackground == True:
##           window.blit(underwaterBackground2,(0,-int(depth/25)+depth))
##           reverseBackground = False
##        else:
##            window.blit(underwaterBackground3,(0,-int(depth/25)+depth))
##            reverseBackground = True
        
        Sprite1.x+=moveX
        Sprite1.y+=moveY
        
        #Keeps it on the screen
        if Sprite1.x>=675:
            Sprite1.x=675
        if Sprite1.x<=25:
            Sprite1.x=25
        if Sprite1.y<=75:
            Sprite1.y=75
        if Sprite1.y>=400:
            Sprite1.y=400
            for i in obstacles: #moves screen down
                if moveY > 0 and gameOver == False:
                    if (i == MovingObstacle1 or i == MovingObstacle2 or i == MovingObstacle3) and i.y <= -i.height:
                        i.y = screenHeight+random.randint(600,1000)
                        i.x = random.randint(100,700)
                    else:
                        i.y -= int(playerSpeed/4)
                    depth += int(playerSpeed/4)

        #moving obstacles v
        if ObstacleX1 != -100:
            ObstacleX1 -= ObstacleXSpeed1
        else:
            ObstacleX1 = 800

        if ObstacleX2 != -100:
            ObstacleX2 -= ObstacleXSpeed2
        else:
            ObstacleX2 = 800
            
        if ObstacleX3 != -100:
            ObstacleX3 -= ObstacleXSpeed3
        else:
            ObstacleX3 = 800
        
        MovingObstacle1.x = ObstacleX1
        MovingObstacle2.x = ObstacleX2
        MovingObstacle3.x = ObstacleX3
        #moving obstacles ^
        
        #use if you want it to keep up and get faster with time: (chase.x-Sprite1.x)/int(((timeLength/5)+100))
        if chase.x > Sprite1.x:
            chase.x -= (chase.x-Sprite1.x-50)/100
        elif chase.x < Sprite1.x:
            chase.x += (Sprite1.x-chase.x-50)/100

        if chase.y > Sprite1.y:
            chase.y -= (chase.y-Sprite1.y-50)/100
        elif chase.y < Sprite1.y:
            chase.y += (Sprite1.y-chase.y-50)/100
        
        collisions=detectCollisions(Sprite1.x,Sprite1.y,Sprite1.width,Sprite1.height)#,Sprite2.x,Sprite2.y,Sprite2.width,Sprite2.height
        
        MovingObstacle1.render(False,moveX,moveY)
        MovingObstacle2.render(False,moveX,moveY)
        MovingObstacle3.render(False,moveX,moveY)
        chase.render(False,moveX,moveY)

        Sprite1.render(collisions,moveX,moveY)

        #pygame.draw.rect(window,green,(0,0,screenWidth,75))
        window.blit(guiBackground,(25,0))
        
        if collisions == True and prevCollisions == False:
            health -= 1
        
        if health <= 0:
            window.blit(emptyHeart,(675,35))
            window.blit(emptyHeart,(705,35))
            window.blit(emptyHeart,(735,35))
            if maxHealth == 4:
                window.blit(emptyHeart,(765,35))
            gameOver = True
            moveY = 0
            moveX = 0
        elif health == 1 and gameOver == False:
            window.blit(heart,(675,35))
            window.blit(emptyHeart,(705,35))
            window.blit(emptyHeart,(735,35))
            if maxHealth == 4:
                window.blit(emptyHeart,(765,35))
        elif health == 2 and gameOver == False:
            window.blit(heart,(675,35))
            window.blit(heart,(705,35))
            window.blit(emptyHeart,(735,35))
            if maxHealth == 4:
                window.blit(emptyHeart,(765,35))
        elif health == 3 and gameOver == False:
            window.blit(heart,(675,35))
            window.blit(heart,(705,35))
            window.blit(heart,(735,35))
            if maxHealth == 4:
                window.blit(emptyHeart,(765,35))
        elif health == 4 and gameOver == False:
            window.blit(heart,(675,35))
            window.blit(heart,(705,35))
            window.blit(heart,(735,35))
            window.blit(heart,(765,35))
        
        prevCollisions = collisions

        #Timer Bar v
        pygame.draw.rect(window,green,(TimerBar.x,TimerBar.y,int(timerBarWidth),TimerBar.height))
        
        test = (425/timeLength)/(1000/clock.get_time())
        
        if seconds <= timeLength:
            if gameOver == False:
                seconds=(pygame.time.get_ticks()-start_ticks)/1000
                timerBarWidth -= (425/timeLength)/(1000/clock.get_time())
                #print(TimerBar.width)
        else:
            gameOver = True
        #Timer Bar ^

        timeText = font.render('Time Left:',True,white)
        timeText2 = font.render(str(int(timeLength-seconds)),True,white)
        depthText = font.render('Depth: '+str(int(depth/25))+'m',True,white)
        depthRect = depthText.get_rect()
        window.blit(timeText,(110,10))
        window.blit(timeText2,(160,30))
        window.blit(depthText,(int(screenWidth-(depthRect.width+10)),10))

        #Displaying Arrow Keys:
        if left == True:
            window.blit(arrowLeftOn,(screenWidth-165,screenHeight-55))
        else:
            window.blit(arrowLeftOff,(screenWidth-165,screenHeight-55))

        if right == True:
            window.blit(arrowRightOn,(screenWidth-55,screenHeight-55))
        else:
            window.blit(arrowRightOff,(screenWidth-55,screenHeight-55))

        if up == True:
            window.blit(arrowUpOn,(screenWidth-110,screenHeight-110))
        else:
            window.blit(arrowUpOff,(screenWidth-110,screenHeight-110))

        if down == True:
            window.blit(arrowDownOn,(screenWidth-110,screenHeight-55))
        else:
            window.blit(arrowDownOff,(screenWidth-110,screenHeight-55))
        #End of Displaying Arrow Keys
        
        if gameOver == True:
            curCoins = int(abs((depth*(health+1)/100)))
            if addCoins:
                totalCoins += curCoins
                addCoins = False
            gameOverTxt1 = font.render('Game Over',True,white)
            gameOverTxt2 = font.render('Coins: '+str(curCoins),True,white)
            gameOverRect1 = gameOverTxt1.get_rect()
            gameOverRect2 = gameOverTxt2.get_rect()
            window.blit(gameOverTxt1,(int((screenWidth/2)-(gameOverRect1.width/2)),200))
            window.blit(gameOverTxt2,(int((screenWidth/2)-(gameOverRect2.width/2)),220))

            mouse = pygame.mouse.get_pos()
            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            
            if (screenWidth/2)-100 <= mouse[0] <= (screenWidth/2)+100 and (screenHeight/2)-50 <= mouse[1] <= (screenHeight/2)+50:
                pygame.draw.rect(window,green,(int(screenWidth/2-100),int(screenHeight/2-50),200,100))
                playAgainTxt = fontL.render('Main Menu',True,black)
                playAgainRect = playAgainTxt.get_rect()
                window.blit(playAgainTxt,(int(screenWidth/2-(playAgainRect.width/2)),int(screenHeight/2-20)))
                if prevPressed1 == True and pressed1 == False:
                    gameLoop = False
            else:
                pygame.draw.rect(window,white,(int(screenWidth/2-100),int(screenHeight/2-50),200,100))
                playAgainTxt = fontL.render('Main Menu',True,black)
                playAgainRect = playAgainTxt.get_rect()
                window.blit(playAgainTxt,(int(screenWidth/2-(playAgainRect.width/2)),int(screenHeight/2-20)))
                
            prevPressed1 = pressed1
        
        pygame.display.flip()
        
        clock.tick(50)

    titleScreen()

def titleScreen():
    global gameLoop
    global gameOver
    global mainMenu
    global obstacles
    global totalCoins
    global playerSpeed
    global coinImg
    global speedUpCost
    global healthUpCost
    global timeUpCost
    global timeLength
    global maxHealth
    
    mainMenu = True
    prevPressed1 = False
    
    while mainMenu:
        for event in pygame.event.get():
            if (event.type==pygame.QUIT): 
                pygame.quit()
        
        mouse = pygame.mouse.get_pos()
        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
        window.fill(mainMenuBack)

        titleTxt = fontXL.render('Submarine Dive',True,black)
        titleRect = titleTxt.get_rect()
        window.blit(titleTxt,(int((screenWidth/2)-(titleRect.width/2)),25))
        
        def coinDisplay(x,y,coinNum):
            coinTxt = font.render(str(coinNum),True,black)
            coinRect = coinTxt.get_rect()
            window.blit(coinTxt,(int(x+30),int(y))) #x --> (screenWidth-(coinRect.width+10)
            window.blit(coinImg,(int(x),int(y-5)))

        coinDisplay(screenWidth-(11*len(str(totalCoins))+40),10,totalCoins) #11 = coinRect.width of 1 digit
        
        #Play Button
        #if (screenWidth/2)-100 <= mouse[0] <= (screenWidth/2)+100 and (screenHeight/2)-200 <= mouse[1] <= (screenHeight/2)-100: 
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
        
        #Speed Upgrade
        if 50 <= mouse[0] <= 150 and screenHeight-100 <= mouse[1] <= screenHeight-50: #if hovering over with mouse
            pygame.draw.rect(window,green,(50,screenHeight-100,100,50))
            speedUpTxt = font.render('+Speed',True,black)
            window.blit(speedUpTxt,(60,screenHeight-85))
            if prevPressed1 == True and pressed1 == False:
                if totalCoins >= speedUpCost:
                    playerSpeed += 1
                    totalCoins -= speedUpCost
                    speedUpCost += 25
        else:
            pygame.draw.rect(window,white,(50,screenHeight-100,100,50))
            speedUpTxt = font.render('+Speed',True,black)
            window.blit(speedUpTxt,(60,screenHeight-85))

        #Time Upgrade
        if (screenWidth/2)-50 <= mouse[0] <= (screenWidth/2)+50 and screenHeight-100 <= mouse[1] <= screenHeight-50:
            pygame.draw.rect(window,green,(int((screenWidth/2)-50),int(screenHeight-100),100,50))
            timeUpTxt = font.render('+Time',True,black)
            window.blit(timeUpTxt,(int((screenWidth/2)-30),int(screenHeight-85)))
            if prevPressed1 == True and pressed1 == False:
                if totalCoins >= timeUpCost:
                    timeLength += 5
                    totalCoins -= timeUpCost
                    timeUpCost += 25
        else:
            pygame.draw.rect(window,white,(int((screenWidth/2)-50),int(screenHeight-100),100,50))
            timeUpTxt = font.render('+Time',True,black)
            window.blit(timeUpTxt,(int((screenWidth/2)-30),int(screenHeight-85)))
        
        #Health Upgrade
        if (screenWidth)-150 <= mouse[0] <= (screenWidth)-50 and screenHeight-100 <= mouse[1] <= screenHeight-50:
            pygame.draw.rect(window,green,(screenWidth-150,screenHeight-100,100,50))
            healthUpTxt = font.render('+Health',True,black)
            window.blit(healthUpTxt,(screenWidth-140,screenHeight-85))
            if prevPressed1 == True and pressed1 == False:
                if totalCoins >= healthUpCost and maxHealth < 4:
                    maxHealth += 1
                    totalCoins -= healthUpCost
                    healthUpCost = 0
        else:
            pygame.draw.rect(window,white,(screenWidth-150,screenHeight-100,100,50))
            healthUpTxt = font.render('+Health',True,black)
            window.blit(healthUpTxt,(screenWidth-140,screenHeight-85))

        coinDisplay(screenWidth-120-(len(str(healthUpCost))*5.5),screenHeight-125,healthUpCost)
        coinDisplay((screenWidth/2)-20-(len(str(timeUpCost))*5.5),screenHeight-125,timeUpCost)
        coinDisplay(80-(len(str(speedUpCost))*5.5),screenHeight-125,speedUpCost)
        
        prevPressed1 = pressed1

        pygame.display.flip()
        clock.tick(50)
        
    gameLoop = True
    gameOver = False
    GameLoop()

titleScreen()
