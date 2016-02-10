from tkinter import *
import modulos

def escribe():
    lista.insert(END, "Hola")

def listar():
    agenda = open ("agenda_telefonica.csv")
    numero = 0    
    for i in range(0,10):
        lectura = agenda.readline()
	##Print(lectura.replace(",","\t\t"))
        lista.insert(END,lectura.replace(",","   "))
        numero=numero+1
    agenda.close()

f = Frame (height=300,width=300)
f.pack(padx=15,pady=15)

logoimg=PhotoImage(file="imghj.gif")
etiquetalogo = Label(f,image = logoimg)
etiquetalogo.pack(side=TOP, padx=10,pady=10)

titulo = Label (f, text="Agenda Telefónica", fg="blue", font=("Arial",24))
titulo.pack(side=TOP, padx=10, pady=10)

autor = Label (f, text="Pedro Rafael")
autor.pack(side=TOP, padx=10, pady=10)

campo = Entry(f,textvariable = 0)
campo.pack(side=TOP, padx=10, pady=10)

##boton1 = Button(f,text="Listar elementos", command=lambda:modulos.listar(int(Entry.get(campo))))
boton1 = Button(f,text="Listar elementos", command=listar)
boton1.pack(side=BOTTOM, padx=10,pady=10)

lista = Listbox(f)
lista.pack(side=TOP, padx=10,pady=10)
