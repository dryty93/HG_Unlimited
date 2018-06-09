from vegeta import Vegeta
from gameverse import *
from start import *


seconds = 0.00

time = makeLabel(str(seconds),60,454,0,'white')


while True:

    charSelect()


    seconds += 0.1
    secondsR = round(seconds, 2)
    changeLabel(time, (str)(secondsR), "white")
    showLabel(time)



 

    tick(300)





