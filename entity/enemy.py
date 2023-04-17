import pygame
import sys
import var
from entity import entity
pygame.init()


class Enemy(entity.Entity):
    def __init__(self,x,y,width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def draw(self, window):
        pygame.draw.rect(window, (250,250,250), (self.x,self.y,self.width,self.height))
    def movement(self, player, vel):
        if player.x > var.screenwidth or player.y > var.screenheight:
            vel=vel*1.5
        if player.x <self.x and self.x>vel: 
            self.x-=vel
        if player.x>self.x:
            self.x+=vel
        if player.y <self.y  and self.y>vel:
            self.y-=vel
        if player.y >self.y:
            self.y+=vel
        




