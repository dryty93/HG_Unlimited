from Player import*
from os import path


hieL = makeSprite(os.path.join("images", "Hie1.png"))
hieR = makeSprite(os.path.join("images", "HieR1.png"))
imageListH = [hieL, hieR]

class Hie(Player):

    def __init__(self, image, xPos, yPos):
        super().__init__(self, xPos, yPos)
        self.image = image
        self.xPos = xPos
        self.yPos = yPos


    def fPlay(self):
        moveSprite(imageListH[-1], 100, self.yPos, True)
        showSprite(imageListH[-1])
    def sPlay(self):
        moveSprite(imageListH[0],400, 100, True)
        showSprite(imageListH[0])
