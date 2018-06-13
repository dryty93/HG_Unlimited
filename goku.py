from Player import*


base = 400

p1Pos = 100
p2Pos = 200

gokuInitL = makeSprite(os.path.join("images", "goku1L.png"))
gokuInitR = makeSprite(os.path.join("images", "goku1R.png"))
# left positions


gokuL = [
    (os.path.join("images", "goku1L.png")),(os.path.join("images","goku2L.png")),
    (os.path.join("images", "goku3L.png")),(os.path.join("images","goku4L.png")),
    (os.path.join("images", "goku5L.png")),(os.path.join("images","goku6L.png")),
    (os.path.join("images", "goku7L.png")), (os.path.join("images", "goku8L.png")),
    (os.path.join("images", "goku9L.png")), (os.path.join("images", "goku10L.png")),
    (os.path.join("images", "goku11L.png")), (os.path.join("images", "goku12L.png")),
    (os.path.join("images","goku13L.png")), (os.path.join("images", "goku14L.png")),
    (os.path.join("images", "goku15L.png")), (os.path.join("images", "goku16L.png")),
    (os.path.join("images", "goku17L.png")),(os.path.join("images", "goku18L.png")),
    (os.path.join("images", "goku19L.png")), (os.path.join("images", "goku20L.png")),
    (os.path.join("images", "goku21L.png")), (os.path.join("images", "goku22L.png")),
    (os.path.join("images", "goku23L.png")), (os.path.join("images", "goku24L.png")),
    (os.path.join("images", "goku25L.png")), (os.path.join("images", "goku26L.png")),
    (os.path.join("images", "goku27L.png")), (os.path.join("images", "goku28L.png")),
    (os.path.join("images", "goku29L.png")), (os.path.join("images", "goku30L.png")),
    (os.path.join("images", "goku31L.png")), (os.path.join("images", "goku32L.png")),
    (os.path.join("images", "goku33L.png")), (os.path.join("images", "goku34L.png")),
    (os.path.join("images", "goku35L.png")),(os.path.join("images", "goku36L.png")),
    (os.path.join("images", "goku37L.png")),(os.path.join("images", "goku38L.png")),
    (os.path.join("images", "goku39L.png")),(os.path.join("images", "goku40L.png")),
    (os.path.join("images", "goku41L.png")),(os.path.join("images", "goku42L.png")),
    (os.path.join("images", "goku43L.png")),(os.path.join("images", "goku44L.png")),
    (os.path.join("images", "goku45L.png")),(os.path.join("images", "goku46L.png")),
    (os.path.join("images", "goku47L.png")),(os.path.join("images", "goku48L.png")),
    (os.path.join("images", "goku49L.png")), (os.path.join("images", "goku50L.png")),
    (os.path.join("images", "goku51L.png")), (os.path.join("images", "goku52L.png")),
    (os.path.join("images", "goku53L.png")), (os.path.join("images", "goku54L.png")),
    (os.path.join("images", "goku55L.png")), (os.path.join("images", "goku56L.png")),
    (os.path.join("images", "goku57L.png")), (os.path.join("images", "goku58L.png")),
    (os.path.join("images", "goku59L.png")), (os.path.join("images", "goku60L.png")),
    (os.path.join("images", "goku61L.png")), (os.path.join("images", "goku62L.png")),
    (os.path.join("images", "goku63L.png")), (os.path.join("images", "goku64L.png")),
    (os.path.join("images", "goku65L.png")), (os.path.join("images", "goku66L.png")),
    (os.path.join("images", "goku67L.png"))]

