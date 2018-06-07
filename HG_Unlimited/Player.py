from pygame_functions import *
from os import path

screenSize(500, 800)


class Player():

    def __init__(self, image, xPos, yPos, velocity):
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.velocity = velocity

    def update(self):
        self.xPos += self.velocity
        moveSprite(self.image, self.xPos, self.yPos, False)
        moveSprite(self.image, self.xPos, self.yPos)
        showSprite(self.image)

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
        self.velocity = -4
        self.xPos += self.velocity
        moveSprite(self.image, self.xPos, self.yPos)
        #showSprite(self.image)
        print('triggered')


