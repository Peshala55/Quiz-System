import pygame,sys,time,math
from PIL import Image
#from grazie import proc

import socket
import sys
from details import *
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.connect((ip, port))

bruh = input('Connected to server succesfully! Press Enter to start:')



#Display dimensions
DisplayWidth = 1280
DisplayHeight = 720



def Quit():
    pygame.quit()
    quit()


def master_client():
    f=0
    try:
        h = server.recv(64).decode('utf-8')

        if {h} == {'Scott'}:
            f=1
            return f
        elif {h} == 'Nobel':
            f=2
            return f
        elif {h} == 'Shakespeare':
            f=3
            return f
        elif {h} == 'Newton':
            f=4
            return f

    except:
        print('Closing...')
        sys.exit()


File = open('MCQTable.txt','r')
MCQStore = []
DataLine = 'Aksith ponz'
NoOfMCQs = 0
while len(DataLine)>0:
    DataLine = File.readline()
    if len(DataLine)>0:
        DataLine = DataLine.split('\n')[0]
        Data = DataLine.split(',')
        del Data[0]

        NoOfMCQs+=1
        MCQStore.append(Data)

File = open('LAQTable.txt','r')
LAQStore = []
DataLine = 'Aksith'
NoOfLAQs = 0
while len(DataLine)>0:
    DataLine = File.readline()
    if len(DataLine)>0:
        DataLine = DataLine.split('\n')[0]
        Data = DataLine.split(',')
        del Data[0]
        NoOfLAQs+=1
        LAQStore.append(Data)

for x in range (0,NoOfMCQs):
    image = Image.open(MCQStore[x][5])
    width, height = image.size
    newwidth = int((width/height)*300)
    newimage = image.resize((newwidth, 300), Image.NEAREST)
    newimage.save(MCQStore[x][5])

for x in range (0,NoOfLAQs):
    image = Image.open(LAQStore[x][1])
    width, height = image.size
    newwidth = int((width/height)*300)
    newimage = image.resize((newwidth, 300), Image.NEAREST)
    newimage.save(LAQStore[x][1])



black = [0,0,0]
white = [255,255,255]
grey = [150,150,150]
pink =  [255,0,255]
red = [255,0,0]
orange = [255,165,0]
blue =[0,0,255]
yellow = [255,255,0]
green = [0,255,0]

fontchoice1 = 'Super Mario Bros. NES.ttf'

pygame.init()

TickPic = pygame.image.load('Pictures/Tick.png')
CrossPic = pygame.image.load('Pictures/Cross.png')

#gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight) ,pygame.FULLSCREEN)
gameDisplay = pygame.display.set_mode((DisplayWidth,DisplayHeight))
pygame.display.set_caption('Buzzer System')
clock = pygame.time.Clock()



def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def LargeText(text,font,size,color,posx,posy):
    largeText = pygame.font.Font(font,size)
    TextSurf, TextRect = text_objects(text,largeText,color)
    TextRect.center = ((posx),(posy))
    gameDisplay.blit(TextSurf, TextRect)

def SmallText(text,font,size,color,posx,posy):
    smallText = pygame.font.Font(font,size)
    TextSurf, TextRect = text_objects(text,smallText,color)
    TextRect.center = ((posx),(posy))
    gameDisplay.blit(TextSurf, TextRect)

def text(message,colour,size,location):
    font = pygame.font.Font(fontchoice1,size)
    h = font.render(message,0,colour)
    gameDisplay.blit(h,location)

def DisplayModule1MCQ(ChoiceColour,width,height):
    global MCQStore
    text(MCQStore[x][0],[255,255,255],20,[DisplayWidth/2-10*len(MCQStore[x][0]),DisplayHeight/4])
    text('A:'+MCQStore[x][1],ChoiceColour[0],20,[DisplayWidth/2-10*len(MCQStore[x][1])-300,7*DisplayHeight/8-30])
    text('B:'+MCQStore[x][2],ChoiceColour[1],20,[DisplayWidth/2-10*len(MCQStore[x][2])+300,7*DisplayHeight/8-30])
    text('C:'+MCQStore[x][3],ChoiceColour[2],20,[DisplayWidth/2-10*len(MCQStore[x][3])-300,7*DisplayHeight/8+30])
    text('D:'+MCQStore[x][4],ChoiceColour[3],20,[DisplayWidth/2-10*len(MCQStore[x][4])+300,7*DisplayHeight/8+30])
    gameDisplay.blit(pygame.image.load(MCQStore[x][5]),(DisplayWidth/2-(width/2),DisplayHeight/2-(height/2)))


