from Player import*

hieL = makeSprite(os.path.join("images", "Hie1.png"))
hieR = makeSprite(os.path.join("images", "HieR1.png"))
imageListH = [hieL, hieR]

class Hie(Player):

    def __init__(self, image, xPos, yPos,  xSpeed, ySpeed):
        super().__init__(self, xPos, yPos, xSpeed, ySpeed)
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

