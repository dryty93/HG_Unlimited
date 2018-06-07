from Player import*
from os import path





vegetaStance = makeSprite(os.path.join("images", "vegeta_stand.png"))
vegetaStanceR = makeSprite(os.path.join("images", "vegeta_standR.png"))
imageListV = [vegetaStance, vegetaStanceR]

class Vegeta(Player):

    def __init__(self, image, xPos, yPos):
        super().__init__(self, xPos, yPos)
        self.image = image
        self.xPos = xPos
        self.yPos = yPos

    def fPlay(self):
        moveSprite(imageListV[0], 100, self.yPos, True)
        showSprite(imageListV[0])
    def sPlay(self):
        moveSprite(imageListV[-1],400, 100, True)
        showSprite(imageListV[-1])






















