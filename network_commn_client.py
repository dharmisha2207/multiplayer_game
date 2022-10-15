import socket
import sys
import os
from time import sleep

class Network_Commn:

    def __init__(self):
        self.server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.host = "localhost"
        self.port = 8080
        self.addr = (self.host, self.port)
        self.id = self.connect()
        print("Connected to Server")


    def connect(self):
        self.server_conn.connect(self.addr)
        return self.server_conn.recv(2048).decode()

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            reply = self.client.recv(2048).decode()
            return reply
        except socket.error as e:
            return str(e)

    def receive(self):
        self.server_conn.settimeout(0.5)
        while True:
            try:
                msg = self.server_conn.recv(4096).decode()
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
                return msg


