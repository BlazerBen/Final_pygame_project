import pygame
import var
import sys
pygame.init()

def run_game(fps, starting_scene):
    pygame.init()
    screen = var.screen
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene != None:
        
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = var.keys[pygame.K_LALT] or \
                              var.keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            if event.type==var.click:
                active_scene.quit_execute()
                active_scene.start_execute()
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        active_scene.ProcessInput(filtered_events, var.keys)
        active_scene.Update()
        active_scene.Render(screen)
        
        active_scene = active_scene.next
        
        pygame.display.flip()
        clock.tick(fps)

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
        SceneBase.__init__(self)
    def ProcessInput(self, events, pressed_keys):
        pass     
    def Update(self):
        pass    
    def Render(self, screen):
        # The game scene is just a blank blue screen
        screen.fill((0, 0, 255))
    
    def quit_execute(self):
        pass
    def start_execute(self):
        pass
    