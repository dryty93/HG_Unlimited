"""
Title: "Hell Games"
Author:tylerJDryden
7/7/2017
    """
from pygame_functions import*
#from start import*
from music1 import*
screenSize(1000,750)
p_uno_image = makeSprite("vegeta_standR.png")
p_dos_image = makeSprite("vegeta_stand.png")
shots = makeSprite("laserRed08.png")
moreShots = makeSprite("laserBlue08.png")
blast = makeSprite("trail_00.png")
blast2 = makeSprite("trail_00.png")


xPos = 500
yPos = 320
xPos_2 = 320
yPos_2 = 300
ySpeed_2, xSpeed_2 = 0,0 
xSpeed = 0
ySpeed = 0
width = 1000
height = 750
b_xPos = 10
b_yPos = xPos
b_xSpeed = 1
b_ySpeed  = 1



#p_uno_image(

#screen = pygame.display.set_mode((1000,750))
                                 
class Game():

    
    def __init__(self):
        pass
        

    def update(self):
        screenSize(1000,750)
        bg = setBackgroundImage("Background-1.png")
        title = makeLabel("Hell Games", 60, 350, 10, "yellow")

        showLabel(title)
      #  return screenSize



    def controls(self):
        #defines the game loop and controls for p1
         global bullets
         global moreShots
         global pic
         global pic2
         global xPos
         global yPos
         global xSpeed
         global ySpeed
         global xPos_2
         global yPos_2
         global xSpeed_2
         global ySpeed_2
         global p1_Hp
         global p2_Hp

         p1_Hp = 100
         p2_Hp = 100

         while True :
            #P2 Up
 
             if keyPressed("q"):
                 rotateSprite(p_dos_image,0)
                 ySpeed_2 = -10
                 yPos_2 += ySpeed_2

            #P2 Down
             elif keyPressed("a"):
                 rotateSprite(p_dos_image,180)
                 ySpeed_2 = 10
                 yPos_2 += ySpeed_2
            # P2 Right

             if keyPressed("d"):
                rotateSprite(p_dos_image,0)
                xSpeed_2 = 1
                xPos_2 += 5
            # P2 Left
             if keyPressed("s"):
                 rotateSprite(p_dos_image,0)
                 xSpeed_2 -= 1
                 xPos_2 -= 5
            

                 
                 
                
             elif keyPressed("space"):
                 p2.shoot()

                 

            #P1 Controls

             if keyPressed("up"):
                 rotateSprite(p_uno_image,0)
                 ySpeed = 30
                 yPos += -5.5
        
             if keyPressed("p"):
                 p1.shoot()
        
             elif keyPressed("down"):
                 rotateSprite(p_uno_image,180)
                 ySpeed += 6
                 yPos += ySpeed

             elif keyPressed("right"):
                 rotateSprite(p_uno_image,0)
                 xSpeed += 1
                 xPos += 5
        

             elif keyPressed("left"):
                 rotateSprite(p_uno_image, 0)
                 xSpeed -= 1
                 xPos -= 5
            
             
                          
             elif keyPressed("down") and keyPressed ("0"):
                 shooter = showSprite(blast)
                 rotateSprite(blast, 90)
                 moveSprite(blast,xPos - 20, yPos + 200,True)
                 moveSprite(blast,xPos - 20, yPos - 200)
                 if touching(blast, p_dos_image):
                      killSprite(blast)
                      p1_Hp -= 10
                      print("P2:",p1_Hp)
                      print("P1:", p2_Hp)
                      xPos_2 -= 50
                      if p1_Hp == 0:
                          updateDisplay()
                          pygame.quit()
             elif keyPressed("up") and keyPressed ("0"):
                  shooter = showSprite(blast)
                  rotateSprite(blast, -90)
                  moveSprite(blast,xPos - 20, yPos + 200,True)
                  moveSprite(blast,xPos - 20, yPos - 200)
                  if touching(blast, p_dos_image):
                       killSprite(blast)
                       p1_Hp -= 10
                       print("P2:",p1_Hp)
                       print("P1:", p2_Hp)
                       xPos_2 -= 50
                       if p1_Hp == 0:
                           updateDisplay()
                           pygame.quit()
                                      
             elif keyPressed("a") and keyPressed ("8") or keyPressed("q") and keyPressed("8"):
                 shooter = showSprite(blast2)
                 rotateSprite(blast2, -90)
                 moveSprite(blast2,xPos_2 - 20, yPos_2 + 200,True)
                 moveSprite(blast2,xPos_2 - 20, yPos_2 - 200)
                 if touching(blast2, p_uno_image):
                      killSprite(blast2)
                      p2_Hp -= 10
                      print("P2:",p1_Hp)
                      print("P1:", p2_Hp)
                      xPos_2 -= 50
                      if p2_Hp == 0:
                          updateDisplay()
                          pygame.quit()
             
                                       
                                           
                 #if i > 300:
                  #   killSprite(blast)
             elif keyPressed("0") and ("left"):
                  i = 700
                  shooter = showSprite(blast)
                  rotateSprite(blast, 180)
                  moveSprite(blast,xPos + 30, yPos + 30,True)
                  moveSprite(blast,xPos - 550, yPos - 30 )
                  if touching(blast, p_dos_image):
                      killSprite(blast)
                      p1_Hp -= 10
                      print("P2:",p1_Hp)
                      print("P1:", p2_Hp)
                      xPos_2 -= 50
                      if p1_Hp == 0:
                          updateDisplay()
                          pygame.quit()


             elif keyPressed("8"):
                 shooter = showSprite(blast2)
                 rotateSprite(blast2,360)
                 moveSprite(blast2,xPos_2 , yPos_2 ,True)
                 moveSprite(blast2,xPos_2, yPos_2)
                 if touching(blast2, p_uno_image):
                     killSprite(blast2)
                     p2_Hp -= 10
                     print("P2:",p1_Hp)
                     print("P1:", p2_Hp)
                     xPos += 50
                     if p2_Hp == 0:
                         updateDisplay()
                         pygame.quit()

             if touching(blast,blast2):
                 killSprite(blast)
                 killSprite(blast2)
            
              
                      
                      



                     

             if xPos > 900: 
                xPos =900
             if xPos < 15:
                 xPos = 15
             if yPos < 56.0:
                 yPos = 56.0
             if yPos > 660.0:
                 yPos = 660.0

             if xPos_2 > 900: 
                xPos_2 =900
             if xPos_2 < 15:
                 xPos_2 = 15
             if yPos_2 < 56.0:
                 yPos_2 = 56.0
             if yPos_2 > 660.0:
                 yPos_2 = 660.0
             
             if touching(p_dos_image,shots):
                 print(0 + 1)
                 print("P2:",p1_Hp)
                 print("P1:", p2_Hp)
                 updateDisplay()
                 p1_Hp -= 2
                 xPos_2 -= 50
                 
                 
             if p1_Hp <= 0:
                 p1_Hp == 0
                 end()
                 updateDisplay()
                 
             
             if touching(p_uno_image,moreShots):
                  print("P1:",p2_Hp)
                  print("P2:", p1_Hp)
                  updateDisplay()
                  p2_Hp -= 2
                  xPos -= 50

          
             if touching(shots, moreShots):
                killSprite(shots)
                killSprite(moreShots)
                updateDisplay()
             
             if p2_Hp == 0:
                 pygame.quit()
                 updateDisplay()
                 
             
             moveSprite(p_uno_image, xPos, yPos)
             moveSprite(p_dos_image, xPos_2, yPos_2)


             tick(60)
          

    def damage():
        player_1_Hp -= 5

