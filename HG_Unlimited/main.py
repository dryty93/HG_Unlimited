from vegeta import Vegeta
from gameverse import *

seconds = 0.00

time = makeLabel(str(seconds),60,454,0,'white')


while True:
    seconds += 0.1
    secondsR = round(seconds, 2)
    changeLabel(time, (str)(secondsR), "white")
    showLabel(time)


    charSelect()

    if keyPressed("m"):
        print('k')

    tick(300)





