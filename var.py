import pygame
pygame.init()


#WINDOW
infoObject = pygame.display.Info()
screenwidth=infoObject.current_w
screenheight=infoObject.current_h
screen = pygame.display.set_mode((screenwidth,screenheight))
width = screen.get_width()
height = screen.get_height()
background=(100,150,90)

#CONTROLS
#keyboard
keys=pygame.key.get_pressed()
LSHIFT=pygame.K_LSHIFT
a=pygame.K_a
s=pygame.K_s
d=pygame.K_d
w=pygame.K_w
tab=pygame.K_TAB
enter=pygame.K_RETURN
escape=pygame.K_ESCAPE
#mouse
click=pygame.MOUSEBUTTONDOWN

 

#miscellaneous
clock=pygame.time.Clock()
events = pygame.event

#Title screen
#colors
button_light = (170,170,170)
button_dark = (100,100,100)
white=(255,255,255)
buttonwidth=140
#enemy
pygame.font.init()
font= pygame.font.SysFont('Arial', int(round(screenheight/75)))
write_damage=font.render('5' , True , (255,0,0))
damage_erase=font.render('5' , True , (100,150,90))

#sprite
sprite=pygame.sprite.Sprite()
group=pygame.sprite.Group()