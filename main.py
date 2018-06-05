from pygame_functions import*
screenSize(900,500)
Red = (255, 0, 0)
Green = (0,255,0)
Blue = (0, 0 , 255)
Black = (0,0,0)
White = (255, 255, 255)
Yellow = (255, 255, 0)
pic1 = makeSprite(os.path.join("images","vegeta_stand.png"))
pic2 = makeSprite(os.path.join("images","hie1.png"))
shots = makeSprite(os.path.join("images","blaster.png"))
blast = makeSprite(os.path.join("images","vegexplode.png"))
vegetakick = makeSprite(os.path.join("images","vegeta_kick.png"))
blast2 = makeSprite(os.path.join("images","blaster.png"))
vegshot1 = makeSprite(os.path.join("images","vegetashot1.png"))
vegshot2 = makeSprite(os.path.join("images","vegetashot2.png"))
vegshot3 = makeSprite(os.path.join("images","vegetashot3.png"))
vegshot4 = makeSprite(os.path.join("images","vegetashot4.png"))
hieattack1 =makeSprite(os.path.join("images","hie2R.png"))
hieattack2 = makeSprite(os.path.join("images","hie3R.png"))
hieattack3 = makeSprite(os.path.join("images","hie4R.png"))
drFist1= makeSprite(os.path.join("images","hieDragon1R.png"))
drFistList = [makeSprite(os.path.join("images","hieDragon1R.png")),
makeSprite(os.path.join("images","hieDragon2R.png")),
makeSprite(os.path.join("images","hieDragon3R.png")),
makeSprite(os.path.join("images","hieDragon4R.png")),
makeSprite(os.path.join("images","hieDragon5R.png")),
makeSprite(os.path.join("images","hieDragon6R.png")),
makeSprite(os.path.join("images","hieDragon7R.png"))]
hieRight = makeSprite(os.path.join("images","hieR1.png"))
bg = setBackgroundImage(os.path.join("images","Background-1.png"))
blastSound = makeSound(os.path.join("sounds","kiblast.wav"))
darkness = makeSound(os.path.join("sounds","darknessFlame.wav"))
music = makeSound(os.path.join("sounds","Music1.wav"))
v = pygame.sprite.Group()
vegShootList = [vegshot1,vegshot2,vegshot3,vegshot4]
#vegShoot = [makeSprite("vegshot1.png"),makeSprite("vegshot2.png"),makeSprite(
 #           "vegshot3.png"), makeSprite("vegshot4.png"),]

class Sprite():
    def __init__(self,xPos,yPos,xSpeed,ySpeed,img):
        #initializes parameters for positions and image of Sprites
        self.xPos = xPos
        self.yPos = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.img = img



    def pos(self):
        #defines positions for Sprites
        moveSprite(self.img,self.xPos,self.yPos,False)
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)

    def damage(self):
        p1.xPos = p1.xPos - 20


class HP(Sprite):
    def __init__(self,life,stamina,color):
        self.life = life
        self.stamina = stamina
        self.color = color

    def smallHit(self):
        self.life -= 5
        self.stamina -= 2


    def bigHit(self):

        self.life -= 10
        self.stamina -= 4


class P1(Sprite):

    def __init__(self,xPos, yPos, xSpeed, ySpeed,img):
        Sprite.__init__(self,xPos, yPos, xSpeed, ySpeed,img)


        #Movement for p1

    def up(self):
        #Move up
        self.ySpeed = 10
        self.yPos  -= self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        if self.yPos < 56.0:
            self.yPos = 56.0
    def quickUp(self):
        #Faster upward movement

        self.ySpeed = 20
        self.yPos -= self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)

    def down(self):
        #Move down
        self.ySpeed = 10
        self.yPos += self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        if self.yPos > 420:
            self.yPos = 420

    def quickDown(self):
        #Move Down quickly
        self.ySpeed = 20
        self.yPos += self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)



    def left(self):
        #Move Left
        self.xSpeed = -10
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)
        if self.xPos < 56.0:
            self.xPos = 56.0

    def quickLeft(self):
        #Move left quickly
        self.xSpeed = -20
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)

    def right(self):
        #Move right
        self.xSpeed = 10
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)
        print(self.xPos)
        if self.xPos > 760:
            self.xPos = 760


    def quickRight(self):
        #Move right quickly
        self.xSpeed = 20
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)


    def shoot(self):
        #shooting
        #for i in range(90):

        self.xSpeed = 280
        self.xPos = p1.xPos - 20
        showSprite(p1Blast)

        for i in range(self.xSpeed):
            p1.xPos += i
            moveSprite(p1.blast2, p1.xPos, p1.yPos)

            if self.xPos > p2.xPos:
                self.yPos -= 300

        if self.xPos > 700:
            killSprite(self.img)
        self.xPos = p1.xPos
        self.yPos = p1.yPos


    def vegShootPos(self):
        global vegShootList
        for pics in vegShootList:
            moveSprite(pics,p1.xPos,p1.yPos,False)
            showSprite(pics)
            killSprite(pics)
            if pics == vegShootList[:-1]:
                vegShootList = []
                v.remove(pics)
                v = []


        print("shooter" + str(p1.xPos))
        print(p1.yPos)

    def blast(self):
        killSprite(self.img)
        moveSprite(blast,self.xPos,self.yPos - 70,False)
        showSprite(blast)
        pause(100)
        showSprite(self.img)
        killSprite(blast)
        showSprite(self.img)
        print("blast" + str(self.xPos))
        print(self.yPos)
        print("veg x:" + str(p1.xPos))


    def kick(self):
        killSprite(self.img)
        moveSprite(self.img,self.xPos,self.yPos,False)
        showSprite(vegetakick)
        moveSprite(vegetakick,self.xPos + 4,self.yPos)
        moveSprite(self.img,self.xPos,self.yPos,False)
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        showSprite(vegetakick)
        killSprite(vegetakick)


