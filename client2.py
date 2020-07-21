import socket
import select
from _thread import *
import threading
import sys
from datetime import datetime

def chat_client():
 def thread_receive(s):
    while True:
            x=s.recv(500)
            if 'quit' in str(x):
                sys.exit()
            
            print(x.decode('UTF-8'))

 s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 s.connect((socket.gethostname(),8081))
    

 receive = threading.Thread(target=thread_receive, args=(s,))
 receive.start()
 print("Successfully connected to server")
 print("You can start the conversation now")
 while True:
          date = datetime.now()
          x = "[ "+str(date)+" ]"+"Client "+" :"
          
          m = input()
          m = x+" "+m
          
          s.send(m.encode("UTF-8"))

if __name__=="__main__":
    sys.exit(chat_client())
    
