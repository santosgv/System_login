from db import checklogin,creatlogin
from tkinter import *

root=Tk()

class Funcoes():
    def validar(self):
        status=checklogin(self.entlog.get(),self.entpwd.get())
        if status ==True:
            self.lbtext['text']=('Login acept')
            self.lbtext.place(relx=0.2, rely=0.80)
        elif status ==False:
            self.lbtext['text']= ('Login or password incorrect')
            self.lbtext.place(relx=0.1, rely=0.80)
        else:
            self.lbtext['text'] = (status)
            self.lbtext.place(relx=0.01, rely=0.80)

    def Criar(self):
        situacao=creatlogin(self.login.get(),self.password.get())
        if situacao ==('Conta Criada com sucesso'):
            self.login.delete(0,END)
            self.password.delete(0,END)
            self.lbstatus['text']=('Conta Criada com sucesso')
            self.btcreat.destroy()

        if situacao ==('Conta ja em uso'):
            self.lbstatus['text']=('Conta ja em uso')

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
        self.btlog.place(relx=0.5,rely=0.60)

        self.btacc=Button(self.main,text='New',command=self.Newwindow)
        self.btacc.place(relx=0.10,rely=0.60)

        self.lbtext=Label(self.main,text='Situation',bg='white')
        self.lbtext.place(relx=0.2,rely=0.80)
    def Newwindow(self):
        nwwindow=Toplevel(self.root,bg='white')
        nwwindow.geometry('250x100')
        nwwindow.title('Create New Accont')
        nwwindow.resizable(False,False)
        Label(nwwindow,text='Login',bg='white').place(relx=0.01,rely=0.20)
        Label(nwwindow, text='Password',bg='white').place(relx=0.01, rely=0.40)
        self.lbstatus=Label(nwwindow, text='status',bg='white')
        self.lbstatus.place(relx=0.01, rely=0.70)
        self.login=Entry(nwwindow)
        self.login.place(relx=0.25,rely=0.20)
        self.password=Entry(nwwindow,show="*")
        self.password.place(relx=0.25, rely=0.40)
        self.btcreat=Button(nwwindow,text='Creat',command=self.Criar)
        self.btcreat.place(relx=0.4,rely=0.70)

Aplicacao()