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
        self.step = 1
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
            if self.x + self.step > x-50 and self.y - self.step < y:
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
            if self.x - self.step < x+50 and self.y - self.step < y:
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


class Game:

    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.bunny1 = Bunny(100,600)
        self.bunny2 = Bunny(800,600)
        self.carrot_x = 450
        self.carrot_y = 200
        self.bg = pygame.image.load(os.path.join('Assets','bg.jpeg'))
        self.bg = pygame.transform.scale(self.bg,(width,height))
        self.carrot = pygame.image.load(os.path.join('Assets','carrot.png'))
        self.carrot = pygame.transform.scale(self.carrot,(100,100))
        self.win = pygame.display.set_mode((width,height))
        self.font = pygame.font.SysFont('comicsans', 30)
        self.quesgen = question.Question()
        self.pathx1 = pygame.Rect(100, 650, 370, 20)
        self.pathx2 = pygame.Rect(520, 650, 350, 20)
        self.pathy1 = pygame.Rect(450, 250, 20, 400)
        self.pathy2 = pygame.Rect(520, 250, 20, 400)
       

        

    def draw_window(self):
        pygame.display.set_caption("Reach the Goal")
        self.win.blit(self.bg, (0,0))

        self.player1score = self.font.render("Score : " + str(self.bunny1.get_score()), 1,(255,255,255))
        self.player2score = self.font.render("Score : " + str(self.bunny2.get_score()), 1,(255,255,255))
        self.win.blit(self.player1score, (100,100))
        self.win.blit(self.player2score, (800,100))

        self.ques = self.font.render(self.quesgen.generate_ques(),1, (255,255,255))
        self.win.blit(self.ques, (450,100))

        pygame.draw.rect(self.win, (255,255,255), self.pathx1)
        pygame.draw.rect(self.win, (255,255,255), self.pathx2)
        pygame.draw.rect(self.win, (255,255,255), self.pathy1)
        pygame.draw.rect(self.win, (255,255,255), self.pathy2)

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

