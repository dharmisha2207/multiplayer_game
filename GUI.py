import pygame
import os
import Random_Arithmetic_question
import Player
pygame.mixer.init()
pygame.font.init()

class GUI:

    def __init__ (self, width, height,id):
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
        self.quesgen = Random_Arithmetic_question.Question_Generator()
        self.ques = self.font.render(self.quesgen.generate_ques(),1, (255,255,255))
        self.pathx1 = pygame.Rect(100, 650, 360, 10)
        self.pathx2 = pygame.Rect(510, 650, 350, 10)
        self.pathy1 = pygame.Rect(450, 275, 10, 375)
        self.pathy2 = pygame.Rect(510, 275, 10, 375)
        self.answer = ''
        self.answer_rect = pygame.Rect(450,150,100,40)
        self.text_surface = self.font.render(self.answer,True,(0,0,0))
        self.wrong_sound = pygame.mixer.Sound(os.path.join('Assets','wrong.mp3'))
        self.hop = pygame.mixer.Sound(os.path.join('Assets','hop.mp3'))
        self.winner = pygame.mixer.Sound(os.path.join('Assets','win.mp3'))
        self.run = False
        self.id = id
        self.winner_announced = False
        
    def window(self):

        pygame.display.set_caption("Reach the Goal")
        self.win.blit(self.bg, (0,0))
        if self.id == 1:
            self.player1score = self.font.render("You : " + str(self.bunny1.get_score()), 1,(255,255,255))
            self.player2score = self.font.render("Opponent : " + str(self.bunny2.get_score()), 1,(255,255,255))
        else:
            self.player1score = self.font.render("Opponent : " + str(self.bunny1.get_score()), 1,(255,255,255))
            self.player2score = self.font.render("You : " + str(self.bunny2.get_score()), 1,(255,255,255))

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
    
    def draw_window(self):
        while self.run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = True
                self.window()

    def player1_inc(self):
        self.bunny1.left_increment(self.carrot_x, self.carrot_y)
        self.hop.play()
        if self.bunny1.get_score()==13:
            self.draw_winner("Bunny 1 won!!")
    
    def player2_inc(self):
        self.bunny2.right_increment(self.carrot_x, self.carrot_y)
        self.hop.play()
        if self.bunny2.get_score()==13:
            self.draw_winner("Bunny 2 won!!")
    
    def player1_dec(self):
        self.bunny1.left_decrement(self.carrot_x, self.carrot_y)
        self.wrong_sound.play()
    
    def player2_dec(self):
        self.bunny2.right_decrement(self.carrot_x, self.carrot_y)
        self.wrong_sound.play()

    def draw_winner(self,text):
        font = pygame.font.SysFont('comicsans', 100)
        winner = font.render(text, 1, (255,255,255))
        self.draw_window()
        self.win.blit(winner,(self.width/2-winner.get_width()/2, self.height/2-winner.get_height()/2))
        pygame.display.update()
        self.winner.play()
        pygame.time.delay(5000)
        pygame.quit()
    
    def toggle_run(self):
        if self.run==True:
            self.run=False
        self.run=True

    def waiting_win(self):
        pygame.display.set_caption("Reach the Goal")
        self.win.blit(self.bg, (0,0))
        font = pygame.font.SysFont('comicsans', 70)
        waiting = font.render("Please wait for the opponent!", 1, (255,255,255))
        self.win.blit(waiting,(self.width/2-waiting.get_width()/2, self.height/2-waiting.get_height()/2))
        pygame.display.update()

    def draw_waiting(self):
        while not(self.run):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = True
            self.waiting_win()

    def play(self):
        while not(self.winner_announced):
            while self.run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
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
                                return True
                            else:
                                self.wrong_sound.play()
                                self.answer=''
                                self.update_text()
            pygame.quit()
        self.winner_announced = False

    def update_text(self):
        self.text_surface = self.font.render(self.answer,True,(0,0,0))
        self.win.blit(self.text_surface,self.answer_rect)

    def get_answer(self):
        return self.answer
    
    def update_ques(self,quesgen):
        self.quesgen = quesgen
        self.ques = self.font.render(self.quesgen.generate_ques(),1, (255,255,255))
        self.win.blit(self.ques, (450,100))