import pygame
import sys
import var
pygame.init()
from entity import entity


class Player(entity.Entity):
    def __init__(self, x,y,width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def draw(self, window):
        pygame.draw.rect(window, (0,0,0), (self.x,self.y,self.width,self.height))
    def movement(self, keys, vel):
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            vel=vel*1.5
        if keys[pygame.K_a]and self.x>0: 
            self.x-=vel
        if keys[pygame.K_d] and self.x < var.screenwidth-self.width:
            self.x+=vel
        if keys[pygame.K_w]  and self.y>0:
            self.y-=vel
        if keys[pygame.K_s]and self.y < var.screenheight-self.height:
            self.y+=vel
        




