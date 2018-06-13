from Player import*


base = 400

p1Pos = 100
p2Pos = 200

hieL = makeSprite(os.path.join("images", "Hie1.png"))
hieR = makeSprite(os.path.join("images", "HieR1.png"))


imageListH = [hieL, hieR]

class Hie(Player):

    def __init__(self, image, xPos, yPos,  xSpeed, ySpeed, hp, xp):
        super().__init__(self, xPos, yPos, xSpeed, ySpeed, hp, xp)
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.hp = hp
        self.xp = xp

HIEP1 = Hie(imageListH[0], p1Pos, base, 5,  5, 100, 0)
HIEP2 = Hie(imageListH[-1], p2Pos, base, 5,  5, 100, 0)


