from math import hypot
from pygame.sprite import Sprite
import pygame

class Vampire(Sprite):
    def __init__(self):
        super(Vampire, self).__init__()
        self.x = 100
        self.y = 224
        self.speed = 2
        self.rect = pygame.Rect(0,0,64,64)
        self.rect.centerx = self.x
        self.rect.top = self.y
    def update_me(self,player):
        dx = self.x - player.x
        dy = self.y - player.y
        dist = hypot(dx,dy)
        dx = dx/dist
        dy = dy/dist
        self.x += dx * self.speed
        self.y += dy * self.speed
        self.rect.x = self.x