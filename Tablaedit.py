from tkinter import *
from tkinter import ttk
import mariadb
import sqlite3

class Alumno:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Montacargas")
        marco=LabelFrame(self.ventana,text="Listas")
        marco.grid(row=0,column=0,columnspan=3,pady=20)
        #Nombre
        Label(marco,text="Producto").grid(row=0,column=0)
        self.nombre=Entry(marco)
        self.nombre.grid(row=0,column=1)
        self.nombre.focus()
        #Clave
        Label(marco,text="Cantidad").grid(row=1,column=0)
        self.cant=Entry(marco)
        self.cant.grid(row=1,column=1)
        #Boton
        self.crear=ttk.Button(marco,text="Crear Producto",command=self.agregarRegistro)
        self.crear.grid(row=2,columnspan=2,sticky=W+E)
        self.editar=ttk.Button(marco,text="Editar Producto",command=self.editarRegistro)
        self.editar.grid(row=3,columnspan=2,sticky=W+E)
        self.editar["state"]="disabled"
        self.borrar=ttk.Button(marco,text="Borrar Producto",command=self.borrarRegistro)
        self.borrar.grid(row=4,columnspan=2,sticky=W+E)
        self.borrar["state"]="disabled"
        #Mensaje
        self.mensaje=Label(text='',fg='green')
        self.mensaje.grid(row=5,column=0,columnspan=2,sticky=W+E)
        #Tabla
        self.tabla=ttk.Treeview(self.ventana,columns=2)
        self.tabla.bind("<Double-Button-1>",self.doubleClickTabla)
        self.tabla.grid(row=6,column=0,columnspan=2)
        self.tabla.heading("#0",text="Nombre",anchor=CENTER)
        self.tabla.heading("#1",text="Cantidad",anchor=CENTER)

    def queryAlumnos(self,query):
        #global cur
        conn=sqlite3.connect("Lista.db")
        cur=conn.cursor()
        cur.execute(query)
        conn.commit()
        return cur

    def mostrarDatos(self):
        registros=self.tabla.get_children()
        for registro in registros:
            self.tabla.delete(registro)
        cur=self.queryAlumnos("SELECT `nombre`,`cant` FROM `Productos`")
        for (nombre,cant) in cur:
            self.tabla.insert('',0,text=nombre,values=cant)

    def agregarRegistro(self):
        if len(self.nombre.get())!=0 and len(self.cant.get())!=0:
            query="INSERT INTO Productos VALUES (NULL, '"+self.nombre.get()+"', "+self.cant.get()+")"
            self.queryAlumnos(query)
            self.mensaje['text']="El Producto "+self.nombre.get()+" se ha insertado exitosamente"
            self.nombre.delete(0,END)
            self.cant.delete(0,END)
            self.nombre.focus()
        else:
            self.mensaje['text']="Los campos no pueden estar vacias humano tonto"
        self.mostrarDatos()

    def editarRegistro(self):
        if len(self.nombre.get())!=0 and len(self.cant.get())!=0:
            query="UPDATE `Productos` set nombre='"+self.nombre.get()+"',cant="+self.cant.get()+" where cant="+self.claveVieja+"; "
            self.queryAlumnos(query)
            self.mensaje['text']="El Producto "+self.nombre.get()+" se a actualizado exitosamente"
            self.nombre.delete(0,END)
            self.cant.delete(0,END)
            self.nombre.focus()
        else:
            self.mensaje['text']="Los campos no pueden estar vacias humano tonto"
        self.mostrarDatos()
        self.crear["state"]="normal"
        self.editar["state"]="disabled"
        self.borrar["state"]="disabled"

    def borrarRegistro(self):
        query="delete from Productos where cant='"+self.claveVieja+"'"
        self.queryAlumnos(query)
        self.mensaje['text']="El Producto "+self.nombre.get()+" se a borrado exitosamente"
        self.nombre.delete(0,END)
        self.cant.delete(0,END)
        self.nombre.focus()
        self.mostrarDatos()
        self.crear["state"]="normal"
        self.editar["state"]="disabled"
        self.borrar["state"]="disabled"        

    def doubleClickTabla(self,event):
        self.claveVieja=str(self.tabla.item(self.tabla.selection())["values"][0])
        self.nombre.delete(0,END)
        self.cant.delete(0,END)
        self.crear["state"]="disable"
        self.editar["state"]="normal"
        self.borrar["state"]="normal"
        self.nombre.insert(0,str(self.tabla.item(self.tabla.selection())["text"]))
        self.cant.insert(0,str(self.tabla.item(self.tabla.selection())["values"][0]))

if __name__=="__main__":
    ventana=Tk()
    aplicacion=Alumno(ventana)
    aplicacion.mostrarDatos()
    ventana.mainloop()