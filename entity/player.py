import pygame
import sys
import var
import math
pygame.init()



class Player:
    def __init__(self, x,y,width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.bullets=[]
    def draw_player(self, window):
        pygame.draw.rect(window, (0,0,0), (self.x,self.y,self.width,self.height))
    def movement(self, keys, vel):
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            vel=vel*1.5
        if keys[pygame.K_a]and self.x>vel: 
            self.x-=vel
        if keys[pygame.K_d]:
            self.x+=vel
        if keys[pygame.K_w]  and self.y>vel:
            self.y-=vel
        if keys[pygame.K_s]:
            self.y+=vel
        
class PlayerBullet:
    def __init__(self,x,y, mouse_x,mouse_y):
        self.x=x
        self.y=y
        self.mouse_x=mouse_x
        self.mouse_y=mouse_y
        self.speed=15
        self.angle=math.atan2(y-mouse_y,x-mouse_x)
        self.x_vel=math.cos(self.angle)*self.speed
        self.y_vel=math.sin(self.angle)*self.speed
    def main(self, win):
        self.x-=int(self.x_vel)
        self.y-=int(self.y_vel)
        pygame.draw.circle(win, (255,0,0),(self.x, self.y), var.screenwidth/150)




