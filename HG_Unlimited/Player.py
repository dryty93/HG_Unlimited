from pygame_functions import *

screenSize(500, 800)


class Player():

    def __init__(self, image, xPos, yPos):
        self.image = image
        self.xPos = xPos
        self.yPos = yPos

    def playerSide(self):
        pass


    def spawn(self):
        pass

    def animate(self):
        moveSprite(self.image, self.xPos, self.yPos, True)
        showSprite(self.image)

    def gravity(self):
        pass

    def moves(self):
        pass