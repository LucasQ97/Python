import Database
from tkinter import *
import random

root = Tk()
root.title("Sistema de Reservas")



########################
lista = []
def showDatos():
   print(len(lista))
   lista.append({'Mesa': e1.get(), 'Cantidad Personas': e2.get(), 'Horario de reserva': e3.get(),'Fecha' : e4.get() , 'Nombre' : e5.get()})
########################

colores = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'cyan', 'purple']

def changeColors():
    for x in colores:
        root.configure(bg=random.choice(colores))


def entrada(valor,ancho,fila,columna):
    entry = Entry(root, width= ancho)
    entry.grid(row=fila, column=columna) 
    entry.insert(0,valor)
    return entry

def leer():
    conexion = Database.conectar()
    con = conexion.cursor()
    try:
        con.execute('select * from MESAS;')
        resultado = con.fetchall()
        for x in resultado:
            print(x)
    except:
        print('Algo salio mal en leer la reserva')
    finally:
        con.close()

def alta():
    conexion = Database.conectar()
    con = conexion.cursor()
    try:
        sql = "INSERT INTO MESAS (MESA, CANT_PERSONAS, RESERVA, FECHA ,NOMBRE) VALUES (%s, %s, %s, %s, %s)"
        datos = (e1.get(), e2.get(), e3.get(), e4.get(), e5.get())
        con.execute(sql, datos)
        conexion.commit()
        print('Reserva agendada')
    except:
        print('Algo salio mal en la reserva')

titulo = Label(root,text="Ingrese datos de la reserva", bg="DarkOrchid3", fg="thistle1")
titulo.grid(row=0, column=0, columnspan=4, padx=1, pady=1, sticky=W + E)

Label(root,text="Mesa").grid(row=1,column=0,sticky=W)
Label(root,text="Cantidad Personas").grid(row=2,column=0,sticky=W)
Label(root,text="Horario").grid(row=3,column=0,sticky=W)
Label(root,text="Fecha").grid(row=4,column=0,sticky=W)
Label(root,text="Nombre").grid(row=5,column=0,sticky=W)


e1 = entrada('Mesa 1',20,1,1)
e2 = entrada('2',20,2,1)
e3 = entrada('19:00',20,3,1)
e4 = entrada('1-12-2020',20,4,1)
e5 = entrada('Lucas',20,5,1)

base = Button(root, text="Crear bd",command=Database.creardb).grid(row=6,column=0, ipadx=20,padx=10)
alta = Button(root, text="alta", command=alta).grid(row=6,column=1)
sorpresa = Button(root, text="Sorpresa",command=changeColors).grid(row=6,column=2, ipadx=20,padx=10)
drop = Button(root, text="DROP",command=Database.drop).grid(row=6,column=3, ipadx=20,padx=10)
leer = Button(root, text="Ver Reservas",command=leer).grid(row=3,column=2, ipadx=20,padx=10)

mainloop()
