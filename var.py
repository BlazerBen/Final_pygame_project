import pygame

#WINDOW
screenwidth=1800
screenheight=1000
screen = pygame.display.set_mode((screenheight,screenwidth))
width = screen.get_width()
height = screen.get_height()

#CONTROLS
#keyboard
keys=pygame.key.get_pressed()
LSHIFT=pygame.K_LSHIFT
a=pygame.K_a
s=pygame.K_s
d=pygame.K_d
w=pygame.K_w
enter=pygame.K_RETURN
#mouse
click=pygame.MOUSEBUTTONDOWN
mouse = pygame.mouse.get_pos()


#miscellaneous
clock=pygame.time.Clock()
events = pygame.event

#Title screen
#colors
button_light = (170,170,170)
button_dark = (100,100,100)
white=(255,255,255)

