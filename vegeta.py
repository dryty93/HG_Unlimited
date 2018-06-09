from Player import*

vegetaStance = makeSprite(os.path.join("images", "vegeta_stand.png"))
vegetaStanceR = makeSprite(os.path.join("images", "vegeta_standR.png"))
imageListV = [vegetaStance, vegetaStanceR]

class Vegeta(Player):

    def __init__(self, image, xPos, yPos,  xSpeed, ySpeed):
        super().__init__(self, xPos, yPos, xSpeed, ySpeed)
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed























