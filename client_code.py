import Game_World
import network_commn_client
import Player
import sys
import socket
from time import sleep
import os
from time import sleep
import Random_Arithmetic_question
import threading
import pygame

pygame.mixer.init()
pygame.font.init()

class client:
    def __init__(self):
        self.net = network_commn_client.Network_Commn()

        self.id = int(self.net.id)

        print("Your Id is:"+ str(self.id))

        self.game=Game_World.GUI(1000,700,self.id)

        self.run=False

        self.winner_announced=False


    def parse_question(self,ques_str):
        ques=Random_Arithmetic_question.Question_Generator()
        if ques_str[1]=='+' or ques_str[1]=='-':
            ques.a=int(ques_str[0])
            if ques_str[1]=='+':
                ques.c=0
            else:
                ques.c=1
            if len(ques_str)==3:
                ques.b=int(ques_str[2])
            else:
                ques.b=int(ques_str[2])*10+int(ques_str[3])

        else:
            ques.a=int(ques_str[0])*10+int(ques_str[1])
            if ques_str[2]=='+':
                ques.c=0
            else:
                ques.c=1
            if len(ques_str)==4:
                ques.b=int(ques_str[3])
            else:
                ques.b=int(ques_str[3])*10+int(ques_str[4])

        ques.current_ques = str(ques.a) + ques.ops[ques.c] + str(ques.b)
        return ques




    def arrival(self):
        print("Checking if opponent has arrived")
        msg = self.net.receive()
        if msg == "Arrived":
            print("Everyone Arrived")
            self.run=True
        else:
            print("Error")
            exit(-1)

    def driver_code(self):

        if (self.id == 1):
            # Wait indefinitely till server informs of arrival of all participants
            arrival = threading.Thread(target=self.arrival)
            arrival.start()

            while not self.run:
                self.game.draw_waiting()
                sleep(1)

            arrival.join()

        self.game.toggle_run()
        self.run=True


        round= threading.Thread(target=self.Round)
        round.start()

        while self.run:
            self.game.draw_window()



    def Round(self):
        while True:
            #wait for question from server
            question_str = self.net.receive()
            question=self.parse_question(question_str)

            print("question received: "+question.current_ques)

            self.game.update_ques(question)

            #waiting indefinitely for server to announce winner
            winner_announce = threading.Thread(target=self.winner_receive, args=())
            winner_announce.start()

            #while answer is wrong
            #if user entered input event
            #check for correct answer
            #if not correct continue loop
            #if correct send id to server and break loop

            correct=False

            if self.game.play():
                self.net.send(self.id)

            #while self.run:
            #    if self.winner_announced:
            #        self.winner_announced = False
            #        break
            #    winner_id=int(self.net.try_receive())
            #    if winner_id!= -1:
            #        self.winner_announced=True
            #        if winner_id == 1:
            #            self.game.player1_inc()
            #            self.game.player2_dec()
            #        else:
            #            self.game.player2_inc()
            #            self.game.player1_dec()
            #    break
            #    if not correct:
            #        for event in pygame.event.get():
            #            if event.type == pygame.QUIT:
            #                self.run = False
            #            if event.type == pygame.KEYDOWN:
            #                print("key")
            #                if event.key == pygame.K_BACKSPACE:
            #                    self.game.answer = self.game.answer[:-1]
            #                    self.game.update_text()
            #                else:
            #                    self.game.answer += event.unicode
            #                    self.game.update_text()
            #                if event.key == pygame.K_RETURN:
            #                    if int(self.game.answer) == question.answer():
            #                        self.game.answer = ''
            #                        self.game.update_text()
            #                        self.net.send(self.id)
            #                        correct=True
            #                        break
            #                    else:
            #                        self.game.wrong_sound.play()
            #                        self.game.answer = ''
            #                        self.game.update_text()
            #        pygame.display.update()
            #pygame.quit()

            winner_announce.join()

    def winner_receive(self):

        winner_id=int(self.net.receive())
        self.game.winner_announced=True
        if winner_id==1:
            self.game.player1_inc()
            self.game.player2_dec()
        else:
            self.game.player2_inc()
            self.game.player1_dec()

        #if self.id==winner_id:
        #    print()
            #victory sound
        #else:
        #    print()
            #loss sound

