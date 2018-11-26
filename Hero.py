import pygame

class Hero(object):
    def __init__(self):
        self.x = 400
        self.y = 300
        self.speed = 6
        self.should_move_down = False
        self.should_move_left = False
        self.should_move_right = False
        self.should_move_up = False
    def go_move(self,direction,start = True):
        if direction == "left":
            self.should_move_left = start
        if direction == 'right':
            self.should_move_right = start
        if direction == 'up':
            self.should_move_up = start
        if direction == 'down':
            self.should_move_down = start
    def draw_me(self,w,h):
        if(self.should_move_right):
            if(self.x <= w - 24):
                self.x += self.speed
        elif(self.should_move_left):
            if(self.x >= 0):
                self.x -= self.speed
        if(self.should_move_up):
            if(self.y <= h - 24):
                self.y += self.speed
        elif(self.should_move_down):
            if(self.y >= 0):
                self.y -= self.speed
