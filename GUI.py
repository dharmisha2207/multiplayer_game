import pygame
import os

class Bunny:

    bunny_height=70
    bunny_width=75

    def __init__(self, bunny_x, bunny_y):
        self.bunny = pygame.image.load(os.path.join('Assets','bunny.png'))
        self.bunny = pygame.transform.scale(self.bunny,(self.bunny_width,self.bunny_height))
        self.bunny_x = bunny_x
        self.bunny_y = bunny_y
        self.x=bunny_x
        self.y=bunny_y
    
    def get_bunny(self):
        return self.bunny

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def left_increment(self, x, y):
        if self.x + 1 > x and self.y + 1 < y:
            return
        if self.x + 1 > x:
            self.y -= 1
        else: 
            self.x += 1
    
    def right_increment(self, x, y):
        if self.x - 1 < x and self.y + 1 < y:
            return
        if self.x - 1 < x:
            self.y -= 1
        else:
            self.x -= 1

    def left_decrement(self, x, y):
        if self.x - 1 < self.bunny_x and self.y + 1 < self.bunny_y:
            return
        if self.y + 1 < self.bunny_y:
            self.y += 1
        elif self.x - 1 > self.bunny_x: 
            self.x -= 1
    
    def right_decrement(self, x, y):
        if self.x + 1 > self.bunny_x and self.y + 1 > self.bunny_y:
            return
        if self.y + 1 < self.bunny_y:
            self.y += 1
        elif self.x + 1 < self.bunny_x: 
            self.x += 1


class Game:

    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.bunny1 = Bunny(100,600)
        self.bunny2 = Bunny(800,600)
        self.carrot_x = 400
        self.carrot_y = 200
        self.bg = pygame.image.load(os.path.join('Assets','bg.jpeg'))
        self.bg = pygame.transform.scale(self.bg,(width,height))
        self.carrot = pygame.image.load(os.path.join('Assets','carrot.png'))
        self.carrot = pygame.transform.scale(self.carrot,(100,100))
        self.win = pygame.display.set_mode((width,height))

    def draw_window(self):
        pygame.display.set_caption("Reach the Goal")
        self.win.blit(self.bg, (0,0))
        self.win.blit(self.bunny1.get_bunny(),(self.bunny1.get_x(), self.bunny1.get_y()))
        self.win.blit(self.bunny2.get_bunny(),(self.bunny2.get_x(), self.bunny2.get_y()))
        self.win.blit(self.carrot,(self.carrot_x,self.carrot_y))
        pygame.display.update()

    def player1_inc(self):
        self.bunny1.left_increment(self.carrot_x, self.carrot_y)
    
    def player2_inc(self):
        self.bunny2.right_increment(self.carrot_x, self.carrot_y)
    
    def player1_dec(self):
        self.bunny1.left_decrement(self.carrot_x, self.carrot_y)
    
    def player2_dec(self):
        self.bunny2.right_decrement(self.carrot_x, self.carrot_y)


    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.player1_inc()
            self.player2_inc()
            self.draw_window()
        pygame.quit()

