#graphics_play_1.py
gamemode=10
from pygame import *
from random import *
x=input("Would you like to play a game? ")
if x.upper()=="YES":
    print("Well then your in for a suprise!")
elif x.upper()=="NO":
    print("Too bad!")

gamemode=int(input("Length "))

running=True
screen = display.set_mode((1920, 1000))

x=0

cx,cy=300,500
bx,by=1620-(gamemode),500
screen.fill((0,0,255))
while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    keys=key.get_pressed()
    if 1==keys[119]:
        cy-=10
    if 1==keys[115]:
        cy+=10
    if 1==keys[97]:
        cx-=10
    if 1==keys[100]:
        cx+=10
    if 1==keys[273]:
        by-=9
    if 1==keys[274]:

        by+=9
    if 1==keys[275]:
        bx+=9
    if 1==keys[276]:
        bx-=9
    draw.rect(screen,(0,0,0),(0,0,1921,1001))       


    draw.rect(screen,(randint(0,255),0,0),(cx,cy,gamemode,gamemode))
    draw.rect(screen,(255,255,255),(bx,by,gamemode,gamemode))
    time.wait(7)
    if cx in range (bx-gamemode,bx+gamemode) and cy in range (by-gamemode,by+gamemode):
        running=False
    display.flip()
quit()
