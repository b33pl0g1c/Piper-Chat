from email import message
import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

from server import receive


HOST='127.0.0.1'
PORT='9989'

class client:
    def __init__(self,host,port):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((host,port))
        msg=tkinter.TK()
        msg.withdraw()
        self.nickname = simpledialog.askstring("Nickname","Please Choose a nickname:",parent=msg)
        self.gui_done=False
        self.running=True
        gui_thread=threading.Thread(target=self.gui_loop)
        receive_thread=threading.Thread(target=receive)
        gui_thread.start()
        receive_thread.start()





