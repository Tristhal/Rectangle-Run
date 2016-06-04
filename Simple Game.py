#graphics_play_3.py
#speed boost multiplier
score=0
spdbst=1
pspdbst=1
spdbar=500
spdwait=0
#Square size
gamemode=5
#number of spawning dots
c=0
#spawn timer
x=20
#time between spawns
y=1
#health
h=10
from pygame import *
from random import *
'''x=input("Would you like to play a game? ")
if x.upper()=="YES":
    print("Well then your in for a suprise!")
elif x.upper()=="NO":
    print("Too bad!")
gamemode=int(input("Length "))'''

running=True
screen = display.set_mode((1920, 1000))
bxby=[randint(0,1920),1000,2,10,255,1]
cx,cy=300,500
bx,by=1620-(gamemode),500
while running:
    clock=time.Clock()
    clock.tick(75)
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys=key.get_pressed()
    if 1==keys[304] and spdbar//10>10 and spdwait<=0:
        spdbar-=5
        pspdbst=2
    elif 1==keys[304] and spdbar//10<11:
        spdwait=100
    elif 0==keys[304]:
        spdbar+=1
    if 1==keys[119]:
        cy-=10*pspdbst
    if 1==keys[115]:
        cy+=10*pspdbst
    if 1==keys[97]:
        cx-=10*pspdbst
    if 1==keys[100]:
        cx+=10*pspdbst
    if 1==keys[98]:
        x=x*50
    if 1==keys[99]:
        score=score*50
    if 1==keys[102]:
        h+=100
    if 1==keys[101]:
        spdbar+=100

#GAME START        
    resetint=randint(0,1423)
    for i in range (0,len(bxby),6):
        #speedboost
        xxx=randint(0,300)
        #RESET code
        if resetint==0:
#            for i in range (0,len(bxby),3):
            bxby[i]=randint(-2000,3920)
            bxby[i+1]=randint(-2000,3000)
        #AI MOVEMENT
        if xxx==(1):
            spdbst=10
        if cx>bxby[i]:
            bxby[i+1]+=bxby[i+2]*spdbst*randint(1,3)
        if cx<bxby[i] and cy>bxby[i+1]:
            bxby[i+1]+=bxby[i+2]*spdbst*randint(1,3)
        if cx>bxby[i]:
            bxby[i]+=bxby[i+2]*spdbst*randint(1,3)
        if cy<bxby[i+1]:
            bxby[i+1]-=bxby[i+2]*spdbst*randint(1,3)
        if cx>bxby[i] and cy<bxby[i+1]:
            bxby[i+1]-=bxby[i+2]*spdbst*randint(1,3)
        if cx<bxby[i]:
            bxby[i]-=bxby[i+2]*spdbst*randint(1,3)
        if cx==bxby[i] and cy>bxby[i+1]:
            bxby[i+1]+=bxby[i+2]*spdbst*randint(1,3)
        if cx==bxby[i] and cy<bxby[i]:
            bxby[i+1]-=bxby[i+2]*spdbst*randint(1,3)
        #PERIMETER BORDERS
        if cx>2000 or cx <-100 or cy >1100 or cy <-100 or h<=0:
            running=False
        #RANDOMISED MOTION
        bxby[i]+=randint(-2,2)
        #SPEED BOOST RESET
        spdbst=1
        #Adds Dots
        if x>y:
            c+=1
            for i in range (0,c):
                h+=1
                bxby.append(randint(0,1920))
                bxby.append(randint(0,1000))
                bxby.append(randint(1,3))
                bxby.append(randint(2,25))
                bxby.append(200)
                bxby.append(0)
                x=0
            y+=10
        if bxby[i+5]==1:
            bxby[i+4]-=5
            if bxby[i+4]<150:
                bxby[i+5]=0
        elif bxby[i+5]==0:
            bxby[i+4]+=5
            if bxby[i+4]>250:
                bxby[i+5]=1
    #Screen reset
    draw.rect(screen,(0,0,0),(0,0,1921,1001))
    #Playerw
    draw.rect(screen,(255,0,0),(cx,cy,gamemode,gamemode))
    #HEALTH Loss and AI DRAW       
    for i in range (0,len(bxby),6):
        draw.rect(screen,(255,int(bxby[i+4]),randint(0,100)),(bxby[i],bxby[i+1],bxby[i+3],bxby[i+3]))
        if cx in range (bxby[i]-bxby[i+3],bxby[i]+bxby[i+3]) and cy in range (bxby[i+1]-bxby[i+3],bxby[i+1]+bxby[i+3]):
            h-=1
    #Spawn counter
    x+=1
    pspdbst=1
    spdbst+=1
    spdwait-=1
    #time.delay(15)
    #Health Bar
    if h*20>255:
        draw.rect(screen,(0,255,0),(0,0,20,20))
    elif h>0:
        draw.rect(screen,(0,h*20,0),(0,0,100,20))
    else:
        print("You Loose! :)")
    for i in range(0,h):
        draw.line(screen,(255,50,50),(0+i,40),(0+i,60))
    for i in range(0,spdbar//5):
        if spdwait>0:
            draw.line(screen,(100,150,255),(0+i,70),(0+i,90))
        else:
            draw.line(screen,(50,50,255),(0+i,70),(0+i,90))
    score+=1
    if score>=5000:
        print("YOU WIN!")
        time.wait(550)
    display.flip()
quit()
print("Your score is",score)
