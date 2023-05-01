import math
#useful math functions
import pygame
import var
from entity import entity
pygame.init()


class Player(entity.Entity):
    """
    A class to represent the player

    ...

    Attributes
    ----------
    x : int
        first x position of the player
    y : int
        first y position of the player
    color : tuple
        rgb of color of the player
    health : int
        health integer of player
    mana : int
        mana integer of player
    kill : int
        number of enemies killed by player
    Methods
    -------
    draw(window):
        draws the player onto the screen at its position
    movement(key, vel):
        uses keyboard input to move the players position
    score(x=var.width-var.width/10, y=0, font_size=40):
        draws kill count in top right corner
    """
    def __init__(self, x,y, color, health=100, mana=20, kills=0):
        '''
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
        x : int
            first x position of the player
        y : int
            first y position of the player
        color : tuple
            rgb of color of the player
        health : int
            health integer of player
        mana : int
            mana integer of player
        kill : int
            number of enemies killed by player
        '''
        super().__init__()
        self.x=x
        self.y=y
        self.health=health
        self.max_health=100
        self.max_mana=20
        self.mana=mana
        self.ratio=self.max_health/self.width
        self.color=color
        self.point=[]
        for i in range(kills):
            self.point.append('') 
    def movement(self, keys, vel):
        '''
        moves player positon based on keyboard input

        Parameters
        ----------
        keys : pygame.key.get_pressed()
            checks if keys are pressed
        vel : int
            player speed
        '''
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
    def score(self):
        '''
        draws player score

        Parameters
        ----------
        none
        '''
        point_font=pygame.font.SysFont('Arial', 40)
        kill=len(self.point)
        point_text=point_font.render(f'Kills: {kill}' , True , var.white)
        var.screen.blit(point_text, (var.width*.9,0))
    def mana_bar(self):
        '''
        draws player mana bar

        Parameters
        ----------
        none
        '''
        pygame.draw.rect(var.screen, (120,81,169), (self.x, self.y+self.height,self.mana,self.height/5))

class PlayerBullet:
    """
    A class to represent a player bullet.

    ...

    Attributes
    ----------
    x : int
        first x position of the bullet
    y : int
        first y position of the bullet
    
    Methods
    -------
    main(win):
        draws the bullet onto the screen at its position
    check_pos()
        check if bullet is on screen or not
    """
    def __init__(self,x_pos,y_pos, mouse_x,mouse_y):
        self.x=x_pos
        self.y=y_pos
        self.mouse_x=mouse_x
        self.mouse_y=mouse_y
        self.speed=15
        self.angle=math.atan2(y_pos-mouse_y,x_pos-mouse_x)
        self.x_vel=math.cos(self.angle)*self.speed
        self.y_vel=math.sin(self.angle)*self.speed
    def main(self, win):
        '''
        draws player bullets and moves the position

        Parameters
        ----------
        win : pygame.display.set_mode(screenhieght,screenwidth)
            screen display
        '''
        self.x-=int(self.x_vel)
        self.y-=int(self.y_vel)
        pygame.draw.circle(win, (120,81,169),(self.x, self.y), var.screenwidth/150)
    def check_pos(self):
        '''
        check if bullets are on screen or not

        Parameters
        ----------
        none
        '''
        if self.x>var.screenwidth or self.x<0 or self.y>var.screenheight or self.y<0:
            return True
        else:
            return False
