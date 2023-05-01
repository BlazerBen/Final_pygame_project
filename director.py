import pygame
#necessary for all pygame commands
import var
#contains global variables
import scenes
#contains scenes

title = scenes.Title()

def run_game(starting_scene):
    '''runs the pygame while loop
        Parameters:
            starting_scene(class): class object of the scene that starts the game
        Returns:
            none
    '''
    pygame.init()
    screen = var.screen
    clock = pygame.time.Clock()

    active_scene = starting_scene

    while active_scene is not None:
        # Event filtering
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = var.keys[pygame.K_LALT] or var.keys[pygame.K_RALT]
                if event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            if event.type==var.click:
                active_scene.quit_execute()
                active_scene.start_execute()
            if quit_attempt:
                active_scene.terminate()
            else:
                filtered_events.append(event)
        active_scene.process_input(filtered_events, var.keys)
        active_scene.update()
        active_scene.render(screen)
        active_scene = active_scene.next
        pygame.display.flip()
        clock.tick(60)

if __name__=='__main__':
    run_game(title)
