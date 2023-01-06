import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from Test import AddItem, Ranks, AddMember

conn = sqlite3.connect('DB/Database.db')
c = conn.cursor()

def Dactiv():
	raiz = Tk()
	raiz.title("Moni-カ")
	raiz.resizable(0,0)
	raiz.iconbitmap("Recursos/Grafico/Monika2.ico")
	raiz.geometry("1280x720+5+5")
	raiz.config(bg="blue",) # Cambiar el color a las ventanas
	raiz.config(bd=3) # Borde para la raiz 
	raiz.config(relief="sunken") # Tipo de borde para la raiz
	raiz.config(cursor= "hand2") # Tipo de cursor para la raiz

	frame1=Frame(raiz)#se crea un frame
	frame1.pack()#side="(rigth, bottom, etc)" anclado de frame por lado, anchor="(n,s,w,e)" coordenadas de anclado con cardinales, fill expansión en ejes (x,y,both,none), expand="true" para y, 
	frame1.config(bg="#303030")
	frame1.config(width="1280",height="720")
	frame1.config(bd=1)#borde
	#frame1.config(relief="flat")#borde
	frame1.config(cursor="hand2")#cambiar forma del cursor

	Frame1 = Frame(frame1) # Definiendo el tamaño del frame 
	Frame1.place(x=0, y=0) # Empaquetando el frame en la raiz  (side = "top", anchor="n")
	Frame1.config(width="1280",height="720")
	Frame1.config(bg="#303030")
	Frame1.config(bd= 3) # Establecemos el ancho del borde
	Frame1.config(relief= "sunken") # Otro borde es "sunken"
	Frame1.config(cursor= "pirate") # Otro cursor es "hand2", cursores chidos xD


	#--------------------------------#----------------------------------#------------------------------#---------------------#--------

	label1=Label(Frame1, text="HELEMENT")
	label1.grid(row=0, column=0, sticky="w", pady=0, padx=50)
	label1.config(fg="white")
	label1.config(bg="#303030")
	label1.config(font=("Bad Signal",40))

	frameline=Frame(Frame1)
	frameline.grid(row=1, column=0, sticky="w", pady=1, padx=50)
	frameline.config(bg="white")
	frameline.config(width="1180", height="10")

	NuevaActividad = Label(Frame1, text="Nueva Actividad.")
	NuevaActividad.grid(row=2,column=0, sticky="w", pady=1, padx=50) # El sticky sirve para alinearlos a la izquierda, o derecha, por default: centro
	NuevaActividad.config(bg="#303030", fg="white")
	NuevaActividad.config(font=("Verdana", 35))

	Frame1b=Frame(Frame1)
	Frame1b.grid(row=3, column=0, sticky="w", pady=1, padx=50)
	Frame1b.config(bg="black")
	Frame1b.config(width="1180", height="540")

	Frame2=Frame(Frame1b)
	Frame2.place(x=0, y=0)
	Frame2.config(bg="black")
	Frame2.config(width="1180", height="540")

	Descripcion = Label(Frame2, text="Descripcion de la Actividad:")
	Descripcion.grid(row=0,column=0, sticky="w", pady=10) # El sticky sirve para alinearlos a la izquierda, o derecha, por default: centro
	Descripcion.config(bg="black", fg="white")
	Descripcion.config(font=("Verdana", 35))

	def Close():
		raiz.destroy()

	Frameg=Frame(Frame2)
	Frameg.grid(row=2, column=1, sticky="e", padx=5, pady=15)
	Frameg.config(width=130, height=42, bg="#1896c6")

	Guardar = Button(Frameg, text= "Guardar", width=10, command=Close)
	Guardar.place(x=2, y=3)
	Guardar.config(bg="#303030", fg="white", bd=0)
	Guardar.config(font=("Verdana", 14))

	Framec=Frame(Frame2)
	Framec.grid(row=2, column=2, sticky="e", padx=5, pady=15)
	Framec.config(width=130, height=42, bg="#1896c6")

	Cancelar = Button(Framec, text="Cancelar", width=10, command=Close) # con sticky es n,s,e,w
	Cancelar.place(x=2, y=3) # El sticky sirve para alinearlos a la izquierda, o derecha, por default: centro
	Cancelar.config(bg="#303030", fg="white", bd=0)
	Cancelar.config(font=("Verdana", 14))


	#----------------------#---------------------------------#-------------------------------#--------------------#-------------#-------


	Descripcion1 = Text(Frame2, width=53, height=9)
	Descripcion1.grid(row=1, column=0, padx=10, pady=1, columnspan="3")
	Descripcion1.config(fg="blue", bg= "white", bd=5)
	Descripcion1.config(font=("Verdana", 25))

	Barrita = Scrollbar(Frame2, command= Descripcion1.yview) # El scrollbar es basicamente para lograr poner una barra de desplazamiento
	Barrita.grid(row=1,column=3, sticky="nsew") # con el sticky logramos adaptar la barra al tamaño del widget de texto 
	Descripcion1.config(yscrollcommand=Barrita.set) # Esto lo escribimos para que la barra se desplace conforme a lo que escribimos






	#-------------------#---------------------#-----------------------#----------------------#------------------#-----------------#----
	raiz.mainloop()
#Dactiv()




