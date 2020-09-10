from tkinter import ttk
from tkinter import *

root=Tk()
class Aplicacao():
    def __init__(self):
        self.root=root
        self.Tela()
        root.mainloop()
    def Tela(self):
        self.root.title('Gerenciador')
        self.root.configure(background='black')
        self.root.geometry('800x600')
        self.root.maxsize(width=1280,height=1024)
        self.root.minsize(width=800,height=600)
Aplicacao()