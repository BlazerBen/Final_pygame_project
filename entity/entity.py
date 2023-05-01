import pygame
import sys
import var
pygame.init()

class Entity(pygame.sprite.Sprite):
    """
    A class to represent an entity

    ...

    Attributes
    ----------
    self.health=25
        default health int
    self.max_health=50
        default max health
    self.width=var.screenwidth/50
        default width of entity
    self.height=var.screenwidth/50
        default height of entity
    self.x=0
        default x position
    self.y=0
        default y postion
    self.ratio=self.max_health/self.width
        used for health bar length
    Methods
    -------
    draw(window):
        function to be overwritten
    movement(key, vel):
        function to be overwritten
    get_damage(amount):
        decreases health
    get_health(amount):
        increases health
    """
    def __init__(self):
        '''
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
        none
        '''
        self.health=25
        self.max_health=50
        self.width=var.screenwidth/50
        self.height=var.screenwidth/50
        self.x=0
        self.y=0
        self.ratio=self.max_health/self.width
        super().__init__()
    def draw(self, window):
        '''
        Draws player rectangle

        Parameters
        ----------
        window : pygame.display.set_mode(screenhieght,screenwidth)
            screen display
        '''
        self.health_bar()
        pygame.draw.rect(window, self.color , (self.x,self.y,self.width,self.height))
    def movement(self):
        '''
        function to be overwritten

        Parameters
        ----------
        none
        '''
        print("uh-oh, you didn't override this in the child class")
    def get_damage(self,amount):
        '''
        decreases health

        Parameters
        ----------
        amount : int
            amount to decrease health by
        '''
        if self.health>0:
            self.health-=amount
        if self.health<=0:
            self.health=0
    def get_health(self,amount):
        '''
        increase health

        Parameters
        ----------
        amount : int
            amount to increase health by
        '''
        if self.health<self.max_health:
            self.health+=amount
        if self.health>=self.max_health:
            self.health=self.max_health
    def health_bar(self):
        '''
        draws health bar

        Parameters
        ----------
        none
        '''
        pygame.draw.rect(var.screen, (255,0,0), (self.x, self.y-self.height/5,self.health/self.ratio,self.height/5))
