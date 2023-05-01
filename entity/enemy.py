import pygame
import var
from entity import entity
pygame.init()

class Enemy(entity.Entity):
    """
    A class to represent an enemy

    ...

    Attributes
    ----------
    x
        x position
    y
        y postion
    color : tuple, optional
        rgb of enemy
    Methods
    -------
    movement(key, vel):
        function to be overridden
    
    """
    def __init__(self,x,y, color=(250,250,250)):
        super().__init__()
        self.x=x
        self.y=y
        self.count=0
        self.damage_write=var.write_damage
        self.color=color
    def movement(self, player, vel):
        '''
        moves enemy positon based on player position

        Parameters
        ----------
        player : class object
            for player position
        vel : int
            enemy speed
        '''
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
        '''
        decreases player health based on enemy position

        Parameters
        ----------
        player : class object
            for player position
        '''
        self.count+=1
        if self.count>=100:
            if player.x-2<self.x<player.x+player.width+2 and player.y-2<self.y<player.height+player.y+2:
                player.get_damage(5)
                self.count=0
    def update(self, bullet):
        '''
        decreases enemy health based on bullet position

        Parameters
        ----------
        bullet : class object
            for bullet position
        '''
        if self.x-var.screenwidth/75<bullet.x<self.x+self.width+var.screenwidth/75 and self.y-var.screenwidth/75<bullet.y<self.y+self.height+var.screenwidth/75:
            self.get_damage(2)
            return True
        else:
            return False
