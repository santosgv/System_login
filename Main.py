from Check_list.db import checklogin
from tkinter import *

root=Tk()

class Funcoes():
    def validar(self):
        status=checklogin(self.entlog.get(),self.entpwd.get())
        if status ==True:
            self.lbtext['text'] = ('Login acept')
            self.lbtext.place(relx=0.2, rely=0.80)
        elif status ==False:
            self.lbtext['text'] = ('Login or password incorrect')
            self.lbtext.place(relx=0.1, rely=0.80)
        else:
            self.lbtext['text'] = (status)
            self.lbtext.place(relx=0.01, rely=0.80)
class Aplicacao(Funcoes):
    def __init__(self):
        self.root=root
        self.Tela()
        self.Frame()
        self.labelAndBotton()
        root.mainloop()
    def Tela(self):
        self.root.title('System_login')
        self.root.configure(background='black')
        self.root.geometry('300x200')
        self.root.maxsize(width=1280,height=1024)
    def Frame(self):
        self.main=Frame(self.root,bg='white')
        self.main.place(relx=0.01,rely=0.01,relwidth=0.98,relheight=0.98)
    def labelAndBotton(self):
        self.lblog=Label(self.main,bg='white',text='Login')
        self.lblog.place(relx=0.05,rely=0.15)
        self.entlog=Entry(self.main)
        self.entlog.place(relx=0.20,rely=0.15,width=150)

        self.lbpwd=Label(self.main,bg='white',text='Senha')
        self.lbpwd.place(relx=0.05,rely=0.45)
        self.entpwd=Entry(self.main, show="*")
        self.entpwd.place(relx=0.20,rely=0.45,width=150)

        self.btlog=Button(self.main,text='Logar',command=self.validar)
        self.btlog.place(relx=0.3,rely=0.60)

        self.lbtext=Label(self.main,text='Status',bg='white')
        self.lbtext.place(relx=0.2,rely=0.80)
Aplicacao()