import pygame
import var
import sys
from entity import player
pygame.init()

class SceneBase:
    def __init__(self):
        self.next = self
    
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
    def quit_execute():
        print("uh-oh, you didn't override this in the child class")
    def start_execute():
        print("uh-oh, you didn't override this in the child class")

class Title(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type== pygame.KEYDOWN and event.key==var.enter:
                self.SwitchToScene(GameScene())
    def Update(self):
        pass
    def Render(self, screen):
        var.screen.fill((100,150,90))
        self.mouse = pygame.mouse.get_pos()
        for event in var.events.get():
            if event.type==pygame.QUIT:
                sys.exit()
                pygame.QUIT()
            if event.type==var.click:
                self.quit_execute()
        self.write_title()
        self.start()
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
        if var.width/2 <= self.mouse[0] <= var.width/2+140 and var.height/3 <= self.mouse[1] <= var.height/3+40:
            self.SwitchToScene(GameScene()) 
    def start(self):
        pygame.font.init()
        font= pygame.font.SysFont('Arial', 35)
        start_text = font.render('Start' , True , var.white)

        if var.width/2 <= self.mouse[0] <= var.width/2+140 and var.height/3 <= self.mouse[1] <= var.height/3+40:
            pygame.draw.rect(var.screen,var.button_light,[var.width/2,var.height/3,140,40])
        else:
            pygame.draw.rect(var.screen,var.button_dark,[var.width/2,var.height/3,140,40])
        var.screen.blit(start_text, (var.width/2+50,var.height/3))
    #quit bottun
    def quit_execute(self):
        if var.width/2 <= self.mouse[0] <= var.width/2+140 and var.height/2 <= self.mouse[1] <= var.height/2+40:
            sys.exit()
            pygame.QUIT()  
    def quit_draw(self):
        pygame.font.init()
        font= pygame.font.SysFont('Arial', 35)
        quit_text = font.render('Quit' , True , var.white)

        if var.width/2 <= self.mouse[0] <= var.width/2+140 and var.height/2 <= self.mouse[1] <= var.height/2+40:
            pygame.draw.rect(var.screen,var.button_light,[var.width/2,var.height/2,140,40])
        else:
            pygame.draw.rect(var.screen,var.button_dark,[var.width/2,var.height/2,140,40])
        var.screen.blit(quit_text, (var.width/2+50,var.height/2))

class GameScene(SceneBase):
    def __init__(self):
        self.pc=player.Player(var.screenwidth/2,var.screenheight/2, var.screenwidth/50,var.screenwidth/50)
        SceneBase.__init__(self)
    def ProcessInput(self, events, pressed_keys):
        vel = var.screenwidth/500
        self.pc.movement(pygame.key.get_pressed(), vel)
    def Update(self):
        
        self.pc.draw_player(var.screen)    
    def Render(self, screen):
        var.clock.tick(60)
        #window
        var.screen.fill((100,150,90))
        self.pc.draw_player(var.screen)
        pygame.display.update()
    
    def quit_execute(self):
        pass
    def start_execute(self):
        pass
    