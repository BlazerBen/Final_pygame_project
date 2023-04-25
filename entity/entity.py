import pygame
import sys
import var
pygame.init()

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        self.next=self
    def draw(self, window):
        print("uh-oh, you didn't override this in the child class")
    def movement(self):
        print("uh-oh, you didn't override this in the child class")
        




