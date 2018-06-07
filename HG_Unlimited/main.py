from vegeta import Vegeta
from gameverse import *

seconds = 0.00

time = makeLabel(str(seconds),60,454,0,'white')

firstPlayer()
secondPlayer()


while True:
    seconds += 0.1
    secondsR = round(seconds, 2)
    changeLabel(time, (str)(secondsR), "white")
    showLabel(time)


    if keyPressed('a'):
        HIEP2.left()

    tick(300)





