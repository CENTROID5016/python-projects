#imports
import pygame,time,random
from pygame.locals import*
pygame.init()

#empty value of all boxes on the tic tac toe board
box1=0
box2=0
box3=0
box4=0
box5=0
box6=0
box7=0
box8=0
box9=0

#Giving players usernames of their choice
print("Enter the username of player_X down below:")
x_name=input()
print("Enter the username of player_O down below:")
o_name=input()
#checks that username are not the same
if o_name==x_name:
    print("THAT USERNAME IS ALREADY TAKEN")
print("Enter the username of player_O down below:")
o_name=input()


#function for displaying text on  the tic tac toe borad
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",50)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
#function for x winning the match
def x_win():
    #all the possible outcomes of X winning
    if((box1==box2==box3==1) or (box4==box5==box6==1) or(box7==box8==box9==1)or(box1==box4==box7==1)or (box2==box5==box8==1)or(box3==box6==box9==1)or(box1==box5==box9==1)or(box3==box5==box7==1)):
        #displaying X as the winner
        print(x_name," WINS!!!      :D")
        show_text(x_name+" WINS!!!",0,200,colors[r])
        pygame.display.update()
        #ending the game in style
        time.sleep(3)
        quit()      
#function for O winning the match    
def o_win():
    #all the possible outcomes of O winning
    if(box1==box2==box3==2) or (box4==box5==box6==2) or(box7==box8==box9==2)or(box1==box4==box7==2)or (box2==box5==box8==2)or(box3==box6==box9==2)or(box1==box5==box9==2)or(box3==box5==box7==2):
        #displaying O as the winner
        print(o_name," WINS!!!      :D")
        show_text(o_name+" WINS!!!",0,200,colors[n])
        pygame.display.update()
        #ending the game in style
        time.sleep(3)
        quit()
#making random numbers to use to create a random color
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

#colors that X and O can be drawn in
rand_col=(r,g,b)
green=(0,255,0)
blue=((0,0,255))
red=((255,0,0))
teel=((0,255,255))
yellow=((225,225,0))
purple=((225,0,255))
black=((0,0,0))
white=((255,255,255))
#list of colors that X and O can be drawn in
colors=[red,yellow,green,teel,blue,purple,white,rand_col]

#decides to drawn either X or O
count=1
#values of x,y,w, and h
x=0
y=-150
w=150
h=150

#setting up the screen/board
screen= pygame.display.set_mode((450,450))

#used to make random colors for X and O
r=random.randint(0,7)
n=random.randint(0,7)

#quickly draws rectangles on the board
for b in range(0,3):
    y=y+150
    x=0
    for a in range(0,3):
        pygame.draw.rect(screen,blue,(x,y,w,h),5)
        x=x+150

#game caption
pygame.display.set_caption("Tic Tac Toe")
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            x=event.pos

#box1 logic
            #if click was in box1...
            if ((x[0]<=150) and (x[1]<=150)):
                #and if box1 is empty
                if box1==0:
                    #if Xs turn
                    if count%2!=0:
                        #draws an X
                        pygame.draw.line(screen,colors[r],(0,0),(150,150),8)
                        pygame.draw.line(screen,colors[r],(150,0),(0,150),8)
                        #changing to Os turn
                        count=count+1
                        box1=1
                    #if Os turn
                    elif count%2==0:
                        #draws a circle
                        pygame.draw.circle(screen,colors[n],(75,75),75,8)
                        #changes to Xs turn
                        count=count+1

                        box1=2
                   
#box2 logic(simlar to previous box)

            elif (x[0]>150 and x[0]<300 and x[1]<=150):
                if box2==0:
                    if count%2!=0:
                        pygame.draw.line(screen,colors[r],(150,0),(300,150),8)
                        pygame.draw.line(screen,colors[r],(300,0),(150,150),8)

                        count=count+1
                        box2=1
    
                    elif count%2==0:
                        pygame.draw.circle(screen,colors[n],(225,75),75,8)

                        count=count+1
                        box2=2
                
