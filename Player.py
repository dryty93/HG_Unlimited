from pygame_functions import *
from os import path

screenSize(800, 600)


class Player():

    def __init__(self, image, xPos, yPos, xSpeed, ySpeed):
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

    def playerSide(self):
        pass


    def spawn(self):
        pass

    def animate(self):
        moveSprite(self.image, self.xPos, self.yPos, True)
        showSprite(self.image)

    def gravity(self):
        pass

    def left(self):
        # Move Left
        self.xPos += self.velocity
        moveSprite(self.image, self.xPos, self.yPos, True)
        moveSprite(self.image, self.xPos, self.yPos)
        print('triggered')


    def fPlay(self):
        """Moves player instance into position for first place"""
        moveSprite(self.image, self.xPos, self.yPos)
        showSprite(self.image)
        nextSpriteImage(self.image)

        # 800 600

    def sPlay(self):
        """Moves player instance into position for 2nd place"""
        moveSprite(self.image, self.xPos, self.yPos)
        showSprite(self.image)
        nextSpriteImage(self.image)

    def left(self):
        #Move Left

        self.xPos -= self.xSpeed
        moveSprite(self.image, self.xPos, self.yPos)
        if self.xPos < 56.0:
            self.xPos = 56.0




