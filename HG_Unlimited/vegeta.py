from Player import*

vegetaStance = makeSprite(os.path.join("images", "vegeta_stand.png"))
vegetaStanceR = makeSprite(os.path.join("images", "vegeta_standR.png"))
imageListV = [vegetaStance, vegetaStanceR]

class Vegeta(Player):

    def __init__(self, image, xPos, yPos, velocity):
        super().__init__(self, xPos, yPos, velocity)
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.velocity

    def fPlay(self):
        moveSprite(imageListV[0], 100, 100, True)
        moveSprite(imageListV[0], 100, 100)
        showSprite(imageListV[0])

        #if keyPressed('a'):
         #   VEGP1.xPos += 30

    def sPlay(self):
        moveSprite(imageListV[-1],400, 100, True)
        moveSprite(imageListV[-1], 400, 100)
        showSprite(imageListV[-1])






















