import pygame
import sys
import var
pygame.init()

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        self.health=25
        self.max_health=50
        self.width=var.screenwidth/50
        self.height=var.screenwidth/50
        self.x=0
        self.y=0
        self.ratio=self.max_health/self.width
        super().__init__()
    def draw(self, window):
        print("uh-oh, you didn't override this in the child class")
    def movement(self):
        print("uh-oh, you didn't override this in the child class")
    def get_damage(self,amount):
        if self.health>0:
            self.health-=amount
        if self.health<=0:
            self.health=0
    def get_health(self,amount):
        if self.health<self.max_health:
            self.health+=amount
        if self.health>=self.max_health:
            self.health=self.max_health
    def health_bar(self):
        pygame.draw.rect(var.screen, (255,0,0), (self.x, self.y-self.height/5,self.health/self.ratio,self.height/5))




