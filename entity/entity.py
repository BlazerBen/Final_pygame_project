import pygame
import sys
import var
pygame.init()

class Entity:
    def __init__(self):
        self.next=self
        self.health=100
    def draw(self, window):
        print("uh-oh, you didn't override this in the child class")
    def movement(self):
        print("uh-oh, you didn't override this in the child class")
        




