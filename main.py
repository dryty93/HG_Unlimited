from start import *
from vegeta import Vegeta
from gameverse import *


seconds = 0.00

time = makeLabel(str(seconds),60,454,0,'white')
drawLine(0, 470, 800, 475, 'White', linewidth= 10)

startScreen()

while True:
    firstPlayer()
    secondPlayer()

    seconds += 0.1
    secondsR = round(seconds, 2)
    changeLabel(time, (str)(secondsR), "white")
    showLabel(time)




 

    tick(300)





