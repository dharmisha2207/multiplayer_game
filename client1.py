import socket

s=socket.socket()

ip="10.184.42.54"
port=9999

s.connect((ip,port))
print("connected")
while True:
    ques=s.recv(1000000).decode()
    print(ques)
    ans=input("your message:>>>")
    s.send(ans.encode())

