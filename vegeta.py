from Player import*


base = 400

p1Pos = 100
p2Pos = 200

vegetaStance = makeSprite(os.path.join("images", "vegeta_stand.png"))
vegetaStanceR = makeSprite(os.path.join("images", "vegeta_standR.png"))
imageListV = [vegetaStance, vegetaStanceR]

class Vegeta(Player):

    def __init__(self, image, xPos, yPos,  xSpeed, ySpeed, xp):
        super().__init__(self, xPos, yPos, xSpeed, ySpeed, xp)
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.xp = xp




VEGP1 = Vegeta(imageListV[0], p1Pos, base,  2, 2, 0)
VEGP2 = Vegeta(imageListV[-1], p2Pos, base,  2, 2, 0)






















