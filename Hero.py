import pygame
from Arrow import Arrow

class Hero(object):
    def __init__(self):
        self.x = 400
        self.y = 300
        self.speed = 10
        self.should_move_down = False
        self.should_move_left = False
        self.should_move_right = False
        self.should_move_up = False
    def go_move(self,direction):
        if direction == "left":
            self.should_move_left = True
            #self.x -= 10
        if direction == 'right':
            self.should_move_right = True
            #self.x += 10
        if direction == 'up':
            self.should_move_up = True
            #self.y += 10
        if direction == 'down':
            self.should_move_down = True
            #self.y -= 10