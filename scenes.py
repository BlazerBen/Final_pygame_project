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
                self.SwitchToScene(GameScene())
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
            self.SwitchToScene(GameScene()) 
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
    def __init__(self, x=var.screenwidth/2, y=var.screenheight/2, e_x=0, e_y=0):
        self.pc=player.Player(x,y, (0,0,0))
        self.bad=[]
        for i in range(4):
            if e_x!= 0 or e_y!=0:
                self.bad.append(enemy.Enemy(e_x,e_y))
            else:
                self.bad.append(enemy.Enemy(random.randint(0, var.screenwidth),random.randint(0,var.screenheight)))
        self.bullets=[]
        SceneBase.__init__(self)
        self.scene_name='GameScene'
    def ProcessInput(self, events, pressed_keys):
        vel = var.screenwidth/500
        for event in events:
            if event.type== var.click:
                mouse_x,mouse_y= pygame.mouse.get_pos()
                self.bullets.append(player.PlayerBullet(self.pc.x,self.pc.y, mouse_x,mouse_y))
            if pygame.key.get_pressed()[var.escape]:
                self.bullets=[]
                self.SwitchToScene(Pause(self))
        self.pc.movement(pygame.key.get_pressed(), vel)
        for i in self.bad:
            i.movement(self.pc, vel*.75)
        
    def Update(self):
        self.pc.draw(var.screen)    
    def Render(self, screen):
        var.clock.tick(60)
        #window
        var.screen.fill(var.background)
        self.pc.draw(var.screen)
        for i in self.bad:
                i.draw(var.screen)
        for bullet in self.bullets:
            bullet.main(var.screen)
            for i in self.bad:
                i.update(bullet)

        pygame.display.update()
    
    def quit_execute(self):
        pass
    def start_execute(self):
        pass

class Pause(Title):
    def __init__(self, previous):
        super().__init__()
        self.previous=previous
        self.previous.Render(var.screen)
        self.scene_name='Pause'
        
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
        
        self.start('Resume')
        self.quit_draw()
    def start_execute(self):
        if var.width/2 <= self.mouse[0] <= var.width/2+160 and var.height/2.5 <= self.mouse[1] <= var.height/2.5+40:
            self.SwitchToScene()
    def SwitchToScene(self):
        print('pause to game')
        self.next=GameScene(self.previous.pc.x, self.previous.pc.y, self.previous.bad.x, self.previous.bad.y)

        