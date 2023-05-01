import pygame
import var
import sys
from entity import player
from entity import enemy
import random
pygame.init()



class SceneBase:
    """
    A class that served as a base for all scene classes

    ...

    Attributes
    ----------
    self.next
    Methods
    process_input():
        proccesses incoming inputs
    update():
        updates objects
    render():
        draws screen display
    quit_execute():
        executes a quit function
    start_execute():
        executes a start/resume function
    switch_to_scene(next_scene):
        switches to next scene
    terminate():
        terminates program
    -------
    """
    def __init__(self):
        self.next = self
        self.scene_name="uh-oh, you didn't override this in the child class"
    def process_input(self, events, pressed_keys):
        '''
        proccesses incoming inputs

        Parameters
        ----------
        events
            pygame events
        pressed_keys
            pygame pressed keys
        '''
        print("uh-oh, you didn't override this in the child class")
    def update(self):
        '''
        updates objects

        Parameters
        ----------
        none
        '''
        print("uh-oh, you didn't override this in the child class")
    def render(self, screen):
        '''
        draws screen display

        Parameters
        ----------
        screen
            SCREENDISPLAY
        '''
        print("uh-oh, you didn't override this in the child class")
    def switch_to_scene(self, next_scene):
        '''
        switched active scene

        Parameters
        ----------
        next_scene : scene object
            new scene
        '''
        self.next = next_scene
    def terminate(self):
        '''
        terminates program

        Parameters
        ----------
        none
        '''
        self.switch_to_scene(None)
    def quit_execute(self):
        '''
        executes a quit function

        Parameters
        ----------
        none
        '''
        print("uh-oh, you didn't override this in the child class")
    def start_execute(self):
        '''
        executes a start/resume function

        Parameters
        ----------
        none
        '''
        print("uh-oh, you didn't override this in the child class")