gokuR =   [
    (os.path.join("images", "goku1R.png")),(os.path.join("images","goku2R.png")),
    (os.path.join("images", "goku3R.png")),(os.path.join("images","goku4R.png")),
    (os.path.join("images", "goku5R.png")),(os.path.join("images","goku6R.png")),
    (os.path.join("images", "goku7R.png")), (os.path.join("images","goku8R.png")),
    (os.path.join("images", "goku9R.png")), (os.path.join("images", "goku10R.png")),
    (os.path.join("images", "goku11R.png")), (os.path.join("images", "goku12R.png")),
    (os.path.join("images","goku13Rpng")), (os.path.join("images", "goku14R.png")),
    (os.path.join("images", "goku15R.png")), (os.path.join("images", "goku16R.png")),
    (os.path.join("images", "goku17R.png")),(os.path.join("images", "goku18R.png")),
    (os.path.join("images", "goku19R.png")), (os.path.join("images", "goku20R.png")),
    (os.path.join("images", "goku21R.png")), (os.path.join("images", "goku22R.png")),
    (os.path.join("images", "goku23R.png")), (os.path.join("images", "goku24R.png")),
    (os.path.join("images", "goku25R.png")), (os.path.join("images", "goku26R.png")),
    (os.path.join("images", "goku27R.png")), (os.path.join("images", "goku28R.png")),
    (os.path.join("images", "goku29R.png")), (os.path.join("images", "goku30R.png")),
    (os.path.join("images", "goku31R.png")), (os.path.join("images", "goku32R.png")),
    (os.path.join("images", "goku33R.png")), (os.path.join("images", "goku34R.png")),
    (os.path.join("images", "goku35R.png")),(os.path.join("images", "goku36R.png")),
    (os.path.join("images", "goku37R.png")),(os.path.join("images", "goku38R.png")),
    (os.path.join("images", "goku39R.png")),(os.path.join("images", "goku40R.png")),
    (os.path.join("images", "goku41R.png")),(os.path.join("images", "goku42R.png")),
    (os.path.join("images", "goku43R.png")),(os.path.join("images", "goku44R.png")),
    (os.path.join("images", "goku45R.png")),(os.path.join("images", "goku46R.png")),
    (os.path.join("images", "goku47R.png")),(os.path.join("images", "goku48R.png")),
    (os.path.join("images", "goku49R.png")),(os.path.join("images", "goku50R.png")),
    (os.path.join("images", "goku51R.png")),(os.path.join("images", "goku52R.png")),
    (os.path.join("images", "goku53R.png")),(os.path.join("images", "goku54R.png")),
    (os.path.join("images", "goku55R.png")),(os.path.join("images", "goku56R.png")),
    (os.path.join("images", "goku57R.png")),(os.path.join("images", "goku58R.png")),
    (os.path.join("images", "goku59R.png")),(os.path.join("images", "goku60R.png")),
    (os.path.join("images", "goku61R.png")),(os.path.join("images", "goku62R.png")),
    (os.path.join("images", "goku63R.png")),(os.path.join("images", "goku64R.png")),
    (os.path.join("images", "goku65R.png")),(os.path.join("images", "goku66R.png")),
    (os.path.join("images", "goku67R.png"))]

gokuAttacks = makeSprite((os.path.join("images", "blaster.png")))


count = 0


print(count)


class Goku(Player):

    def __init__(self, image, xPos, yPos,  xSpeed, ySpeed, xp, sSI = False, sSII = False):
        super().__init__(self, xPos, yPos, xSpeed, ySpeed,xp, sSI, sSII)
        self.image = image
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.sSI = sSI
        self.sSII = sSII
        self.xp = xp




    def superI(self):

        if self.fP:

            if GOKUP1.xp >= 100:

                self.sSI = 2 > 1
               # addSpriteImage(GOKUP1.image, gokuL[12])
                killSprite(GOKUP1.image)
                GOKUP1.image = makeSprite(gokuL[12])


            if GOKUP1.xp < 100:
                self.sSI = 2 < 1
                killSprite(GOKUP1.image)
                GOKUP1.image = makeSprite(gokuL[0])

    def powerUp(self):

        self.xp += 5

        print(self.xp)

    def kamehaL(self):

        if self.fP:

            self.xp -= 20
            print(self.xp)

            if GOKUP1.sSI == False:
                counted = -1

                for items in gokuL[0:10]:
                    counted += 1
                    addSpriteImage(GOKUP1.image, gokuL[counted])
                    pause(50, True)
                    nextSpriteImage(GOKUP1.image)
                showSprite(gokuAttacks)
                moveSprite(gokuAttacks, GOKUP1.xPos + self.xPos, GOKUP1.yPos, False)
                n = GOKUP1.xPos + 400
                for i in range(int(GOKUP1.xPos), int(n)):
                    moveSprite(gokuAttacks, i, self.yPos)
                hideSprite(gokuAttacks)




            else:
                if GOKUP1.sSI:
                    print("SSi")

                    counted = 11

                    for items in gokuL[11:22]:
                        counted += 1
                        addSpriteImage(GOKUP1.image, gokuL[counted])
                        pause(50, True)
                        nextSpriteImage(GOKUP1.image)
                    showSprite(gokuAttacks)
                    moveSprite(gokuAttacks, GOKUP1.xPos + self.xPos, GOKUP1.yPos, False)
                    n = GOKUP1.xPos + 400
                    for i in range(int(GOKUP1.xPos), int(n)):
                        moveSprite(gokuAttacks, i, self.yPos)
                    hideSprite(gokuAttacks)

    def kamehaR(self):
        if self.sP:
            counted = -1
            for items in gokuR[0:10]:
                counted += 1
                addSpriteImage(GOKUP2.image, gokuR[counted])
                pause(50, True)
                nextSpriteImage(GOKUP2.image)
                print(GOKUP2.currentImage)
            showSprite(gokuAttacks)
            moveSprite(gokuAttacks, GOKUP1.xPos + self.xPos, GOKUP1.yPos, False)
            for i in range(400, 100):
                moveSprite(gokuAttacks, i, self.yPos)
            hideSprite(gokuAttacks)


GOKUP1 = Goku(gokuInitL, p1Pos, base, 2,  2, 0)
GOKUP2 = Goku(gokuInitR, p2Pos, base,  2, 2, 0)