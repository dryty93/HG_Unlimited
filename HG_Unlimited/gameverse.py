from vegeta import *
from hie import *

fP = False
sP = False

fPlayer = input('WHat character for p1?')

sPlayer = input('what character for p2')

#Possible Player Instances
HIEP1 = Hie(imageListH[0], 100, 100)
HIEP2 = Hie(imageListH[-1], 200, 100)

VEGP1 = Vegeta(imageListV[0], 200, 100)
VEGP2 = Vegeta(imageListV[-1], 100, 100)


def firstPlayer():



    if fPlayer == "Hie":


        HIEP1.fPlay()
        fp = True



    if fPlayer == "Vegeta":
        VEGP1.fPlay()
        fp = True

def secondPlayer():


    if sPlayer == "Vegeta":

        VEGP2.sPlay()
        sp = True

    if sPlayer == "Hie":


        HIEP2.sPlay()
        sp = True


