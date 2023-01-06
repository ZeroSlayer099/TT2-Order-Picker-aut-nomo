from tkinter import *
from tkinter import ttk
import mariadb
import sqlite3

class Alumno:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Hola mundo")
        marco=LabelFrame(self.ventana,text="Alumno")
        marco.grid(row=0,column=0,columnspan=3,pady=20)
        #Nombre
        Label(marco,text="Nombre").grid(row=0,column=0)
        self.nombre=Entry(marco)
        self.nombre.grid(row=0,column=1)
        self.nombre.focus()
        #Clave
        Label(marco,text="Clave").grid(row=1,column=0)
        self.clave=Entry(marco)
        self.clave.grid(row=1,column=1)
        #Boton
        self.crear=ttk.Button(marco,text="Crear alumno",command=self.agregarRegistro)
        self.crear.grid(row=2,columnspan=2,sticky=W+E)
        self.editar=ttk.Button(marco,text="Editar alumno",command=self.editarRegistro)
        self.editar.grid(row=3,columnspan=2,sticky=W+E)
        #Mensaje
        self.mensaje=Label(text='',fg='green')
        self.mensaje.grid(row=4,column=0,columnspan=2,sticky=W+E)
        #Tabla
        self.tabla=ttk.Treeview(self.ventana,columns=2)
        #self.tabla.bind("<Double-Button-1>",self.doubleClickTabla)
        self.tabla.grid(row=5,column=0,columnspan=2)
        self.tabla.heading("#0",text="Nombre",anchor=CENTER)
        self.tabla.heading("#1",text="Clave",anchor=CENTER)

    def consultaproducto(self,query):
        conn=sqlite3.connect("Lista.db")
        cur=conn.cursor()
        cur.execute(query)
        return cur

    def Read():
        global Nombre 
        global Unidades
        Nombre=nombre.get()
        Unidades=cant.get()

    def mostrardatos(self):
        cur=self.consultaproducto("SELECT 'nombre', 'cant' FROM `Productos`")
        for (nombre,cant) in cur:
            print(nombre,cant)

    def agregarRegistro(self):
        print(" ")

    def editarRegistro(self):
        print(" ")

if __name__=="__main__":
    ventana=Tk()
    aplicacion=Alumno(ventana)
    aplicacion.mostrardatos()
    ventana.mainloop()