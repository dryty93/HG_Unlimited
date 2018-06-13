from pygame_functions import*
from os import path
from gameverse import *
#from health_bars import*
Red = (255, 0, 0)
Green = (0,255,0)
Blue = (0, 0 , 255)
Black = (0,0,0)
White = (255, 255, 255)
Yellow = (255, 255, 0)


vegetaChar = makeSprite(os.path.join("images","vegChar.png" ))
hieChar = makeSprite(os.path.join("images","hieChar.png"))
gokuChar = makeSprite(os.path.join("images","gokuChar.jpg"))


started = makeLabel("Press select to start", 60, 200, 250, "yellow")
welcome = makeLabel("Welcome to Hell Games",70, 100, 10, "red")
vegeta = makeLabel("Vegeta", 0,100, 500,"red")
hie = makeLabel("Hie", 10,100, 500,"black")



def startScreen():
    a = True
    while a:
           #make vegeta char select
        showLabel(welcome)
        showLabel(started)
        showLabel(vegeta)

        moveSprite(gokuChar, 350, 310)
        showSprite(gokuChar)

       # showSprite(hie)
       # moveSprite(vegetaChar,30,320,False)
        moveSprite(vegetaChar, 30,320)
        showSprite(vegetaChar)

             #make hie char select

        #moveSprite(hieChar,650,310,False)
        moveSprite(hieChar, 650,310)
        showSprite(hieChar)


        if keyPressed("enter"):
            a = False
            hideLabel(started)
            hideLabel(welcome)
            killSprite(vegetaChar)
            killSprite(hieChar)
            killSprite(gokuChar)





