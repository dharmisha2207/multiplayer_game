import socket
import question

#generating question
q = question.Question()
def generate_ques():
    ques=q.generate_ques()
    return ques

def answer():   
    ans=q.answer()
    return ans

s=socket.socket()
ip='0.0.0.0'
port=9999
s.bind((ip,port))
s.listen()
print("wait for player...")
player1,addr=s.accept()
print("player added!")
def check_ans(ans,pans):
    if str(ans)==pans:
        return True
    else:
        return False
        
        
def send_ques(ques):
    player1.send(ques.encode())

def get_ans():
    pans=(player1.recv(1000000).decode())
    return pans
    
       
while True: 
    ques=generate_ques()
    send_ques(ques)
    pans = get_ans()
    if check_ans(answer(),pans):
        print("yay!")
    else:
        player1.send("try again!")
        pans = get_ans()
        check_ans(answer(), pans)
    
    
    
        