def DisplayQuestionNo():
    global QuestionNo
    global event
    Exit1 = False
    Time = 0
    while Exit1 == False :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Quit()
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   return Quit()

        gameDisplay.fill(black)
        text('Question No: '+str(QuestionNo),pink,20,[(DisplayWidth/2)-100,DisplayHeight/2])
        pygame.draw.line(gameDisplay,red,(0,0),(DisplayWidth*(Time/4),0),10)
        Time+=0.03

        if event.type == pygame.MOUSEBUTTONDOWN or Time>4 :
            #if event.key == pygame.K_SPACE:
            Exit1 = True


        pygame.display.flip()
        clock.tick(60)

def DisplayQs():
    global QuestionNo
    global event

    Time = 15


    Exit2 = False

    thread1.house = 0
    while Exit2 == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return Quit()

        image = Image.open(MCQStore[x][5])
        width, height = image.size
        gameDisplay.fill(black)
        ChoiceColour = [white,white,white,white]
        DisplayModule1MCQ(ChoiceColour,width,height)
        text('Question No: '+str(QuestionNo),[255,255,255],20,[DisplayWidth/10,DisplayHeight/10])
        global angle
        global ded

        if round(Time) < 10:
            color = [255,0,0]
        else:
            color = [255,255,255]
        ded =1- (Time- int(Time))
                    #print(ded)

        angle = 2*ded*math.pi
        t = 4
        pygame.draw.arc(gameDisplay,(color), ((DisplayWidth)-300,(DisplayHeight/10-30),100,100), 0,angle,t)
        if (round(Time,4))<10:
            TimeStr = '0'+(str(round(Time,1)))
        else:
            TimeStr = (str(round(Time,1)))
        text((TimeStr),color,15,[DisplayWidth-300,DisplayHeight/10+20])
        if Time >0:
            Time-=(1/60)
        if Time<0:
            return '0'
        #print(thread1.isAlive())

        if thread1.house !=0:
            print('Detected that house has changed')
            #print(int(thread1.house))
            buzzy = int(thread1.house)
            thread1.house = 0
            return buzzy

        #for i in 'scott shakespeare newton nobel'.split():
         #   s = proc(i)
          #  if s:
           #     return s
            #else:
             #   pass

        pygame.display.update()
        clock.tick(60)

def SomeoneBuzzesIn(TeamNo):
    global QuestionNo
    global event
    Exit3 = False
    if TeamNo == '0':
        return ['0','0']

    while not Exit3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Quit()
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   return Quit()
        image = Image.open(MCQStore[x][5])
        width, height = image.size
        BorderColour = TeamColours[TeamNo]
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, BorderColour, (0,0,DisplayWidth,DisplayHeight), 10)
        ChoiceColour = [white,white,white,white]
        DisplayModule1MCQ(ChoiceColour,width,height)
        text(str(TeamName[int(TeamNo)-1]),[255,255,255],20,[DisplayWidth/10,DisplayHeight/10])

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_a:
                return ['a',TeamNo]
            elif event.key == pygame.K_b:
                return ['b',TeamNo]
            elif event.key == pygame.K_c:
                return ['c',TeamNo]
            elif event.key == pygame.K_d:
                return ['d',TeamNo]

        pygame.display.flip()
        clock.tick(100)

def InputAnswer(TeamAnswerArray):
    global QuestionNo
    global event
    Exit4 = False
    TeamNo = TeamAnswerArray[1]
    TeamAnswer = TeamAnswerArray[0]
    if TeamNo == '0':
        return ['0','0']
    Time = 0
    while not Exit4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Quit()
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   return Quit()
        image = Image.open(MCQStore[x][5])
        width, height = image.size
        BorderColour = TeamColours[TeamNo]
        ChoiceColour = [grey,grey,grey,grey]
        ChoiceColour[TeamAnswers[TeamAnswer]] = white
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, BorderColour, (0,0,DisplayWidth,DisplayHeight), 10)
        DisplayModule1MCQ(ChoiceColour,width,height)
        text(str(TeamName[int(TeamNo)-1]),[255,255,255],20,[DisplayWidth/10,DisplayHeight/10])


        if Time >2:
            return TeamAnswerArray

        Time +=0.03
        pygame.display.flip()
        clock.tick(100)

