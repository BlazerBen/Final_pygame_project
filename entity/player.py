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
        
    def main(self, window):
        pygame.draw.rect(window, (0,0,0), (self.x,self.y,self.width,self.height))
    def movement(self, vel):
        if var.keys[var.LSHIFT] or var.keys[pygame.K_RSHIFT]:
            vel=30
        if var.keys[var.a] and self.x>vel:
            self.x-=vel
        if var.keys[var.d] and self.x<var.screenwidth-self.width:
            self.x+=vel
        if var.keys[var.w] and self.y>vel:
            self.y-=vel
        if var.keys[var.s] and self.y<var.screenheight-self.height:
            self.y+=vel
        




