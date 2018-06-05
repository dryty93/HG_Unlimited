import pygame
from main import*
Red = (255, 0, 0)
Green = (0,255,0)
Blue = (0, 0 , 255)
Black = (0,0,0)
White = (255, 255, 255)
Yellow = (255, 255, 0)
p1_health = 100
p2_health = 100
p1_stam = 10
p2_stam = 10
p1_health_color = Green
p2_health_color = Green

def health_bars(p1_health, p2_health, p1_stamina, p2_stamina):
    
    if p1HP.life> 75:
        p1_health_color = Green
    elif   p1HP.life > 50:
        p1_health_color = Yellow

    else:   
        p1_health_color = Red

    if p2HP.life > 75:
         p2_health_color = Green
    elif p2HP.life > 50:
        p2_health_color = Yellow

    else:
        p2_health_color = Red
    if p1HP.life < 0:
        end()

    if p2HP.life < 0:
        end()

    if p1HP.stamina == 10:
        p1_stam_color = Red
    else:
        p1_stam_color = Yellow

    if p2HP.stamina == 10:
        p2_stam_color = Red
    else:
        p2_stam_color = Yellow
    
    drawRect(200,20,100,25,p1_health_color,linewidth=0)
    drawRect(200,50,100,10,p1_stam_color,linewidth=0)
    drawRect(680,20,100,25,p2_health_color,linewidth=0)
    drawRect(680,50,100,10,p2_stam_color,linewidth=0)
    
    
