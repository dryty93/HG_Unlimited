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
    if keyPressed("u"):
        pygame.mixer.music.stop()
        pygame.mixer.music.load('C:/Users/slave/Desktop/NYS2.mp3')
        pygame.mixer.music.play(-1)
        song = makeLabel("Nas: NY State of Mind 2", 30,350,60,'white')
        showLabel(song)
    
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

    if keyPressed("0"):     
        shooter.update()
        p1.shootUpdate()
        playSound(blastSound)

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

    if keyPressed ("a"):
        p2.down()

    if keyPressed ("y") and keyPressed("a"):
        p2.quickDown()

    if keyPressed("s"):
        p2.left()

    if keyPressed("y") and keyPressed("s"):
        p2.quickLeft()

    if keyPressed("d"):
        p2.right()

    if keyPressed("y") and keyPressed("d"):
        p2.quickRight() 

    if keyPressed("8"):
        playSound(darkness)
        p2.dragonFist()
        

    if keyPressed("space"):

        p2.slice()

    #Collisions and points/HP

    if touching(vegetakick,pic2):
        p2HP.smallHit()
        p2.damage()
        killSprite(vegetakick)
        

    # Destroy all sprites on impact
    if touching(shots,shots2):
        killSprite(shots)
        killSprite(shots2)


    if touching(blast,blast2):
        killSprite(blast)
        killSprite(blast2)

    if touching(pic1, shots2):
        killSprite(shots)
        p1HP.smallHit()
        p1.damage()
        

    if touching(pic2, shots):
        killSprite(shots)
        p2HP.smallHit()
        p2.damage()
        
    if touching(pic1,hieattack3) or touching(pic1,hieattack2):
        p1HP.smallHit()
        p1.damage()
        killSprite(hieattack3)

    if touching(pic1, drFist1): 
        p1HP.bigHit()
        p1.damage()
        killSprite(drFist1)

    
    if touching(pic1, drFist2): 
        p1HP.bigHit()
        p1.damage()
        killSprite(drFist2)

    
    if touching(pic1, drFist3): 
        p1HP.bigHit()
        p1.damage()
        killSprite(drFist3)
        
    if touching(pic1, drFist4): 
        p1HP.bigHit()
        p1.damage()
        killSprite(drFist4)
    
    if touching(pic1, drFist5): 
        p1HP.bigHit()
        p1.damage()
        killSprite(drFist5)
        
    if p1HP.life < 0:
        end()
        
    if p2HP.life < 0:
        end()
        
    
    tick(400)
    

      
