
import pygame,time,random
from pygame.locals import*
pygame.init()

box1=0
box2=0
box3=0
box4=0
box5=0
box6=0
box7=0
box8=0
box9=0

print("Enter the username of player_X down below:")
x_name=input()
print("Enter the username of player_O down below:")
o_name=input()

boxs={box1:0,box2:0,box3:0,box4:0,box5:0,box6:0,box7:0,box8:0,box9:0}

def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",50)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

def x_win():

    if((box1==box2==box3==1) or (box4==box5==box6==1) or(box7==box8==box9==1)or(box1==box4==box7==1)or (box2==box5==box8==1)or(box3==box6==box9==1)or(box1==box5==box9==1)or(box3==box5==box7==1)):
        print(x_name," WINS!!!      :D")
        show_text(x_name+" WINS!!!",0,200,colors[r])
        pygame.display.update()
        time.sleep(3)
        quit()      
    
def o_win():

    if(box1==box2==box3==2) or (box4==box5==box6==2) or(box7==box8==box9==2)or(box1==box4==box7==2)or (box2==box5==box8==2)or(box3==box6==box9==2)or(box1==box5==box9==2)or(box3==box5==box7==2):
        print(o_name," WINS!!!      :D")
        show_text(o_name+" WINS!!!",0,200,colors[n])
        pygame.display.update()
        time.sleep(3)
        quit()
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

rand_col=(r,g,b)
green=(0,255,0)
blue=((0,0,255))
red=((255,0,0))
teel=((0,255,255))
yellow=((225,225,0))
purple=((225,0,255))
black=((0,0,0))
white=((255,255,255))
colors=[red,yellow,green,teel,blue,purple,white,rand_col]

count=1

x=0
y=-150
w=150
h=150

screen= pygame.display.set_mode((450,450))

r=random.randint(0,7)
n=random.randint(0,7)

for b in range(0,3):
    y=y+150
    x=0
    for a in range(0,3):
        pygame.draw.rect(screen,blue,(x,y,w,h),5)
        x=x+150


pygame.display.set_caption("Tic Tac Toe")
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            x=event.pos

#box1
            if ((x[0]<=150) and (x[1]<=150)):
                if box1==0:
                    if count%2!=0:
                        pygame.draw.line(screen,colors[r],(0,0),(150,150),8)
                        pygame.draw.line(screen,colors[r],(150,0),(0,150),8)

                        count=count+1
                        box1=1

                    elif count%2==0:
                        pygame.draw.circle(screen,colors[n],(75,75),75,8)

                        count=count+1

                        box1=2
                   
#box2

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
                
#box3

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
        
#box4
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
            
#box5
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
           
#box6
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
              
#box7
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
              
#box8
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
             
#box9
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
                



    pygame.display.update()

    x_win()
    o_win()

    if box1!=0 and box2!=0 and box3!=0 and box4!=0 and box5!=0 and box6!=0 and box7!=0 and box8!=0 and box9!=0:
        print("DRAW!")
        show_text("DRAW!",50,200,white)
        pygame.display.update()
        time.sleep(3)
        quit()
        