class Title(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.scene_name='Title'
        self.mouse = pygame.mouse.get_pos()
    def process_input(self, events, pressed_keys):
        for event in events:
            if event.type== pygame.KEYDOWN and event.key==var.enter:
                self.switch_to_scene(Difficulty())
    def update(self):
        pass
    def render(self, screen):
        var.screen.fill(var.background)
        self.mouse = pygame.mouse.get_pos()
        for event in var.events.get():
            if event.type==pygame.QUIT:
                sys.exit()
                pygame.QUIT()
            if event.type==var.click:
                self.quit_execute()
                self.start_execute()
        self.write_title()
        self.start('Start')
        self.quit_draw()
        pygame.display.update()
    def write_title(self):
        '''
        Writes title

        Parameters
        ----------
        none
        '''
        pygame.font.init()
        title_font= pygame.font.SysFont('Arial', 60)
        title_text = title_font.render('Mystic Meadow' , True , var.white)
        var.screen.blit(title_text, (var.width/2-50,var.height/4))
    def start_execute(self):
        if var.width/2 <= self.mouse[0] <= var.width/2+160 and var.height/2.5 <= self.mouse[1] <= var.height/2.5+40:
            self.switch_to_scene(Difficulty()) 
    def start(self, button):
        '''
        draws the start button

        Parameters
        ----------
        button : str
            button text
        '''
        pygame.font.init()
        font= pygame.font.SysFont('Arial', 35)
        start_text = font.render(button , True , var.white)
        if var.width/2 <= self.mouse[0] <= var.width/2+var.width/10 and var.height/2.5 <= self.mouse[1] <= var.height/2.5+var.height/25:
            pygame.draw.rect(var.screen,var.button_light,[var.width/2,var.height/2.5,var.width/10,var.height/25])
        else:
            pygame.draw.rect(var.screen,var.button_dark,[var.width/2,var.height/2.5,var.width/10,var.height/25])
        var.screen.blit(start_text, (var.width/2+50,var.height/2.5))
    def quit_execute(self):
        if var.width/2 <= self.mouse[0] <= var.width/2+var.width/10 and var.height/2 <= self.mouse[1] <= var.height/2+var.height/25:
            sys.exit()
            pygame.QUIT()
    def quit_draw(self):
        '''
        draws the quit button

        Parameters
        ----------
        none
        '''
        pygame.font.init()
        font= pygame.font.SysFont('Arial', 35)
        quit_text = font.render('Quit' , True , var.white)

        if var.width/2 <= self.mouse[0] <= var.width/2+var.width/10 and var.height/2 <= self.mouse[1] <= var.height/2+var.height/25:
            pygame.draw.rect(var.screen,var.button_light,[var.width/2,var.height/2,var.width/10,var.height/25])
        else:
            pygame.draw.rect(var.screen,var.button_dark,[var.width/2,var.height/2,var.width/10,var.height/25])
        var.screen.blit(quit_text, (var.width/2+50,var.height/2))

class GameScene(SceneBase):
    """
    A class for the game scene

    ...

    Attributes
    ----------
    pc : class obj
        player class
    bad : list
        list of enemy classes
    number : int
        number of enemies
    self.bullets : list
        list of bullets on screen

    Methods
    nothing not in SceneBase
    -------
    """
    def __init__(self, x=var.screenwidth/2, y=var.screenheight/2, e_cord=0, number=10, health=100, mana=20, kills=0):
        self.pc=player.Player(x,y, (0,0,0), health, mana, kills)
        self.bad=[]
        self.number=number
        if e_cord==0:
            for i in range(number):
                bad_color=random.choices(range(256), k=3)
                self.bad.append(enemy.Enemy(x/(i+1), 0, bad_color))
        else:
            for i in e_cord:
                self.bad.append(enemy.Enemy(i.x,i.y, i.color))         
        self.bullets=[]
        SceneBase.__init__(self)
        self.scene_name='GameScene'
    def process_input(self, events, pressed_keys):
        vel = var.screenwidth/500
        for event in events:
            if event.type== var.click:
                mouse_x,mouse_y= pygame.mouse.get_pos()
                if self.pc.mana >0:
                    self.pc.mana-=1
                    self.bullets.append(player.PlayerBullet(self.pc.x,self.pc.y, mouse_x,mouse_y))
            if pygame.key.get_pressed()[var.escape]:
                self.bullets=[]
                self.switch_to_scene(Pause(self))
        if self.pc.health>0:
            self.pc.movement(pygame.key.get_pressed(), vel)
        else:
            self.switch_to_scene(Pause(self, False))
        for i in self.bad:
            i.movement(self.pc, vel*.5)
    def update(self):
        for i in self.bad:
            if i.health==0:
                self.bad.remove(i)
                self.pc.point.append(i)
                self.pc.get_health(5)
                bad_color=random.choices(range(256), k=3)
                self.bad.append(enemy.Enemy(0, 0, bad_color))
        if self.pc.mana<self.pc.max_mana:
            self.pc.mana+=.025
        if self.pc.mana>=self.pc.max_mana:
            self.pc.mana=self.pc.max_mana          
    def render(self, screen):
        var.clock.tick(60)
        #window
        var.screen.fill(var.background)
        self.pc.draw(var.screen)
        self.pc.score()
        self.pc.mana_bar()
        for i in self.bad:
            i.draw(var.screen)
        for bullet in self.bullets:
            bullet.main(var.screen)
            if bullet.check_pos():
                self.bullets.remove(bullet)
            for i in self.bad:
                if i.update(bullet):
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
        pygame.display.update()
    def quit_execute(self):
        pass
    def start_execute(self):
        pass

class Difficulty(SceneBase):
    """
    A class for the scene where you chose you difficulty

    ...

    Attributes
    ----------
    font : pygame font
        font for buttons
    mouse : pygame mouse position
        gets mouse position
    Methods
    easy_button():
        draws easy button
    normal_button():
        draws normal button
    hard_button():
        draws hard button
    -------
    """
    def __init__(self):
        pygame.font.init()
        self.font= pygame.font.SysFont('Arial', 35)
        SceneBase.__init__(self)
        self.mouse = pygame.mouse.get_pos()
    def process_input(self, events, pressed_keys):
        #self.switch_to_scene(GameScene(var.screenwidth/2, var.screenheight/2, 0, 10))
        pass
    def update(self):
        pass

    def render(self, screen):
        var.screen.fill((0,0,0))
        self.mouse = pygame.mouse.get_pos()
        self.easy_button()
        self.normal_button()
        self.hard_button()
    def quit_execute(self):
        pass
    def start_execute(self):
        if var.width/2-(var.width/2/10) <= self.mouse[0] <= var.width/2+var.width/2/5-var.width/2/10 and var.height/5 <= self.mouse[1] <= var.height/5+var.height/35:
            #easy
            self.switch_to_scene(GameScene(var.screenwidth/2, var.screenheight/2, 0, 5))
        if var.width/2-(var.width/2/10) <= self.mouse[0] <= var.width/2+var.width/2/5-var.width/2/10 and var.height/2.5 <= self.mouse[1] <= var.height/2.5+var.height/25:
            #Normal
            self.switch_to_scene(GameScene(var.screenwidth/2, var.screenheight/2, 0, 10))
        if var.width/2-(var.width/2/10) <= self.mouse[0] <= var.width/2+var.width/2/5-var.width/2/10 and var.height/2 <= self.mouse[1] <= var.height/2+var.height/25:
            #Hard
            self.switch_to_scene(GameScene(var.screenwidth/2, var.screenheight/2, 0, 25))
    def easy_button(self):
        '''
        draws the easy button

        Parameters
        ----------
        none
        '''
        easy_text = self.font.render('Easy', True , var.white)
        if var.width/2-(var.width/2/10) <= self.mouse[0] <= var.width/2+var.width/2/5-var.width/2/10 and var.height/5 <= self.mouse[1] <= var.height/5+var.height/25:
            pygame.draw.rect(var.screen,var.button_light,[var.width/2-(var.width/2/10),var.height/5,var.width/2/5-var.width/2/10,var.height/25])
        else:
            pygame.draw.rect(var.screen,var.button_dark,[var.width/2-(var.width/2/10),var.height/5,var.width/2/5-var.width/2/10,var.height/25])
        var.screen.blit(easy_text, (var.width/2-(var.width/2/10),var.height/5))
    def normal_button(self):
        '''
        draws the normal button

        Parameters
        ----------
        none
        '''
        normal_text = self.font.render('Normal', True , var.white)
        if var.width/2-(var.width/2/10) <= self.mouse[0] <= var.width/2+var.width/2/5-var.width/2/10 and var.height/2.5 <= self.mouse[1] <= var.height/2.5+var.height/25:
            pygame.draw.rect(var.screen,var.button_light,[var.width/2-(var.width/2/10),var.height/2.5,var.width/2/5-var.width/2/10,var.height/25])
        else:
            pygame.draw.rect(var.screen,var.button_dark,[var.width/2-(var.width/2/10),var.height/2.5,var.width/2/5-var.width/2/10,var.height/25])
        var.screen.blit(normal_text, (var.width/2-(var.width/2/10),var.height/2.5))
    def hard_button(self):
        '''
        draws the hard button

        Parameters
        ----------
        none
        '''
        hard_text = self.font.render('Hard', True , var.white)
        if var.width/2-(var.width/2/10) <= self.mouse[0] <= var.width/2+var.width/2/5-var.width/2/10 and var.height/2 <= self.mouse[1] <= var.height/2+var.height/25:
            pygame.draw.rect(var.screen,var.button_light,[var.width/2-(var.width/2/10),var.height/2,var.width/2/5-var.width/2/10,var.height/25])
        else:
            pygame.draw.rect(var.screen,var.button_dark,[var.width/2-(var.width/2/10),var.height/2,var.width/2/5-var.width/2/10,var.height/25])
        var.screen.blit(hard_text, (var.width/2-(var.width/2/10),var.height/2))

class Pause(Title):
    """
    A class for the game scene

    ...

    Attributes
    ----------
    previous : scene obj
        previous scene
    game : bool
        check if player has died or not
    mouse : pygame.mouse.get_pos()
        gets mouse position

    Methods
    switch_to_scene(next=False):
        changed to switch to previous scene with same postion of everything
    game_over():
        prints game over text
    -------
    """
    def __init__(self, previous, game=True):
        super().__init__()
        self.previous=previous
        self.previous.render(var.screen)
        self.game=game
        self.mouse=pygame.mouse.get_pos()
    def process_input(self, events, pressed_keys):
        if pygame.key.get_pressed()[var.tab]:
            self.switch_to_scene()
        for event in var.events.get():
            if event.type==var.click:
                self.quit_execute()
                self.start_execute()
    def update(self):
        pass
    def render(self, screen):
        self.mouse=pygame.mouse.get_pos()
        if self.game:
            self.start('Resume')
            self.quit_draw()
        else:
            self.start('Back')
            self.gameover()

    def start_execute(self):
        if self.game:
            if var.width/2 <= self.mouse[0] <= var.width/2+160 and var.height/2.5 <= self.mouse[1] <= var.height/2.5+40:
                self.switch_to_scene()
        else:
            if var.width/2 <= self.mouse[0] <= var.width/2+160 and var.height/2.5 <= self.mouse[1] <= var.height/2.5+40:
                self.switch_to_scene(Title())
    def switch_to_scene(self, next_scene=False):
        if next_scene:
            self.next=next_scene
        else:
            e_cord=[]
            for i in self.previous.bad:
                e_cord.append(i)
            self.next=GameScene(self.previous.pc.x, self.previous.pc.y, e_cord, self.previous.number, self.previous.pc.health, self.previous.pc.mana, len(self.previous.pc.point))
    def gameover(self):
        '''
        Writes gameover text

        Parameters
        ----------
        none
        '''
        pygame.font.init()
        font= pygame.font.SysFont('Arial', 72)
        game_over_text = font.render('Game Over' , True , var.white)
        var.screen.blit(game_over_text, (var.screenwidth/3, var.screenheight/3))
