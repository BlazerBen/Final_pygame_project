import pygame
import var
import sys
from entity import player
from entity import enemy
import random
pygame.init()



class SceneBase:
    def __init__(self):
        self.next = self
        self.scene_name="uh-oh, you didn't override this in the child class"
    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene
    
    def Terminate(self):
        self.SwitchToScene(None)
    def quit_execute(self):
        print("uh-oh, you didn't override this in the child class")
    def start_execute(self):
        print("uh-oh, you didn't override this in the child class")

class Title(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.scene_name='Title'
        
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type== pygame.KEYDOWN and event.key==var.enter:
                self.SwitchToScene(Difficulty())
    def Update(self):
        pass
    def Render(self, screen):
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
    
    #title
    def write_title(self):
        pygame.font.init()
        title_font= pygame.font.SysFont('Arial', 60)
        title_text = title_font.render('Game_name' , True , var.white)
        var.screen.blit(title_text, (var.width/2-50,var.height/4))
    #start button
    def start_execute(self):
        if var.width/2 <= self.mouse[0] <= var.width/2+160 and var.height/2.5 <= self.mouse[1] <= var.height/2.5+40:
            self.SwitchToScene(Difficulty()) 
    def start(self, button):
        pygame.font.init()
        font= pygame.font.SysFont('Arial', 35)
        start_text = font.render(button , True , var.white)
        if var.width/2 <= self.mouse[0] <= var.width/2+var.width/10 and var.height/2.5 <= self.mouse[1] <= var.height/2.5+var.height/25:
            pygame.draw.rect(var.screen,var.button_light,[var.width/2,var.height/2.5,var.width/10,var.height/25])
        else:
            pygame.draw.rect(var.screen,var.button_dark,[var.width/2,var.height/2.5,var.width/10,var.height/25])
        var.screen.blit(start_text, (var.width/2+50,var.height/2.5))
    #quit button
    def quit_execute(self):
        if var.width/2 <= self.mouse[0] <= var.width/2+var.width/10 and var.height/2 <= self.mouse[1] <= var.height/2+var.height/25:
            sys.exit()
            pygame.QUIT()
    def quit_draw(self):
        pygame.font.init()
        font= pygame.font.SysFont('Arial', 35)
        quit_text = font.render('Quit' , True , var.white)

        if var.width/2 <= self.mouse[0] <= var.width/2+var.width/10 and var.height/2 <= self.mouse[1] <= var.height/2+var.height/25:
            pygame.draw.rect(var.screen,var.button_light,[var.width/2,var.height/2,var.width/10,var.height/25])
        else:
            pygame.draw.rect(var.screen,var.button_dark,[var.width/2,var.height/2,var.width/10,var.height/25])
        var.screen.blit(quit_text, (var.width/2+50,var.height/2))

class GameScene(SceneBase):
    def __init__(self, x=var.screenwidth/2, y=var.screenheight/2, e_cord=0, number=10):
        self.pc=player.Player(x,y, (0,0,0))
        self.bad=[]
        self.number=number
        for i in range(number):
            if e_cord==0:
                self.bad.append(enemy.Enemy(x/(i+1), 0))
            else:
                for i in e_cord:
                    self.bad.append(enemy.Enemy(i.x,i.y))
            
        self.bullets=[]
        SceneBase.__init__(self)
        self.scene_name='GameScene'
    def ProcessInput(self, events, pressed_keys):
        vel = var.screenwidth/500
        for event in events:
            if event.type== var.click:
                mouse_x,mouse_y= pygame.mouse.get_pos()
                if self.pc.mana >0:
                    self.pc.mana-=1
                    self.bullets.append(player.PlayerBullet(self.pc.x,self.pc.y, mouse_x,mouse_y))
            if pygame.key.get_pressed()[var.escape]:
                self.bullets=[]
                self.SwitchToScene(Pause(self))
        if self.pc.health>0:
            self.pc.movement(pygame.key.get_pressed(), vel)
        else:
            self.SwitchToScene(Pause(self, False))
        for i in self.bad:
            i.movement(self.pc, vel*.5)

    def Update(self):
        for i in self.bad:
            if i.health==0:
                self.bad.remove(i)
                self.pc.point.append(i)
                self.bad.append(enemy.Enemy(0, 0))
        if self.pc.mana<self.pc.max_mana:
            self.pc.mana+=.025
        if self.pc.mana>=self.pc.max_mana:
            self.pc.mana=self.pc.max_mana
        
                
    def Render(self, screen):
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
                if bullet in self.bullets:
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
    def __init__(self):
        self.scene_name="Difficulty"
        pygame.font.init()
        self.font= pygame.font.SysFont('Arial', 35)
        SceneBase.__init__(self)
        self.vertical_left_button=var.width/2

    def ProcessInput(self, events, pressed_keys):
        #self.SwitchToScene(GameScene(var.screenwidth/2, var.screenheight/2, 0, 10))
        pass

    def Update(self):
        pass

    def Render(self, screen):
        var.screen.fill((0,0,0))
        self.mouse = pygame.mouse.get_pos()
        self.easy_button()
        self.normal_button()
        self.hard_button()
    def quit_execute(self):
        pass
    def start_execute(self):
        if self.vertical_left_button-(self.vertical_left_button/10) <= self.mouse[0] <= self.vertical_left_button+self.vertical_left_button/5-self.vertical_left_button/10 and var.height/5 <= self.mouse[1] <= var.height/5+var.height/35:
            #easy
            self.SwitchToScene(GameScene(var.screenwidth/2, var.screenheight/2, 0, 5))
        if self.vertical_left_button-(self.vertical_left_button/10) <= self.mouse[0] <= self.vertical_left_button+self.vertical_left_button/5-self.vertical_left_button/10 and var.height/2.5 <= self.mouse[1] <= var.height/2.5+var.height/25:
            #Normal
            self.SwitchToScene(GameScene(var.screenwidth/2, var.screenheight/2, 0, 10))
        if self.vertical_left_button-(self.vertical_left_button/10) <= self.mouse[0] <= self.vertical_left_button+self.vertical_left_button/5-self.vertical_left_button/10 and var.height/2 <= self.mouse[1] <= var.height/2+var.height/25:
            #Hard
            self.SwitchToScene(GameScene(var.screenwidth/2, var.screenheight/2, 0, 25))
    def easy_button(self):
        easy_text = self.font.render('Easy', True , var.white)
        if self.vertical_left_button-(self.vertical_left_button/10) <= self.mouse[0] <= self.vertical_left_button+self.vertical_left_button/5-self.vertical_left_button/10 and var.height/5 <= self.mouse[1] <= var.height/5+var.height/25:
            pygame.draw.rect(var.screen,var.button_light,[self.vertical_left_button-(self.vertical_left_button/10),var.height/5,self.vertical_left_button/5-self.vertical_left_button/10,var.height/25])
        else:
            pygame.draw.rect(var.screen,var.button_dark,[self.vertical_left_button-(self.vertical_left_button/10),var.height/5,self.vertical_left_button/5-self.vertical_left_button/10,var.height/25])
        var.screen.blit(easy_text, (self.vertical_left_button-(self.vertical_left_button/10),var.height/5))
    def normal_button(self):
        normal_text = self.font.render('Normal', True , var.white)
        if self.vertical_left_button-(self.vertical_left_button/10) <= self.mouse[0] <= self.vertical_left_button+self.vertical_left_button/5-self.vertical_left_button/10 and var.height/2.5 <= self.mouse[1] <= var.height/2.5+var.height/25:
            pygame.draw.rect(var.screen,var.button_light,[self.vertical_left_button-(self.vertical_left_button/10),var.height/2.5,self.vertical_left_button/5-self.vertical_left_button/10,var.height/25])
        else:
            pygame.draw.rect(var.screen,var.button_dark,[self.vertical_left_button-(self.vertical_left_button/10),var.height/2.5,self.vertical_left_button/5-self.vertical_left_button/10,var.height/25])
        var.screen.blit(normal_text, (self.vertical_left_button-(self.vertical_left_button/10),var.height/2.5))
    def hard_button(self):
        hard_text = self.font.render('Hard', True , var.white)
        if self.vertical_left_button-(self.vertical_left_button/10) <= self.mouse[0] <= self.vertical_left_button+self.vertical_left_button/5-self.vertical_left_button/10 and var.height/2 <= self.mouse[1] <= var.height/2+var.height/25:
            pygame.draw.rect(var.screen,var.button_light,[self.vertical_left_button-(self.vertical_left_button/10),var.height/2,self.vertical_left_button/5-self.vertical_left_button/10,var.height/25])
        else:
            pygame.draw.rect(var.screen,var.button_dark,[self.vertical_left_button-(self.vertical_left_button/10),var.height/2,self.vertical_left_button/5-self.vertical_left_button/10,var.height/25])
        var.screen.blit(hard_text, (self.vertical_left_button-(self.vertical_left_button/10),var.height/2))

class Pause(Title):
    def __init__(self, previous, game=True):
        super().__init__()
        self.previous=previous
        self.previous.Render(var.screen)
        self.scene_name='Pause'
        self.game=game
        self.mouse=pygame.mouse.get_pos()
        
    def ProcessInput(self, events, pressed_keys):
        if pygame.key.get_pressed()[var.tab]:
            self.SwitchToScene()
        for event in var.events.get():
            if event.type==var.click:
                self.quit_execute()
                self.start_execute()
                

    def Update(self):
        pass
    def Render(self, screen):
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
                self.SwitchToScene()
        else:
            if var.width/2 <= self.mouse[0] <= var.width/2+160 and var.height/2.5 <= self.mouse[1] <= var.height/2.5+40:
                self.SwitchToScene(Title())
    def SwitchToScene(self, next=False):
        if next:
            self.next=next
        else:
            e_cord=[]
            for i in self.previous.bad:
                e_cord.append(i)
            self.next=GameScene(self.previous.pc.x, self.previous.pc.y, e_cord, self.previous.number)
    def gameover(self):
        pygame.font.init()
        font= pygame.font.SysFont('Arial', 72)
        game_over_text = font.render('Game Over' , True , var.white)
        var.screen.blit(game_over_text, (var.width,var.height/1.5))
        self.previous.pc.score(100, 50, 72)

        