#box3 logic(simlar to previous box)

            elif x[0]>=300 and x[1]<=150:
                if box3==0:
                    if count%2!=0:
                        pygame.draw.line(screen,colors[r],(300,0),(450,150),8)
                        pygame.draw.line(screen,colors[r],(450,0),(300,150),8)

                        count=count+1
                        box3=1
                    elif count%2==0:
                        pygame.draw.circle(screen,colors[n],(375,75),75,8)
    
                        count=count+1
                        box3=2
        
#box4 logic(simlar to previous box)
            if box4==0:
                if x[0]<=150 and x[1]<=300 and x[1]>150:
                    if count%2!=0:
                        pygame.draw.line(screen,colors[r],(0,150),(150,300),8)
                        pygame.draw.line(screen,colors[r],(150,150),(0,300),8)

                        count=count+1
                        box4=1
                    elif count%2==0:
                        pygame.draw.circle(screen,colors[n],(75,225),75,8)
    
                        count=count+1
                        box4=2
            
#box5 logic(simlar to previous box)
            if box5==0:
                if x[0]<=300 and x[0]>150 and x[1]>150 and x[1]<300:
                    if count%2!=0:
                        pygame.draw.line(screen,colors[r],(150,150),(300,300),8)
                        pygame.draw.line(screen,colors[r],(300,150),(150,300),8)
    
                        count=count+1
                        box5=1
                    elif count%2==0:
                        pygame.draw.circle(screen,colors[n],(225,225),75,8)
    
                        count=count+1
                        box5=2
           
#box6 logic(simlar to previous box)
            if box6==0:
                if x[0]>300 and x[1]>150 and x[1]<300:
                    if count%2!=0:
                        pygame.draw.line(screen,colors[r],(300,150),(450,300),8)
                        pygame.draw.line(screen,colors[r],(450,150),(300,300),8)
    
                        count=count+1
                        box6=1
                    elif count%2==0:
                        pygame.draw.circle(screen,colors[n],(375,225),75,8)
    
                        count=count+1
                        box6=2
              
#box7 logic(simlar to previous box)
            if box7==0:
                if x[0]<150 and x[1]>300:
                    if count%2!=0:
                        pygame.draw.line(screen,colors[r],(0,300),(150,450),8)
                        pygame.draw.line(screen,colors[r],(150,300),(0,450),8)
    
                        count=count+1
                        box7=1
                    elif count%2==0:
                        pygame.draw.circle(screen,colors[n],(75,375),75,8)
    
                        count=count+1
                        box7=2
              
#box8 logic(simlar to previous box)
            if box8==0:
                if x[0]>150 and x[0]<300 and x[1]>300:
                    if count%2!=0:
                        pygame.draw.line(screen,colors[r],(150,300),(300,450),8)
                        pygame.draw.line(screen,colors[r],(300,300),(150,450),8)
    
                        count=count+1
                        box8=1
                    elif count%2==0:
                        pygame.draw.circle(screen,colors[n],(225,375),75,8)
    
                        count=count+1
                        box8=2
             
#box9 logic(simlar to previous box)
            if box9==0:
                if x[0]>300 and x[1]>300:
                    if count%2!=0:
                        pygame.draw.line(screen,colors[r],(300,300),(450,450),8)
                        pygame.draw.line(screen,colors[r],(450,300),(300,450),8)
    
                        count=count+1
                        box9=1
                    elif count%2==0:
                        pygame.draw.circle(screen,colors[n],(375,375),75,8)
    
                        count=count+1
                        box9=2
                


    #updating screen/board
    pygame.display.update()
    #checking for a winner
    x_win()
    o_win()
    #checking for draw 
    if box1!=0 and box2!=0 and box3!=0 and box4!=0 and box5!=0 and box6!=0 and box7!=0 and box8!=0 and box9!=0:
        #displaying draw
        print("DRAW!")
        show_text("DRAW!",50,200,white)
        pygame.display.update()
        #ending the game in style
        time.sleep(3)
        quit()
        
