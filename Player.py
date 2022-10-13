import pygame
import os
import question
pygame.font.init()

class Bunny:

    def __init__(self, bunny_x, bunny_y):
        self.bunny_height=70
        self.bunny_width=75
        self.bunny = pygame.image.load(os.path.join('Assets','bunny.png'))
        self.bunny = pygame.transform.scale(self.bunny,(self.bunny_width,self.bunny_height))
        self.bunny_x = bunny_x
        self.bunny_y = bunny_y
        self.x=bunny_x
        self.y=bunny_y
        self.step = 50
        self.score = 0
    
    def get_bunny(self):
        return self.bunny

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def left_increment(self, x, y):
        if self.score < 0:
            self.score += 1
        else:
            if self.x + self.step > x-50 and self.y - self.step < y+50:
                return
            if self.x + self.step > x-50:
                self.y -= self.step
                self.score+=1
            else: 
                self.x += self.step
                self.score+=1

    
    def right_increment(self, x, y):
        if self.score < 0:
            self.score += 1
        else:
            if self.x - self.step < x+50 and self.y - self.step < y+50:
                return
            if self.x - self.step < x+50:
                self.y -= self.step
                self.score+=1
            else:
                self.x -= self.step
                self.score+=1

    def left_decrement(self, x, y):
        if self.x - self.step < self.bunny_x and self.y + self.step < self.bunny_y:
            self.score-=1
        if self.y + self.step < self.bunny_y:
            self.y += self.step
            self.score-=1
        elif self.x - self.step > self.bunny_x: 
            self.x -= self.step
            self.score-=1
    
    def right_decrement(self, x, y):
        if self.x + self.step > self.bunny_x and self.y + 1 > self.bunny_y:
            self.score-=1
        if self.y + self.step < self.bunny_y:
            self.y += self.step
            self.score-=1
        elif self.x + self.step < self.bunny_x: 
            self.x += self.step
            self.score-=1
    
    def get_score(self):
        return self.score