class Player1(Game):

    def __init__(self):
        #Loads image to screen
       # screen = pygame.display.set_mode((800, 600))
        pic =showSprite(p_uno_image)
        moveSprite(p_uno_image,0, 0, True)
        moveSprite(p_uno_image,300,300,True)
        moveSprite(p_uno_image, xPos, yPos)

    def update(self):
        
        # sets its x and y coordinates
        xPos = 500
        yPos = 320
        xSpeed = 0
        ySpeed = 0
        p1_Hp = str(100)
        p1_Life = makeLabel("P1 HP:" + p1_Hp, 40, 10, 10, "blue")
        showLabel(p1_Life)
        
        

    
        
    def shoot(self):
        global xPos
        global yPos
        bullPoint_x = xPos + 50
        bullPoint_y = yPos 

        #Shoots for p1
        bullet = showSprite(shots)
        moveSprite(shots,xPos, yPos,True)
        moveSprite(shots,xPos, yPos)
        #print(bullPoint_x)
        #if bullPoint_x > xPos :
            
         #   killSprite(shots)
          #  updateDisplay()

    
class Player2(Game):

    def __init__(self):
        pass
    # Loads p2 image to screen
    def update(self):
        xPos_2 = 320
        yPos_2 = 300
        ySpeed_2, xSpeed_2 = 0,0
        pic2 = showSprite(p_dos_image)
        moveSprite(p_dos_image, xPos_2, yPos_2)
        p2_Hp = str(100)
        p2_Life = makeLabel("P2 HP:" + p2_Hp, 40, 700,10, "red")
        showLabel(p2_Life)
        
        
             
    def shoot(self):
        # shoots for p2
       bullet = showSprite(moreShots)
       moveSprite(moreShots,xPos_2 , yPos_2,True)
       moveSprite(moreShots, xPos_2,  yPos_2 )
#       print(xPos_2,yPos_2)

       
       
       if xPos and yPos < 0:      
            killSprite(moreShots)
            updateDisplay()
timeDisplay = clock()
gamePlay = Game()
music()
gamePlay.update()
p1 = Player1()
p2 = Player2()
p1.update()
p2.update()
gamePlay.controls()
endWait()

