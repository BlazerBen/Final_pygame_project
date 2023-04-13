import pygame
import sys
import math
#Contains player class
from entity import player
#contains global variables
import var
#contains scenes
import scenes

pygame.init()

player=player.Player(var.screenwidth/2,var.screenheight/2, 32,32)
title = scenes.Title()

def main():    
    scenes.run_game(60, title)
main()


'''while True:
        var.clock.tick(60)
        #window
        var.window.fill((100,150,90))
        for event in var.events.get():
            if event.type==pygame.QUIT:
                sys.exit()
                pygame.QUIT
        player.main(var.window)
        player.movement(15)

        var.update'''