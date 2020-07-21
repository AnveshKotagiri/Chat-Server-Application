import socket
import select
from _thread import *
import threading
import sys
from datetime import datetime

def chat_server():
 def thread_receive(c):
    while True:
        x=c.recv(500)
        print(x.decode('UTF-8'))
 
 def client_thread(c):
        receive = threading.Thread(target=thread_receive, args=(c,))
        receive.start()
        while True:
              date = datetime.now()
              x = "[ "+str(date)+" ]"+"Server "+":"
              m = input()
              m = x+" "+m
              c.send(m.encode("UTF-8"))
        
            

    
 s= socket.socket(socket.AF_INET,socket.SOCK_STREAM);
 s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
 s.bind((socket.gethostname(),8081))
 s.listen(100)
 print("Server setup succesfull!")
 print("Waiting for the client connection....")

 try:
  while True: 
        c, addr = s.accept() 
        print('Successfully connected to :', addr[0])
        print("You can start the conversation now")
        start_new_thread(client_thread, (c,)) 
 except KeyboardInterrupt:
    s.close()
    sys.exit()
if __name__=="__main__":
    sys.exit(chat_server())
