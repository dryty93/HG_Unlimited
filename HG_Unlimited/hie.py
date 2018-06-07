from Player import*

hieL = makeSprite(os.path.join("images", "Hie1.png"))
hieR = makeSprite(os.path.join("images", "HieR1.png"))
imageListH = [hieL, hieR]

class Hie(Player):

    def __init__(self, image, xPos, yPos, velocity):
        super().__init__(self, xPos, yPos, velocity)
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.velocity = velocity




    def fPlay(self):

        moveSprite(imageListH[-1], 100, 100, True)
        moveSprite(imageListH[-1], 100, 100)
        showSprite(imageListH[-1])



    def sPlay(self):
        moveSprite(imageListH[0],400, 100, True)
        moveSprite(imageListH[0], 400, 100)
        showSprite(imageListH[0])
