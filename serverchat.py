import socket
from Tkinter import *
import  threading
import pygame
class google():
    def __init__(self):
        self.root = Tk()
        pygame.mixer.init()
        pygame.mixer.music.load("w.mp3")
        self.root.geometry("600x600")
        self.root.configure(background="#00D1FC")
        self.root.minsize(height=600,width=600)
        self.root.maxsize(height=600, width=600)
        self.ely = Entry(self.root, width=30, font=20)
        self.ely.place(x=200,y=550)
        self.bull = Button(self.root, text="send", height=5, width=7, bg="#6A6C6D",command=self.send)
        self.bull.place(x=0,y=500)
        self.textbox = Text(self.root, height=30, width=82, bg="#FAAB02")
        #self.textbox.config(state=DISABLED)
        self.textbox.place(x=10,y=10)
        t1 = threading.Thread(target=self.Servise)
        t1.daemon = True
        t1.start()
        mainloop()
    def Servise(self):
        self.host= "127.0.0.1"
        self.port= 667
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print  "server started"
        while True:
            self.s.bind((self.host,self.port))
            self.s.listen(5)
            self.conn, self.addr = self.s.accept()
            print  "hello" + str(self.addr)
            while True:
                dada = self.conn.recv(2020)
                pygame.mixer.music.play()
                datainsert= "\nclient~> "+dada
                self.textbox.insert(END, datainsert)

    def send(self):
        datasend = self.ely.get()
        self.conn.send(str(datasend))



f = google()
def main():
    pygame.init()
    f
main()