def ViewCorrectAnswer(TeamAnswerArray):
    global QuestionNo
    global event
    Exit5 = False
    Time = 0
    TeamNo = TeamAnswerArray[1]
    TeamAnswer = TeamAnswerArray[0]
    if TeamNo == '0':
        return ['0','0']
    AnswerCorrect = False
    image = Image.open(MCQStore[x][5])
    width, height = image.size
    BorderColour = TeamColours[TeamNo]
    ChoiceColour = [grey,grey,grey,grey]
    if MCQStore[QuestionNo-1][6] == TeamAnswer.upper():
        ChoiceColour[TeamAnswers[TeamAnswer]] = green
        AnswerCorrect = True
    else:
        ChoiceColour[TeamAnswers[TeamAnswer]] = red
    while not Exit5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Quit()
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   return Quit()
        image = Image.open(MCQStore[x][5])
        width, height = image.size
        BorderColour = TeamColours[TeamNo]
        ChoiceColour = [grey,grey,grey,grey]
        if MCQStore[QuestionNo-1][6] == TeamAnswer.upper():
            ChoiceColour[TeamAnswers[TeamAnswer]] = green
        else:
            ChoiceColour[TeamAnswers[TeamAnswer]] = red
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, BorderColour, (0,0,DisplayWidth,DisplayHeight), 10)
        DisplayModule1MCQ(ChoiceColour,width,height)
        text(str(TeamName[int(TeamNo)-1]),[255,255,255],20,[DisplayWidth/10,DisplayHeight/10])
        if Time >3:
            return [AnswerCorrect,TeamNo]
        Time+=0.03
        pygame.display.flip()
        clock.tick(100)

def DisplayScores(TeamAnswerArray):
    global QuestionNo
    global event
    global Score
    Time = 0
    Exit6 = False
    TeamNo = int(TeamAnswerArray[1])
    TeamAnswer = TeamAnswerArray[0]
    if TeamNo == '0':
        Exit6 = True
    if TeamAnswer == True:
        Score[1][TeamNo-1] += 1
    a = Score[1][0]
    b = Score[1][1]
    c = Score[1][2]
    d = Score[1][3]
    SortedScore =[[1,2,3,4],[a,b,c,d]]
    teams, scores = SortedScore
    teams.sort(key=lambda i: scores[i-1])
    scores.sort()
    teams = teams[::-1]
    scores = scores[::-1]
    SortedScore = [teams],[scores]
    #print(scores,teams)









    while not Exit6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Quit()
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   return Quit()
        image = Image.open(MCQStore[x][5])
        width, height = image.size
        gameDisplay.fill(black)

        text(TeamName[teams[0]-1]+':  '+str(scores[0]),[255,255,255],20,[DisplayWidth/2-10*len(TeamName[teams[0]-1]+':  '+str(scores[0])),DisplayHeight/4-20])
        text(TeamName[teams[1]-1]+':  '+str(scores[1]),[255,255,255],20,[DisplayWidth/2-10*len(TeamName[teams[1]-1]+':  '+str(scores[1])),2*DisplayHeight/4-20])
        text(TeamName[teams[2]-1]+':  '+str(scores[2]),[255,255,255],20,[DisplayWidth/2-10*len(TeamName[teams[2]-1]+':  '+str(scores[2])),3*DisplayHeight/4-20])
        text(TeamName[teams[3]-1]+':  '+str(scores[3]),[255,255,255],20,[DisplayWidth/2-10*len(TeamName[teams[3]-1]+':  '+str(scores[3])),4*DisplayHeight/4-20])

        if Time >4:
            Exit6 = True

        Time+=0.03
        pygame.display.flip()
        clock.tick(100)



################################################################################################################################################################################


def DisplayQs2():
    global QuestionNo
    global event
    Exit2 = False
    Time = 15
    thread1.house=0
    while Exit2 == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return Quit()
        image = Image.open(MCQStore[x][5])
        width, height = image.size

        gameDisplay.fill(black)
        text(LAQStore[x][0],[255,255,255],20,[DisplayWidth/2-10*len(LAQStore[x][0]),DisplayHeight/4])
        gameDisplay.blit(pygame.image.load(LAQStore[x][1]),(DisplayWidth/2-(width/2),DisplayHeight/2-(height/2)))
        text('Question No: '+str(QuestionNo),[255,255,255],20,[DisplayWidth/10,DisplayHeight/10])
        global angle
        global ded

        if round(Time) < 10:
            color = [255,0,0]
        else:
            color = [255,255,255]
        ded =1- (Time- int(Time))
                    #print(ded)

        angle = 2*ded*math.pi
        t = 4
        pygame.draw.arc(gameDisplay,(color), ((DisplayWidth)-300,(DisplayHeight/10-30),100,100), 0,angle,t)
        if (round(Time,4))<10:
            TimeStr = '0'+(str(round(Time,4)))
        else:
            TimeStr = (str(round(Time,4)))
        text((TimeStr),color,15,[DisplayWidth-300,DisplayHeight/10+20])
        if Time >0:
            Time-=0.03
        if Time<0:
            return '0'


        if thread1.house !=0:
            print('Detected that house has changed')
            #print(int(thread1.house))
            buzzy = int(thread1.house)
            thread1.house = 0
            return buzzy


        pygame.display.update()
        clock.tick(100)

