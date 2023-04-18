import pygame
import sys
import math
#Contains player class
from entity import player
#contains global variables
import var
#contains scenes
import scenes
title = scenes.Title()
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

def main():    
    run_game(60, title)
main()
