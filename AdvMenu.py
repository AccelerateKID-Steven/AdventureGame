#imports Modules
import pygame, sys, os

#setup window
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Adventure Game")
screen = pygame.display.set_mode((500,500),0,False)
rootDirectory = os.path.dirname(__file__)
imageDirectory = rootDirectory +'\\img'
textDirectory = rootDirectory +'\\text'



TitleFont = pygame.font.SysFont(None,50)
NormalFont = pygame.font.SysFont(None,30)

#Title
Title = TitleFont.render("Adventure Game",1,(255,255,255))
Titlerect = Title.get_rect()
Titlerect.topleft = (20,20)

#Clicks
click = False
rightClick = False

#Button
btnStart = pygame.draw.rect(screen,(100,250,50),(30,175,150,40))
txtStart = NormalFont.render("Start",1,(0,0,0))
txtStartrect = txtStart.get_rect()
txtStartrect.center = (80,200)
#Buttons for Answers

#Other Field Variables
mouseX, mouseY = pygame.mouse.get_pos()
questionCount = 0
#add more items in here for the game to remember
userDictionary = {
    "name": "",
    "class": ""

}



currentQuestions = []

pygame.display.update()


def grabFile(fileName):

    #[Type of Sentence (Sentence/Question)][The actual words said]
    dialogue = open(textDirectory +'\\' + fileName + '.txt')
    #local variables that can be used in either if statement
    myCount = 0
    tempArray1 = []
    
    if fileName == "text":
        #local variables that can only be used in this if statement
        tempArray2 = []
        
        for line in dialogue:
            tempArray1.insert(myCount,line)
            tempArray2.insert(myCount,dialogue.readline())
            myCount = myCount + 1

        
        textArray = [tempArray1,tempArray2]
    elif fileName == "questions":
        #local variable
        tempString = dialogue.readlines()
        currentAnswers = tempString[questionCount]
        
        #print(tempString)
        #We need to turn the string into a delimited array
        textArray = currentAnswers.split(",")


    dialogue.close()
    return textArray

def fpsAndMouse():
    #FPS
    myFPS = NormalFont.render(str(round(mainClock.get_fps(),2)),1,(255,10,10))             
                
    myFPSrect = myFPS.get_rect()
    myFPSrect.topleft = (400,30)
    screen.blit(myFPS,myFPSrect)
        
    mouseX, mouseY = pygame.mouse.get_pos()
    #shows the x and y of the mouse real time
    xAndy = NormalFont.render("(" + str(mouseX) + ", " + str(mouseY) + ")",1,(255,255,255))                      
    xAndyrect = xAndy.get_rect()
    xAndyrect.topleft = (mouseX+15,mouseY-15)
    screen.blit(xAndy,xAndyrect)
    return mouseX,mouseY

#sends in dialouge and puts it on screen
def createText(text):
    txtBox = NormalFont.render(text,1,(0,0,0))
    txtBoxrect = txtBox.get_rect()
    txtBoxrect.topleft = (20,390)
    #TODO:Wrap text?
    screen.blit(txtBox,txtBoxrect)
    

#create buttons to click for answering questions
def createAnswers(text):
    #parameter: Array that has the answers in them

    #btn Creation
    global btnAnswer1,btnAnswer2,btnAnswer3,btnAnswer4
    btnAnswer1 = pygame.draw.rect(screen,(100,200,50),(30,410,150,30))
    btnAnswer2 = pygame.draw.rect(screen,(100,200,50),(200,410,150,30))
    btnAnswer3 = pygame.draw.rect(screen,(100,200,50),(30,450,150,30))
    btnAnswer4 = pygame.draw.rect(screen,(100,200,50),(200,450,150,30))
    #txt Creation
    txtBtn1 = NormalFont.render(text[0],1,(0,0,0))
    txtBtn1rect = txtBtn1.get_rect()
    txtBtn1rect.topleft = (40,415)
    txtBtn2 = NormalFont.render(text[1],1,(0,0,0))
    txtBtn2rect = txtBtn2.get_rect()
    txtBtn2rect.topleft = (210,415)
    txtBtn3 = NormalFont.render(text[2],1,(0,0,0))
    txtBtn3rect = txtBtn3.get_rect()
    txtBtn3rect.topleft = (40,455)
    txtBtn4 = NormalFont.render(text[3],1,(0,0,0))
    txtBtn4rect = txtBtn4.get_rect()
    txtBtn4rect.topleft = (210,455)
    screen.blit(txtBtn1,txtBtn1rect)
    screen.blit(txtBtn2,txtBtn2rect)
    screen.blit(txtBtn3,txtBtn3rect)
    screen.blit(txtBtn4,txtBtn4rect)

