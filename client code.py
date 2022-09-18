import socket
from tkinter.filedialog import *
import os
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(500)
try:
    l=input("Enter ip address of server: ")
    c.connect((l,1233))
    f_path=askopenfilename()
    f_name=os.path.basename(f_path)
    c.send(f_name.encode("utf-8"))
    with open(f_path,"rb") as f1:
        l=f1.read()
        #print(len(l))
        c.sendall(l)
    print("succesfully sent:")
    #print(c.recv(30))
    f1.close()
#print(c.recv(30))
    c.close()
except:
    print("incorrect ip or server is not ready")