class P2(Sprite):

    def __init__(self,xPos, yPos, xSpeed, ySpeed,img):
        Sprite.__init__(self,xPos, yPos, xSpeed, ySpeed,img)

        #Movement for P2
    def up(self):
        self.ySpeed = 10
        self.yPos  -= self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        if self.yPos < 56.0:
            self.yPos = 56.0
        if self.yPos < 10:
            self.yPos = 10
            print(self.yPos)

    def quickUp(self):
        self.ySpeed = 20
        self.yPos -= self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)


    def down(self):
        self.ySpeed = 10
        self.yPos += self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)

        if self.yPos > 420:
            self.yPos = 420

    def quickDown(self):
        self.ySpeed = 20
        self.yPos += self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)



    def left(self):
        self.xSpeed = -10
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)
        print("hie" + str(p2.xPos))
        print(self.yPos)

        if self.xPos < 56.0:
            self.xPos = 56.0

    def quickLeft(self):
        self.xSpeed = -20
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)

    def right(self):
        self.xSpeed = 10
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)
        if self.xPos > 760:
            self.xPos = 760


    def quickRight(self):
        self.xSpeed = 20
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)


    def dragonFist(self):
        global drFistList
        global pics

        killSprite(pic2)

        for pics in drFistList:

            moveSprite(pics,p2.xPos,p2.yPos,False)
            showSprite(pics)
            pause(20)
            n = [str(pics)]
            killSprite(pics)
            pics.xPos = 400000
            print(n)
            pics.kill()
            if pics == drFistList[:-1]:
                print('empty')
                drFistList = []



    def slice(self):
        self.xPos = p2.xPos
        self.yPos = p2.yPos

        killSprite(self.img)
        moveSprite(hieattack1,self.xPos,self.yPos,False)
        showSprite(hieattack1)
        moveSprite(hieattack1,self.xPos + 4,self.yPos)
        killSprite(hieattack1)
        moveSprite(hieattack2,self.xPos,self.yPos,False)
        showSprite(hieattack2)
        moveSprite(hieattack2,self.xPos + 4,self.yPos)
        killSprite(hieattack2)
        moveSprite(hieattack3,self.xPos,self.yPos,False)
        showSprite(hieattack3)
        moveSprite(hieattack3,self.xPos + 4,self.yPos)
        killSprite(hieattack3)




    def damage(self):
        self.xPos = self.xPos + 20
        if self.xPos >940:
            self.xPos = 940

        if self.xPos < 56.0:
            self.xPos = 56.0

    def boundary(self):
        if self.xPos < p1.xPos:
            self.xPos += 20
            p1.xPos -= 20




class Bullet(P1):
    def __init__(self,xPos,yPos,xSpeed,ySpeed,img):
        #initializes parameters for positions and image of Sprites
        self.xPos = p1.xPos
        self.yPos = p1.yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.img = shots

    def update(self):
        self.xPos += self.xSpeed
        moveSprite(self.img,self.xPos,self.yPos,False)
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        killSprite(self.img)

        if p2.xPos < 400:
            self.xPos = p1.xPos + shooter.xSpeed

        if self.xPos > 600:
            killSprite(self.img)
            self.xPos = p1.xPos
            self.yPos = p1.yPos
        elif self. xPos < 600:
            self.xPos + p1.xSpeed



#p1Controls = P1()
p1 = P1(200,320,1,1,pic1)
p2 = P2(700, 320, 1,1,pic2)
p1HP = HP(100,10,Green)
p2HP = HP(100,10,Green)
p1shots = P1(210, 310,1,1,shots)
p1Blast = P1(205,320,1,1,blast)
p2Blast = P2(690,310,1,1,blast2)
shooter = Bullet(210, 310,140,1,shots)
