import pygame
import sys
import var
from pygame.locals import *
pygame.init()
from entity import entity
import math

class Player(entity.Entity):
    def __init__(self, x,y, color, health=100, mana=20):
        super().__init__()
        self.x=x
        self.y=y
        self.health=health
        self.max_health=100
        self.max_mana=20
        self.mana=mana
        self.ratio=self.max_health/self.width
        self.color=color
        self.hitbox=(self.x,self.y,self.width,self.height)
        self.point=[]
    def draw(self, window):
        self.hitbox=(self.x,self.y,self.width,self.height)
        self.health_bar()
        pygame.draw.rect(window, self.color,self.hitbox)
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
    def score(self, x=var.width-var.width/10, y=0, font_size=40):
        point_font=pygame.font.SysFont('Arial', font_size)
        point_text=point_font.render(f'Kills: {len(self.point)}' , True , var.white)
        var.screen.blit(point_text, (x,y))
    def mana_bar(self):
        pygame.draw.rect(var.screen, (120,81,169), (self.x, self.y+self.height,self.mana,self.height/5))

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
        pygame.draw.circle(win, (120,81,169),(self.x, self.y), var.screenwidth/150)
        
    def check_pos(self):    
        if self.x>var.screenwidth or self.x<0 or self.y>var.screenheight or self.y<0:
            return True
        else:
            return False
