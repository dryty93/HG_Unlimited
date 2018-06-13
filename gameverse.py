from vegeta import *
from hie import *
from goku import *


#imageListG.add(gokuL[2])

fPlayer = input("P1: What character do you choose?")
sPlayer = input("P2: What character do you choose?")




def firstPlayer():

#Assigns instances of char based on 1st
#player screen positionioning and options

    if fPlayer == "Hie":

        HIEP1.fPlay()


    if fPlayer == "Vegeta":
        VEGP1.fPlay()

    if fPlayer == "Goku":
        GOKUP1.fPlay()

        if keyPressed("i"):
            GOKUP1.sSI = True
            GOKUP1.superI()
            if GOKUP1.xp < 100:
                GOKUP1.sSI = False

        if keyPressed("p") and keyPressed("left"):
            GOKUP1.kamehaL()

        if keyPressed("9"):
            GOKUP1.powerUp()



def secondPlayer():
    #Assigns instance of char based on 2st
     #player screen positionioning and options

    if sPlayer == "Vegeta":

        VEGP2.sPlay()


    if sPlayer == "Hie":

        HIEP2.sPlay()

    if sPlayer == "Goku":

        GOKUP2.sPlay()

        if keyPressed("q"):
            GOKUP2.kamehaR()



