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

class client:
    def __init__(self):
        self.net = network_commn_client.Network_Commn()

        self.id = int(self.net.id)

        print("Your Id is:"+ str(self.id))

        self.game=Game_World.GUI(1000,700,self.id)

        self.run=False


    def parse_question(self,ques_str):
        ques=Random_Arithmetic_question.Question_Generator()
        if ques_str[1]=='+' or ques_str[1]=='-':
            ques.a=ques_str[0]
            if ques_str[1]=='+':
                ques.c=0
            else:
                ques.c=1
            if len(ques_str)==3:
                ques.b=int(ques_str[2])
            else:
                ques.b=int(ques_str[2]*10+ques_str[3])

        else:
            ques.a=int(ques_str[0])*10+int(ques_str[1])
            if ques_str[2]=='+':
                ques.c=0
            else:
                ques.c=1
            if len(ques_str)==4:
                ques.b=int(ques_str[3])
            else:
                ques.b=int(ques_str[3]*10+ques_str[4])

        return ques

    def draw_GUI(self):
        while self.run:
            self.game.draw_window()
            sleep(2)


    def arrival(self):
        print("Checking if opponent has arrived")
        msg = self.net.receive()
        if msg == "Arrived":
            print("Everyone Arrived")
        else:
            print("Error")
            exit(-1)

    def driver_code(self):


        arrival = threading.Thread(target=self.arrival)
        arrival.start()

        if (self.id == 1):
            # Wait indefinitely till server informs of arrival of all participants
            while not self.run:
                self.game.draw_waiting()
                sleep(1)

        self.game.toggle_run()
        self.run=True

        #Draw Game world
        if self.id==1:
            arrival.join()

        drawing_thread = threading.Thread(target=self.draw_GUI, args=())
        drawing_thread.start()

        while True:
            #wait for question from server
            question_str = self.net.receive()
            question=self.parse_question(question_str)

            print("question received: "+question_str)

            self.game.update_ques(question)

            #waiting indefinitely for server to announce winner
            winner_announce = threading.Thread(target=self.winner_receive, args=())
            winner_announce.start()

            #while answer is wrong
            #if user entered input event
            #check for correct answer
            #if not correct continue loop
            #if correct send id to server and break loop
            if self.game.play():
                self.net.send(self.id)

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