def grabKey(currentAnswer):
    global questionCount
    #function will grab the key, set value
    #ONLY IF WE CLICK THE BUTTON
    count = 0
    for x in userDictionary.keys():
        if count == questionCount:
                    
            userDictionary[x] = currentAnswer
        else:
            count = count + 1
    questionCount = questionCount + 1

def gameScreen():
    secondWhile = True
    clickCount = 0
    click = False
    questionCount = 0
    clickcounter = True
    responses = None
    global userDictionary
    character = "transparent.jpg"
    background = "fluffy-clouds.jpg"
    while secondWhile == True:
        
        #makes the background black
        screen.fill((0,0,0))
        
        #For Changing Backgrounds
        if(clickCount == 3):
            background = "sunrise.jpg"

        
        myImage = pygame.transform.smoothscale(
            pygame.image.load(imageDirectory + "\\" + background)
            ,(500,376)
        )
        screen.blit(myImage,(0,0))         #   x y    width height
        
        #For Adding Items/Characters on screen
        if(clickCount == 4):
            character = "BajaBlast.jpg"
            myCharacter = pygame.transform.smoothscale(
            pygame.image.load(imageDirectory + "\\" + character)
            ,(500,376)
            )
            screen.blit(myCharacter,(0,0))   
        

         
        #This is the bar at the bottom of the game
        pygame.draw.rect(screen,(255,255,255),(0,375,500,125),0)
        pygame.draw.rect(screen,(135,179,120),(20,390,460,95),0)
        

        mouseX, mouseY = fpsAndMouse()

        #Where to do run game
        
        #Displays text until at the end of the array
        #if clickCount < len(myText[1]):
        #    createText(myText[1][clickCount])

        #If the category is question
        try:
            if myText[0][clickCount]=="Question\n":

                    createText(myText[1][clickCount])
                    #create a text box below the normal text
                    #just for the questions
                    responses = grabFile("questions")
                    createAnswers(responses)

                
                    clickcounter = False
            #if the category is sentence
            elif myText[0][clickCount]=="Sentence\n":
                #Add an If/Else for every item you need to use/replace in text
                    if(myText[1][clickCount].find("NAME") == -1):
                        createText(myText[1][clickCount])
                    else:
                    
                        myText[1][clickCount] = myText[1][clickCount].replace("NAME",userDictionary["name"])
                        createText(myText[1][clickCount])
                    
                    if(myText[1][clickCount].find("CLASS") == -1):
                        createText(myText[1][clickCount])
                    else:
                    
                        myText[1][clickCount] = myText[1][clickCount].replace("CLASS",userDictionary["class"])
                        createText(myText[1][clickCount])
        except IndexError:
            #Display message that game is over,
            #Set clickcounter to false
            createText("Game has ended, please exit the application!")
            clickcounter = False


        if clickcounter == True:
            
        #goes to the next index when you click
            if click == True :
                clickCount = clickCount + 1
        else:
            
            currentAnswer = ""
            if btnAnswer1.collidepoint((mouseX,mouseY)):
                if click == True:
                    #stuff
                    currentAnswer = responses[0]
                    clickcounter = True
                    clickCount = clickCount + 1
                    grabKey(currentAnswer)
            elif btnAnswer2.collidepoint((mouseX,mouseY)):
                if click == True:
                    #stuff
                    currentAnswer = responses[1]
                    clickcounter = True
                    clickCount = clickCount + 1
                    grabKey(currentAnswer)
            elif btnAnswer3.collidepoint((mouseX,mouseY)):
                if click == True:
                    #stuf
                    currentAnswer = responses[2]
                    clickcounter = True
                    clickCount = clickCount + 1
                    grabKey(currentAnswer)
            elif btnAnswer4.collidepoint((mouseX,mouseY)):
                if click == True:
                    #stuff
                    currentAnswer = responses[3]
                    clickcounter = True
                    clickCount = clickCount + 1
                    grabKey(currentAnswer)
           
            



        #Where to stop code for gameplay
        click = False


        rightClick = False     

        
        


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                else:
                    rightClick = True

        pygame.display.update()
        mainClock.tick(60)




        
   
    
def titleScreen():
    firstWhile = True
    while firstWhile == True:

        #TODO: make some epic backgrounds
        titleImage = pygame.image.load(imageDirectory + "\\titleScreenBackground.jpg")
        screen.blit(titleImage,(0,0))
        

        #draws the button
        btnStart = pygame.draw.rect(screen,(100,250,50),(30,175,150,40))
        #moved blits to the while true
        screen.blit(txtStart,txtStartrect)
        screen.blit(Title,Titlerect)

        mouseX, mouseY = fpsAndMouse()

        #Our first Button click event
        if btnStart.collidepoint((mouseX,mouseY)):
            if click == True:
                #do someting
                firstWhile = False
                gameScreen()
                

        
        
       
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    
        #updates the display
        pygame.display.flip()
        mainClock.tick(60)


myText = grabFile("text")
titleScreen() 







