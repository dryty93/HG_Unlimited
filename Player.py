from pygame_functions import *
from os import path

screenSize(800, 600)


class Player():

    def __init__(self, image, xPos, yPos, xSpeed, ySpeed, fP = False, sP = False):
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.fP = fP
        self.sP = sP

    def spawn(self):
        pass

    def animate(self):
        moveSprite(self.image, self.xPos, self.yPos, True)
        showSprite(self.image)

    def gravity(self):
        pass

    def fPlay(self):
        """Moves player instance into position for first place"""
        moveSprite(self.image, self.xPos, self.yPos)
        showSprite(self.image)
        nextSpriteImage(self.image)
        self.fP = 2 > 1
        if self.fP:
            # Moves for fPlayer

            if keyPressed("left"):
                self.left()
            if keyPressed("right"):
                self.right()




    def sPlay(self):
        """Moves player instance into position for 2nd place"""
        moveSprite(self.image, self.xPos, self.yPos)
        showSprite(self.image)
        nextSpriteImage(self.image)

        self.fP = 2 > 1

        if self.fP:

            if keyPressed("z"):
                self.left()
            if keyPressed("c"):
                self.right()

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
        if self.xPos < 56.0:
            self.xPos = 56.0



