import pygame
import os
import question
import Player
pygame.font.init()

class GUI:

    def __init__ (self, width, height):
        self.width = width
        self.height = height
        self.bunny1 = Player.Bunny(100,600)
        self.bunny2 = Player.Bunny(800,600)
        self.carrot_x = 450
        self.carrot_y = 200
        self.bg = pygame.image.load(os.path.join('Assets','bg.jpeg'))
        self.bg = pygame.transform.scale(self.bg,(width,height))
        self.carrot = pygame.image.load(os.path.join('Assets','carrot1.png'))
        self.carrot = pygame.transform.scale(self.carrot,(100,150))
        self.win = pygame.display.set_mode((width,height))
        self.font = pygame.font.SysFont('comicsans', 30)
        self.quesgen = question.Question()
        self.ques = self.font.render(self.quesgen.generate_ques(),1, (255,255,255))
        self.pathx1 = pygame.Rect(100, 650, 360, 10)
        self.pathx2 = pygame.Rect(510, 650, 350, 10)
        self.pathy1 = pygame.Rect(450, 275, 10, 375)
        self.pathy2 = pygame.Rect(510, 275, 10, 375)
        self.answer = ''
        self.answer_rect = pygame.Rect(450,150,100,40)
        self.text_surface = self.font.render(self.answer,True,(0,0,0))
       

    def draw_window(self):
        pygame.display.set_caption("Reach the Goal")
        self.win.blit(self.bg, (0,0))

        self.player1score = self.font.render("Score : " + str(self.bunny1.get_score()), 1,(255,255,255))
        self.player2score = self.font.render("Score : " + str(self.bunny2.get_score()), 1,(255,255,255))
        self.win.blit(self.player1score, (100,100))
        self.win.blit(self.player2score, (800,100))

       
        self.win.blit(self.ques, (450,100))
        pygame.draw.rect(self.win,(255,255,255), self.answer_rect)
        self.win.blit(self.text_surface,self.answer_rect)

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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.answer = self.answer[:-1]
                        self.update_text()
                    else:
                        self.answer += event.unicode
                        self.update_text()
                    if event.key == pygame.K_RETURN:
                        if int(self.answer) == self.quesgen.answer():
                            self.answer=''
                            self.update_text()
                            self.update_ques()
                        else:
                            self.answer=''
                            self.update_text()


            self.player1_inc()
            self.player2_inc()       
            self.draw_window() 
        pygame.quit()

    def update_text(self):
        self.text_surface = self.font.render(self.answer,True,(0,0,0))
        self.win.blit(self.text_surface,self.answer_rect)

    def get_answer(self):
        return self.answer
    
    def update_ques(self):
        self.quesgen = question.Question()
        self.ques = self.font.render(self.quesgen.generate_ques(),1, (255,255,255))
        self.win.blit(self.ques, (450,100))


