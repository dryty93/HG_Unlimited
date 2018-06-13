from pygame_functions import *
from os import path
from spritesheetFunctions import *

screenSize(400, 600)


class Player(newSprite):

    def __init__(self, image, xPos, yPos, xSpeed, ySpeed,xp, fP = False, sP = False):
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.xp = xp
        self.fP = fP
        self.sP = sP

    def spawn(self):
        pass

    def gravity(self):
        pass

    def initial(self):
        changeSpriteImage(self.image, 0)

    def fPlay(self):

        """Moves player instance into position for first place"""
        moveSprite(self.image, self.xPos, self.yPos)
        showSprite(self.image)
        self.fP = 2 > 1
        # Default moves for fPlayer

        if self.fP:

            if keyPressed("left"):
                self.left()
                self.initial()
            if keyPressed("right"):
                self.right()
                self.initial()
                
            if keyPressed("up"):
                self.up()
                self.initial()

            if keyPressed("down"):
                self.down()
                self.initial()

    def sPlay(self):
        """Moves player instance into position for 2nd place"""
        moveSprite(self.image, self.xPos, self.yPos)
        showSprite(self.image)

        self.sP = 2 > 1
        if self.sP:
            #Default moves for p2

            if keyPressed("z"):
                self.left()
                self.initial()

            if keyPressed("c"):
                self.right()
                self.initial()

            if keyPressed("s"):
                self.up()
                self.initial()

            if keyPressed("x"):
                self.down()
                self.initial()


    def left(self):
        #Move Left

        self.xSpeed = -4
        self.xPos += self.xSpeed
        moveSprite(self.image, self.xPos, self.yPos)
        if self.xPos < 56.0:
            self.xPos = 56.0

    def right(self):
        #Move Left
        self.xSpeed = +4
        self.xPos += self.xSpeed
        moveSprite(self.image, self.xPos, self.yPos)
        if self.xPos > 760:
            self.xPos = 760


    def quickLeft(self):
        #Move left quickly
        self.xSpeed = -8
        self.xPos += self.xSpeed
        moveSprite(self.image, self.xPos, self.yPos)



    def quickRight(self):
        #Move right quickly
        self.xSpeed = 8
        self.xPos += self.xSpeed
        moveSprite(self.image, self.xPos, self.yPos)

    
    def up(self):
        #Move up
        self.ySpeed = 5
        self.yPos  -= self.ySpeed
        moveSprite(self.image, self.xPos, self.yPos)
        showSprite(self.image)
        if self.yPos < 56.0:
            self.yPos = 56.0
    def quickUp(self):
        #Faster upward movement

        self.ySpeed = 8
        self.yPos -= self.ySpeed
        moveSprite(self.image, self.xPos, self.yPos)
        showSprite(self.image)

    def down(self):
        #Move down
        self.ySpeed = 5
        self.yPos += self.ySpeed
        moveSprite(self.image, self.xPos, self.yPos)
        showSprite(self.image)
        if self.yPos > 420:
            self.yPos = 420

    def live(self):
        # xp and hp

        self.hp = 100
        self.xp = 100




