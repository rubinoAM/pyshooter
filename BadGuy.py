from Hero import Hero
from math import hypot, fabs

class BadGuy(object):
    def __init__(self):
        self.x = 200
        self.y = 200
        self.speed = 4
    def update_me(self,player):
        dx = self.x - player.x
        dy = self.y - player.y
        dist = hypot(dx,dy)
        dx = dx/dist
        dy = dy/dist
        self.x -= dx * self.speed
        self.y -= dy * self.speed