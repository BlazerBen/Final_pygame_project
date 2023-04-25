import pygame
import sys
import var
from pygame.locals import *
from entity import entity
pygame.init()


class Enemy(entity.Entity):
    def __init__(self,x,y,width, height):
        
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.wait=False
        self.show_damage=False
        self.count=0
        self.damage_write=var.write_damage
        self.rect=Rect(self.x,self.y,self.width,self.height)
    def draw(self, window):
        pygame.draw.rect(window, (250,250,250), (self.x,self.y,self.width,self.height))
    def movement(self, player, vel):
        if player.x > var.screenwidth or player.y > var.screenheight:
            vel=vel*1.5
        if player.x+player.width <self.x and self.x>0: 
            self.x-=vel
        if player.x-player.width>self.x and self.x < var.screenwidth-self.width:
            self.x+=vel
        if player.y+player.height<self.y  and self.y>0:
            self.y-=vel
        if player.y-player.height>self.y and self.y < var.screenwidth-self.width:
            self.y+=vel
        self.damage(player)
    def damage(self,player):
        if self.wait:
            self.count+=1
            var.screen.blit(self.damage_write, (self.x-15, self.y-15))
            if self.count==2:
                var.screen.blit(self.damage_write, (self.x-15, self.y-15))
                self.wait==False
                self.count=0
        else:
            if self.rect.colliderect(player.rect):
                print('works')
                pygame.draw.rect(var.screen, (250,250,250), (50,250,self.width,self.height))
            if player.x-50<self.x<player.x+player.width+50 and player.y-50<self.y<player.height+player.y+50:
                print('damage')
                player.health-=5
                self.wait=True




