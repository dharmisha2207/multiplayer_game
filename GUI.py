import pygame
import os

class Bunny:

    bunny_height=70
    bunny_width=75

    def __init__(self, bunny_x, bunny_y):
        self.bunny = pygame.image.load(os.path.join('Assets','bunny.png'))
        self.bunny = pygame.transform.scale(self.bunny,(self.bunny_width,self.bunny_height))
        self.x=bunny_x
        self.y=bunny_y
    
    def get_bunny(self):
        return self.bunny

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def increment(self):
        self.x += 1
    
    def decrement(self):
        self.x -=1


class Game:

    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.bunny1 = Bunny(100,600)
        self.bunny2 = Bunny(800,600)
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
        self.win.blit(self.carrot,(400,200))
        pygame.display.update()


    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.bunny1.x+=1
            self.bunny2.x+=1
            self.draw_window()
        pygame.quit()

