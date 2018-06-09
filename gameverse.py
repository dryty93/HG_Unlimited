from vegeta import *
from hie import *
from goku import *




base = 400

p1Pos = 100
p2Pos = 200


#Possible Player Instances



HIEP1 = Hie(imageListH[0], p1Pos, base, 5,  5)
HIEP2 = Hie(imageListH[-1], p2Pos, base, 5,  5)

VEGP1 = Vegeta(imageListV[0], p1Pos, base,  5, 5)
VEGP2 = Vegeta(imageListV[-1], p2Pos, base,  5, 5)

GOKU1 = Goku(imageListG[0], p1Pos, base, 5,  5)
GOKU2 = Goku(imageListG[-1], p2Pos, base,  5, 5)


fPlayer = input('WHat character for p1?')

sPlayer = input('what character for p2?')

drawLine(0, 470, 800, 475, 'White', linewidth= 10)

def charSelect():
#this is where player will be selected. Will update
 #for gui in the future

    firstPlayer()
    secondPlayer()

def firstPlayer():

#Assigns instances of char based on 1st
#player screen positionioning and options

    if fPlayer == "Hie":

        HIEP1.fPlay()


    if fPlayer == "Vegeta":
        VEGP1.fPlay()

    if fPlayer == "Goku":
        GOKU1.fPlay()



def secondPlayer():
    #Assigns instance of char based on 2st
     #player screen positionioning and options

    if sPlayer == "Vegeta":

        VEGP2.sPlay()


    if sPlayer == "Hie":

        HIEP2.sPlay()

        if keyPressed('a'):

            HIEP2.left()

    if sPlayer == "Goku":

        GOKU2.sPlay()



