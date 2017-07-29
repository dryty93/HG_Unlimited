from pygame_functions import*
screenSize(900,500)
Red = (255, 0, 0)
Green = (0,255,0)
Blue = (0, 0 , 255)
Black = (0,0,0)
White = (255, 255, 255)
Yellow = (255, 255, 0)
pic1 = makeSprite("vegeta_stand.png")
pic2 = makeSprite("hie1.png")
shots = makeSprite("blaster.png")
shots2 = makeSprite("laserRed08.png")
blast = makeSprite("vegexplode.png")
vegetakick = makeSprite("vegeta_kick.png")
blast2 = makeSprite("blaster.png")
vegshot1 = makeSprite("vegetashot1.png")
vegshot2 = makeSprite("vegetashot2.png")
vegshot3 = makeSprite("vegetashot3.png")
vegshot4 = makeSprite("vegetashot4.png")
hieattack1 =makeSprite("hie2R.png")
hieattack2 = makeSprite("hie3R.png")
hieattack3 = makeSprite("hie4R.png")
drFist1= makeSprite("hieDragon1R.png")
drFist2= makeSprite("hieDragon2R.png")
drFist3= makeSprite("hieDragon3R.png")
drFist4= makeSprite("hieDragon4R.png")
drFist5= makeSprite("hieDragon5R.png")
drFist6= makeSprite("hieDragon6R.png")
drFist7= makeSprite("hieDragon7R.png")
hieRight = makeSprite("hieR1.png")
bg = setBackgroundImage("Background-1.png")
blastSound = makeSound("kiblast.wav")
darkness = makeSound("darknessFlame.wav")
music = makeSound("Music1.wav")
v = pygame.sprite.Group()
v.add(vegshot1)
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
        pass

       
        
