import socket
from Tkinter import *
import threading
import pygame

class google():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("w.mp3")
        self.root = Tk()
        self.root.geometry("600x600")
        self.root.configure(background="#00D1FC")
        self.root.minsize(height=600,width=600)
        self.root.maxsize(height=600, width=600)
        self.ely = Entry(self.root, width=30, font=2)
        self.ely.place(x=200,y=550)
        self.bull = Button(self.root, text="send", height=5, width=7, bg="#6A6C6D", command=self.senddata)
        self.bull.place(x=0,y=500)
        self.textbox = Text(self.root, height=30, width=82, bg="#FAAB02")
        #self.textbox.config(state=DISABLED)
        self.textbox.place(x=10,y=10)
        t1 = threading.Thread(target=self.connection)
        t1.daemon = True
        t1.start()
        mainloop()



    def connection(self):
        self.host = "127.0.0.1"
        self.port = 2222
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        while True:
            data = self.s.recv(2020)
            pygame.mixer.music.play()
            meg ="\nserver~> " + data
            self.textbox.insert(END, meg)

    def senddata(self):
        Valuedata = self.ely.get()
        self.s.send(str(Valuedata))

f = google()

f
