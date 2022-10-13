import socket
from _thread import *
import GUI
import Random_Arithmetic_question

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

        #list to store addresses of connected clients
        self.clients=[]

        #Initialize Game world
        self.game=Game_World.Game(600,600)
        self.q=Random_Arithmetic_question.Question_Generator()

    def connect_to_players(self):

        #Listen for request of clients to connect
        #It will accept at max 2 connections as it is a 2 player game
        self.s.listen(2)
        print("Waiting for a connection")
        Player_Id=1
        while True:
            conn, addr = self.s.accept()
            self.clients=self.clients+[conn,addr]
            print("Connected to: ", addr)

            #Assigning each player an Id in serial order of connection requests
            conn.send(str.encode(Player_Id))
            Player_Id=Player_Id+1


    def run(self):

        self.connect_to_players()

        #Informing Players that all have arrived
        for i in range(self.PLAYERS):
            msg="Arrived"
            print("Sending: " + msg)

            self.clients[i][0].sendall(str.encode(msg))


        while True:
            curr_ques=self.q.generate_ques()

            #Receiving cue from all players that they are ready for next question
            for i in range(self.PLAYERS):
                data = self.clients[i][0].recv(2048)
                ready = data.decode('utf-8')

                print("Recieved: " + ready)

                if(ready=="Ready"):

                    reply="OK"
                    print("Sending: " + reply)

                    self.clients[i][0].sendall(str.encode(reply))

            for i in range(self.PLAYERS):

                print("Sending: " + curr_ques)

                self.clients[i][0].sendall(str.encode(curr_ques))


            #Wait for response from someone, if it happens send to all the winner and continue








        #print("Connection Closed")
        #conn.close()