def SomeoneBuzzesIn2(TeamNo):
    global QuestionNo
    global event
    Exit3 = False
    if TeamNo == '0':
        return ['0','0']

    while not Exit3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Quit()
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   return Quit()
        image = Image.open(MCQStore[x][5])
        width, height = image.size
        BorderColour = TeamColours[TeamNo]
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, BorderColour, (0,0,DisplayWidth,DisplayHeight), 10)
        text(LAQStore[x][0],[255,255,255],20,[DisplayWidth/2-10*len(LAQStore[x][0]),DisplayHeight/4])
        gameDisplay.blit(pygame.image.load(LAQStore[x][1]),(DisplayWidth/2-(width/2),DisplayHeight/2-(height/2)))
        text(str(TeamName[int(TeamNo)-1]),[255,255,255],20,[DisplayWidth/10,DisplayHeight/10])
        pygame.draw.rect(gameDisplay, green,(0,(7*DisplayHeight/8),(DisplayWidth/4),(DisplayHeight/8)))
        pygame.draw.rect(gameDisplay, red,((3*DisplayWidth/4),(7*DisplayHeight/8),(DisplayWidth/4),(DisplayHeight/8)))
        if event.type == pygame.MOUSEBUTTONDOWN :
            pos = pygame.mouse.get_pos()
            if pos[0]<(DisplayWidth/4) and pos[1]>(7*DisplayHeight/8):
                return [True,TeamNo]
            if pos[0]>(3*DisplayWidth/4) and pos[1]>(7*DisplayHeight/8):
                return [False,TeamNo]

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_a:
                return [True,TeamNo]
            elif event.key == pygame.K_b:
                return [False,TeamNo]


        pygame.display.flip()
        clock.tick(100)

def ViewCorrectAnswer2(TeamAnswerArray):
    global QuestionNo
    global event
    Exit5 = False
    Time = 0
    TeamNo = TeamAnswerArray[1]
    TeamAnswer = TeamAnswerArray[0]
    if TeamNo == '0':
        return ['0','0']
    AnswerCorrect = TeamAnswer
    image = Image.open(MCQStore[x][5])
    width, height = image.size
    BorderColour = TeamColours[TeamNo]
    while not Exit5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return Quit()
            elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_ESCAPE:
                   return Quit()
        image = Image.open(MCQStore[x][5])
        width, height = image.size
        BorderColour = TeamColours[TeamNo]
        Picture = CrossPic
        if AnswerCorrect== True:
            Picture = TickPic

        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, BorderColour, (0,0,DisplayWidth,DisplayHeight), 10)
        text(LAQStore[x][0],[255,255,255],20,[DisplayWidth/2-10*len(LAQStore[x][0]),DisplayHeight/4])
        gameDisplay.blit(Picture,(DisplayWidth/2-(width/2),DisplayHeight/2-(height/2)))
        text(str(TeamName[int(TeamNo)-1]),[255,255,255],20,[DisplayWidth/10,DisplayHeight/10])
        if Time >3:
            return [AnswerCorrect,TeamNo]
        Time+=0.03
        pygame.display.flip()
        clock.tick(100)


class myThread(threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)
      self.house = 0
   def run(self):
        print ("Starting Thread")
        while True:
            try:
                h = server.recv(64).decode('utf-8')
                print('The value' + str(h) + 'has been received from the server')
                if {h} == {'Scott'}:
                    f=1
                elif {h} == {'Nobel'}:
                    f=2
                elif {h} == {'Shakespeare'}:
                    f=3
                elif {h} == {'Newton'}:
                    f=4
                thread1.house = f

            #thread1.exit()

            except:
                print('Closing... Exception')
                sys.exit()
        print('Exiting Thread')
        #return 0

################################################################ MAIN PROGRAM ################################################################################################################

TeamName = ['Scott','Nobel','Shakespeare','Newton']
TeamColours = {1:red, 2:orange, 3:blue, 4:yellow}
TeamAnswers = {'a':0, 'b':1, 'c':2, 'd':3}
Score = [[1,2,3,4],[0,0,0,0]]
QuestionNo = 1
thread1 = myThread()
thread1.start()
for x in range(0,NoOfMCQs):
    DisplayQuestionNo()
    DisplayScores(ViewCorrectAnswer(InputAnswer(SomeoneBuzzesIn(DisplayQs()))))
    QuestionNo+=1

for x in range(0,NoOfLAQs):
    DisplayQuestionNo()
    DisplayScores(ViewCorrectAnswer2(SomeoneBuzzesIn2(DisplayQs2())))
    QuestionNo+=1