class P1(Sprite):

    def __init__(self,xPos, yPos, xSpeed, ySpeed,img):
        Sprite.__init__(self,xPos, yPos, xSpeed, ySpeed,img)

        
        #Movement for p1
        
    def up(self):
        #Move up
        self.ySpeed = 5
        self.yPos  -= self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        if self.yPos < 56.0:
            self.yPos = 56.0
    def quickUp(self):
        #Faster upward movement

        self.ySpeed = 8
        self.yPos -= self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
    
    def down(self):
        #Move down
        self.ySpeed = 5
        self.yPos += self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        if self.yPos > 420:
            self.yPos = 420

    def quickDown(self):
        #Move Down quickly
        self.ySpeed = 8
        self.yPos += self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        


    def left(self):
        #Move Left
        self.xSpeed = -4
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)
        if self.xPos < 56.0:
            self.xPos = 56.0

    def quickLeft(self):
        #Move left quickly
        self.xSpeed = -8
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)

    def right(self):
        #Move right
        self.xSpeed = 5
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)
        print(self.xPos)
        if self.xPos > 760:
            self.xPos = 760

    
    def quickRight(self):
        #Move right quickly
        self.xSpeed = 8
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)
        

    def shoot(self):
        #shooting
        #for i in range(90):
        
        
        self.xSpeed = 280
        self.xPos += self.xSpeed
        self.yPos += self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)

        if self.xPos > 700:
            killSprite(self.img)
        self.xPos = p1.xPos
        self.yPos = p1.yPos

    def shootUpdate(self):
        killSprite(self.img)
        moveSprite(vegshot1,self.xPos,self.yPos,False)
        showSprite(vegshot1)
        moveSprite(vegshot1,self.xPos + 4,self.yPos)
        moveSprite(self.img,self.xPos,self.yPos,False)
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        showSprite(vegshot1)
        killSprite(vegshot1)
        killSprite(self.img)
        moveSprite(self.img,self.xPos,self.yPos,False)
        showSprite(vegshot2)
        moveSprite(vegshot2,self.xPos + 4,self.yPos)
        moveSprite(self.img,self.xPos,self.yPos,False)
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        showSprite(vegshot2)
        killSprite(vegshot2)
        moveSprite(self.img,self.xPos,self.yPos,False)
        showSprite(vegshot3)
        moveSprite(vegshot3,self.xPos + 4,self.yPos)
        moveSprite(self.img,self.xPos,self.yPos,False)
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        showSprite(vegshot3)
        killSprite(vegshot3)
        moveSprite(self.img,self.xPos,self.yPos,False)
        showSprite(vegshot4)
        moveSprite(vegshot4,self.xPos + 4,self.yPos)
        moveSprite(self.img,self.xPos,self.yPos,False)
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        showSprite(vegshot4)
        killSprite(vegshot4)
        
    def blast(self):
        killSprite(self.img)
        moveSprite(blast,self.xPos,self.yPos - 70,False)
        showSprite(blast)
        pause(100)
        killSprite(blast)
        showSprite(self.img)

        
		
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
        self.ySpeed = 5
        self.yPos  -= self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        if self.yPos < 56.0:
            self.yPos = 56.0
        if self.yPos < 10:
            self.yPos = 10
            print(self.yPos) 

    def quickUp(self):
        self.ySpeed = 8
        self.yPos -= self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)


    def down(self):
        self.ySpeed = 5
        self.yPos += self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        print(self.yPos)
        print(self.xPos)
        if self.yPos > 420:
            self.yPos = 420

    def quickDown(self):
        self.ySpeed = 8
        self.yPos += self.ySpeed
        moveSprite(self.img, self.xPos, self.yPos)
        showSprite(self.img)
        


    def left(self):
        self.xSpeed = -4
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)
        print(self.xPos)
        if self.xPos < 56.0:
            self.xPos = 56.0

    def quickLeft(self):
        self.xSpeed = -8
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)

    def right(self):
        self.xSpeed = 5
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)
        if self.xPos > 760:
            self.xPos = 760

    
    def quickRight(self):
        self.xSpeed = 8
        self.xPos += self.xSpeed
        moveSprite(self.img, self.xPos, self.yPos)
        

    def dragonFist(self):
        
        killSprite(self.img)
        moveSprite(drFist1,self.xPos,self.yPos,False)
        showSprite(drFist1)
        pause(100,allowEsc = True)
        moveSprite(drFist1,self.xPos + 30,self.yPos)
        killSprite(drFist1)
        moveSprite(drFist2,self.xPos,self.yPos,False)
        showSprite(drFist2)
        pause(100,allowEsc = True)
        moveSprite(drFist2,self.xPos + 10,self.yPos)
        killSprite(drFist2)
        moveSprite(drFist3,self.xPos,self.yPos,False)
        showSprite(drFist3)
        pause(100,allowEsc = True)
        moveSprite(drFist3,self.xPos - 30,self.yPos)
        killSprite(drFist3)
        moveSprite(drFist4,self.xPos - 50,self.yPos,False)
        showSprite(drFist4)
        pause(100,allowEsc = True)
        moveSprite(drFist4,self.xPos + 200,self.yPos)
        killSprite(drFist4)
        moveSprite(drFist5,self.xPos - 50,self.yPos,False)
        showSprite(drFist5)
        pause(100,allowEsc = True)
        moveSprite(drFist5,self.xPos - 60,self.yPos)
        killSprite(drFist5)
        moveSprite(drFist6,self.xPos - 50,self.yPos,False)
        showSprite(drFist6)
        pause(30,allowEsc = True)
        moveSprite(drFist6,self.xPos - 90,self.yPos)
        killSprite(drFist6)
        moveSprite(drFist7,self.xPos,self.yPos,False)
        showSprite(drFist7)
        pause(30,allowEsc = True)
        moveSprite(drFist7,self.xPos - 80,self.yPos)
        killSprite(drFist7)
        
        
        
        

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
        pause(100,allowEsc = True)
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
p2shots = P2(690,310,1,1,shots2)
p2Blast = P2(690,310,1,1,blast2)
shooter = Bullet(210, 310,140,1,shots)
