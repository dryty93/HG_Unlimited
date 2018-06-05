# -*- coding: utf-8 -*-
"""

@author:tylerJdryden
"""

from main import*
from start import*
from health_bars import*
from music1 import*
import decimal

music()
startScreen()
seconds = 0.00
time = makeLabel(str(seconds),60,454,0,'white')

while True:
    #Timer
    seconds += 0.1
    secondsR = round(seconds,2)
    changeLabel(time,(str)(secondsR),"white")
    showLabel(time)

    #music
 #   if keyPressed("u"):
        #pygame.mixer.music.stop()
        #pygame.mixer.music.load('C:/Users/dryde/Downloads/Hell-Games-master/Hell-Games-master/HellGames/NYS2.mp3')
  #      pygame.mixer.music.play(-1)
   #     song = makeLabel("Nas: NY State of Mind 2", 30,350,60,'white')
    #    showLabel(song)

    #Life
    health_bars(p1HP.life,p2HP.life,p1HP.stamina,p2HP.stamina)
    HPL1 = makeLabel("P1 HP",15,80,20,'white')
    stam = makeLabel("Stamina",15,80,45,'red')
    HPL2 = makeLabel("P2 HP",15,790,15,'white')
    stam2 = makeLabel("Stamina",15, 790,45, 'red')

    showLabel(HPL1)
    showLabel(stam)
    showLabel(HPL2)
    showLabel(stam2)
    showLabel(time)


#set positions
    p1.pos()
    p2.pos()

    p2.boundary()


    #P1 Controls
    if keyPressed("p") and not keyPressed("0"):
        p1.blast()

    if keyPressed("n"):
        p1.kick()
        if touching(vegetakick, pic2):
            p2HP.bigHit()
            p2.damage()
            killSprite(vegetakick)

    if keyPressed("0"):
        shooter.update()
        p1.vegShootPos()
        playSound(blastSound)
        
        if touching(pic2, shots):
            p2HP.smallHit()
            p2.damage()

    if keyPressed("left"):
        p1.left()

    if keyPressed("left") and keyPressed("6"):
        p1.quickLeft()

    if keyPressed("up"):
        p1.up()

    if keyPressed("up") and keyPressed("6"):
        p1.quickUp()

    if keyPressed("down"):
        p1.down()

    if keyPressed("down") and keyPressed("6"):
        p1.quickDown()

    if keyPressed("right"):
        p1.right()

    if keyPressed("right") and keyPressed("6"):
        p1.quickRight()

    #P2 Controls


    if keyPressed("q"):
        p2.up()

    if keyPressed ("y") and keyPressed("q"):
        p2.quickUp()

    if keyPressed ("w"):
        p2.down()

    if keyPressed ("y") and keyPressed("a"):
        p2.quickDown()

    if keyPressed("a"):
        p2.left()

    if keyPressed("y") and keyPressed("a"):
        p2.quickLeft()

    if keyPressed("s"):
        p2.right()

    if keyPressed("y") and keyPressed("s"):
        p2.quickRight()

    if keyPressed("8"):
        playSound(darkness)
        p2.dragonFist()
        for images in drFistList:
            if touching(pic1, images):
                p1HP.smallHit()
                p1.damage()



    if keyPressed("space"):

        p2.slice()
        p1HP.smallHit()
        p1.damage()



    # Destroy all sprites on impact
    


    if p1HP.life < 0:
        updateDisplay()
        startScreen()

    if p2HP.life < 0:
        updateDisplay()
        startScreen()


    tick(400)
