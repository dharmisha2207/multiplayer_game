import socket
import Game_World
import Random_Arithmetic_question
import Player
import sys
import os
from time import sleep
import threading

class Server:
    PLAYERS=2
    def __init__(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server = 'localhost'
        self.port = 8080

        self.server_ip = socket.gethostbyname(self.server)

        try:
            self.s.bind((self.server, self.port))

        except socket.error as e:
            print(str(e))

        print("Server started")

        #list to store addresses of connected clients
        self.clients=[]

        #Initialize Game world
        #self.game=Game_World.GUI(600,600)

        #Create Question Generator object
        self.q=Random_Arithmetic_question.Question_Generator()

        self.winner_received=False
        self.curr_winner="-1"

    def connect_to_players(self):

        #Listen for request of clients to connect
        #It will accept at max 2 connections as it is a 2 player game
        self.s.listen(2)
        print("Waiting for a connection..")
        Player_Id=1
        while Player_Id<3:
            conn, addr = self.s.accept()
            self.clients=self.clients+[[conn,addr]]
            print("Connected to: ", addr)

            #Assigning each player an Id in serial order of connection requests
            Player_Id_str=str(Player_Id)
            conn.send(str.encode(Player_Id_str))

            Player_Id=Player_Id+1

    def Player1_response(self):

        self.clients[0][0].settimeout(2)
        while self.winner_received==False:
            try:
                id = int(self.clients[0][0].recv(4096).decode())
            except socket.timeout as e:
                err = e.args[0]
                # this next if/else is a bit redundant, but illustrates how the
                # timeout exception is setup
                if err == 'timed out':
                    continue
                else:
                    print(e)
                    sys.exit(1)
            except socket.error as e:
                # Something else happened, handle error, exit, etc.
                print(e)
                sys.exit(1)
            else:
                if self.winner_received==False:
                    self.winner_received=True
                    self.curr_winner=id
                    #if id==1:
                        #self.game.player1_inc()
                        #self.game.player2_dec()
                    #else:
                        #self.game.player2_inc()
                        #self.game.player1_dec()
                    for i in range(self.PLAYERS):
                        self.clients[i][0].sendall(str.encode(id))
                return


    def Player2_response(self):

        self.clients[1][0].settimeout(2)
        while self.winner_received==False:
            try:
                id = int(self.clients[1][0].recv(4096).decode())
            except socket.timeout as e:
                err = e.args[0]
                # this next if/else is a bit redundant, but illustrates how the
                # timeout exception is setup
                if err == 'timed out':
                    continue
                else:
                    print(e)
                    sys.exit(1)
            except socket.error as e:
                # Something else happened, handle error, exit, etc.
                print(e)
                sys.exit(1)
            else:
                if self.winner_received==False:
                    self.winner_received=True
                    self.curr_winner=id
                    #if id==1:
                        #self.game.player1_inc()
                        #self.game.player2_dec()
                    #else:
                        #self.game.player2_inc()
                        #self.game.player1_dec()
                    for i in range(self.PLAYERS):
                        self.clients[i][0].sendall(str.encode(id))
                return



    def run(self):

        self.connect_to_players()

        #Informing Player-1 that Player-2 has arrived
        msg="Arrived"
        print("Sending all Arrived to Player-1....")
        self.clients[0][0].sendall(str.encode(msg))



        while True:
            self.curr_winner="-1"
            curr_ques=self.q.generate_ques()

            #Receiving cue from all players that they are ready for next question
            #for i in range(self.PLAYERS):
            #    data = self.clients[i][0].recv(2048)
            #    ready = data.decode('utf-8')

            #    print("Recieved: " + ready)

            #    if(ready=="Ready"):

            #        reply="OK"
            #        print("Sending: " + reply)

            #        self.clients[i][0].sendall(str.encode(reply))

            for i in range(self.PLAYERS):

                print("Sending question: " + curr_ques)

                self.clients[i][0].sendall(str.encode(curr_ques))


            #Wait for response from someone 2 threads
            P1_response= threading.Thread(target=self.Player1_response, args=())
            P1_response.start()

            P2_response = threading.Thread(target=self.Player2_response, args=())
            P2_response.start()

            P1_response.join()
            P2_response.join()



