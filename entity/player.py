import pygame
import sys
import var
pygame.init()



class Player:
    def __init__(self, x,y,width, height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
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
            print('w')
        if keys[pygame.K_s]:
            self.y+=vel
            print('s')
        




