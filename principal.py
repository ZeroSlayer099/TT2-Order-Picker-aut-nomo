from tkinter import *
import tkinter as tk
import sys
import os
from os import listdir, sep
from os.path import isdir, join, abspath
from PIL import Image, ImageTk
from itertools import count, cycle
from proyectoherr import herramientas
from proyectoactiv import proyactiv
from proyectofinanza import proyfin
from Inventario import reporte as inventario
import sqlite3
from tkinter import ttk
import tkinter.font as tkFont
import time
from time import *
from time import sleep
#from time import clock
from proyectointer import proyecton
from Nuevalist import nuevlista
from time import time

#import commands
#result=commands.getoutput('/usr/bin/python tuapp.py')
# conn = sqlite3.connect('DB/Database.db')
# c = conn.cursor()

#global rec

#def clickIZ(event):
#    proyecton()


def Newgif():
    #global rec
    #rec=Recognition()
    vozm2=ImageLabel(frame7)
    vozm2.grid(row=0, column=0, sticky="nsew", pady=1, padx=1)
    vozm2.load('Recursos/Grafico/giphy.gif')
    vozm2.config(width="350", height="150")
    #labelv=Label(frame7, text=rec)

def Newgif2():
    vozm3=ImageLabel(frame7)
    vozm3.grid(row=0, column=0, sticky="nsew", pady=1, padx=1)
    vozm3.load('Recursos/Grafico/plaguedoctor.gif')
    vozm3.config(width="350", height="150")


raiz=Tk()#creación de ventana
raiz.title("Sistema de recolección")
raiz.resizable(0,0)
raiz.iconbitmap("Recursos/Grafico/cheemspng.ico")
raiz.geometry("1280x700+1+1")
raiz.config(bg="black")
raiz.config(bd=1)#borde
#raiz.config(relief="flat")#borde
#raiz.config(cursor="heart")#cambiar forma del cursor

frame1=Frame()#se crea un frame
frame1.pack()#side="(rigth, bottom, etc)" anclado de frame por lado, anchor="(n,s,w,e)" coordenadas de anclado con cardinales, fill expansión en ejes (x,y,both,none), expand="true" para y, 
frame1.config(bg="#303030")
frame1.config(width="1280",height="720")
frame1.config(bd=1)#borde
#frame1.config(relief="flat")#borde
frame1.config(cursor="hand2")#cambiar forma del cursor

label1=Label(frame1, text="Sistema de recolección")
#label1.pack()#empaquetar, se acomoda de acuerdo al tamaño del label
label1.place(x=50, y=0)#posición del label
label1.config(fg="white")
label1.config(bg="#303030")
label1.config(font=("Downlink",40))

frameline=Frame(frame1)
frameline.place(x=50, y=60)
frameline.config(bg="white")
frameline.config(width="1180", height="10")

im1=PhotoImage(file="Recursos/Grafico/orderpick1.png")

label2=Label(frame1, image=im1)
label2.place(x=50, y=75)

# texttemp1=StringVar()
# texttemp1="Información del equipo, como miembros, \npróximos eventos, cosas importantes y frases cool. \nEs una de esas weas dinámicas cool que se mueven."

# label3=Label(frame1, text="Información del equipo, como miembros, \npróximos eventos, cosas importantes y frases cool. \nEs una de esas weas dinámicas cool que se mueven.")
# label3.place(x=50, y=305)
# label3.config(bg="#505050")
# label3.config(fg="white")
# label3.config(font=("Aller", 13))

frame2=Frame(frame1)
frame2.place(x=50, y=350)
frame2.config(width="230",height="44")
frame2.config(bg="#1896c6")

botoninventario=Button(frame2, text="Inventario de productos",command=inventario)
botoninventario.pack()
botoninventario.place(x=2, y=2)
#botoninventario.config(width="198",height="38")
botoninventario.config(bg="#404040")
botoninventario.config(fg="white")
botoninventario.config(font=("Aller", 14))

# frame3=Frame(frame1)
# frame3.place(x=50, y=450)
# frame3.config(width="350", height="250")
# frame3.config(bg="black")

# label4=Label(frame3, text="Listas de recolección \nen curso")
# label4.config(bg="black")
# label4.config(font=("Aller", 14), fg="white")
# label4.place(x=60, y=100)

#def frampro():
frameproyectos=Frame(frame1)
frameproyectos.place(x=495, y=75)
frameproyectos.config(width="343", height="483")
frameproyectos.config(bg="black")
	#---------------------------------------------DB

class Table(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.treeview= ttk.Treeview(self,height=22)
        self.treeview.grid(row=0, column=0, sticky="nsew")
        self.treeview.column("#0",minwidth=0,width=400)
        
        # Asociar el evento de expansión de un elemento con la
        # función correspondiente.
        self.treeview.tag_bind(
            "fstag", "<<TreeviewOpen>>", self.item_opened)
        
        # Este diccionario conecta los IDs de los ítems de Tk con
        # su correspondiente archivo o carpeta.
        self.fsobjects = {}
        
        self.file_image = tk.PhotoImage(file="Recursos/Grafico/montaico.png")
        self.folder_image = tk.PhotoImage(file="Recursos/Grafico/montacaric.png")
        
        # Cargar el directorio raíz.
        self.load_tree(abspath('D:/Descargas/Moni-か/DB'))
    
    def listdir(self, path):
        try:
            return listdir(path)
        except PermissionError:
            print("No tienes suficientes permisos para acceder a",
                  path)
            return []
    
    def get_icon(self, path):
        """
        Retorna la imagen correspondiente según se especifique
        un archivo o un directorio.
        """
        return self.folder_image if isdir(path) else self.file_image
    
    def insert_item(self, name, path, parent=""):
        """
        Añade un archivo o carpeta a la lista y retorna el identificador
        del ítem.
        """
        iid = self.treeview.insert(
            parent, tk.END, text=name, tags=("fstag",),
            image=self.get_icon(path))
        self.fsobjects[iid] = path
        return iid
    
    def load_tree(self, path, parent=""):
        """
        Carga el contenido del directorio especificado y lo añade
        a la lista como ítemes hijos del ítem "parent".
        """
        for fsobj in self.listdir(path):
            fullpath = join(path, fsobj)
            child = self.insert_item(fsobj, fullpath, parent)
            if isdir(fullpath):
                for sub_fsobj in self.listdir(fullpath):
                    self.insert_item(sub_fsobj, join(fullpath, sub_fsobj),
                                     child)
        
    def load_subitems(self, iid):
        """
        Cargar el contenido de todas las carpetas hijas del directorio
        que se corresponde con el ítem especificado.
        """
        for child_iid in self.treeview.get_children(iid):
            if isdir(self.fsobjects[child_iid]):
                self.load_tree(self.fsobjects[child_iid],
                               parent=child_iid)
    
    def item_opened(self, event):
        """
        Evento invocado cuando el contenido de una carpeta es abierto.
        """
        iid = self.treeview.selection()[0]
        self.load_subitems(iid)

	#-----------------------
def TabP():
	#proyectos_headers = (u"No.", u"progreso", u"Prioridad")
	proyectos_tab = Table(frameproyectos)
	proyectos_tab.place(x=0, y=0)

TabP()

labelp5=Label(frameproyectos, text="Listas introducidas al sistema", width=35)
labelp5.place(x=0, y=457)
labelp5.config(bg="#505050")
labelp5.config(font=("Aller", 13), fg="white", justify="left")

frame4=Frame(frame1)
frame4.place(x=498, y=580)
frame4.config(width="335",height="44")
frame4.config(bg="#1896c6")

botonnp=Button(frame4, text="Nueva lista", command=nuevlista)
botonnp.pack()
botonnp.place(x=2, y=2)
botonnp.config(bg="#404040")
botonnp.config(fg="white")
botonnp.config(width="29",height="1")
botonnp.config(font=("Aller", 14))

# frame5=Frame(frame1)
# frame5.place(x=680, y=650)
# frame5.config(width="177",height="44")
# frame5.config(bg="#1896c6")

# botonbp=Button(frame5, text="       Proyectos      ",command=proyecton)
# botonbp.pack()
# botonbp.place(x=2, y=2)
# botonbp.config(bg="#404040")
# botonbp.config(fg="white")
# botonbp.config(font=("Aller", 14))

frame6=Frame(frame1)
frame6.place(x=877, y=75)
frame6.config(width="350", height="200")
frame6.config(bg="#505050")


#Desde aquí-----------------------------------
class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs

    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

monikaim=ImageLabel(frame6)
monikaim.grid(row=0, column=0, sticky="nsew", pady=1, padx=1)
monikaim.load('Recursos/Grafico/inprogress.gif')
monikaim.config(width="350", height="150")
#Hasta acá, es para poner un gif-------------------------------

labelm=Label(frame6, text="Estatus de recolección actual")
labelm.grid(row=1, column=0, sticky="nsew", pady=1, padx=1)
labelm.config(bg="#505050")
labelm.config(font=("Aller", 12), fg="white", justify="left")


# frame8=Frame(frame1)
# frame8.place(x=877, y=500)
# frame8.config(width="350", height="200")
# frame8.config(bg="#303030")

# framel1=Frame(frame8)
# framel1.config(width="356", height="30")
# framel1.config(bg="#404040")
# framel1.grid(row=1, column=0, sticky="nsew")

# labellog=Label(framel1, text="Log:")
# labellog.place(x=0, y=0)
# labellog.config(bg="#404040")
# labellog.config(font=("Aller", 14), fg="white", justify="left")

# framel2=Frame(frame8)
# framel2.config(width="356", height="96")
# framel2.config(bg="#505050")
# framel2.grid(row=2, column=0, sticky="nsew")

# framel3=Frame(frame8)
# framel3.config(width="356", height="18")
# framel3.config(bg="#d0d0d0")
# framel3.grid(row=3, column=0, sticky="nsew")

#textventc=StringVar()
#textventc="Ventanita cool para escribir (Por si eres pobre o tu mic no sirve)"

# labell=Label(framel3, textvariable="Ingreso de listas de pedidos")
# labell.place(x=0, y=0)
# labell.config(bg="#d0d0d0", bd=0)
# labell.config(font=("Aller", 9), fg="white", justify="left")

frame9=Frame(frame1)
frame9.place(x=877, y=350)
frame9.config(width="345",height="44")
frame9.config(bg="#1896c6")

botonh=Button(frame9, text="Visualizar estado de order pickers", command=herramientas)
botonh.place(x=2, y=2)
botonh.config(width="30",height="1")
botonh.config(bg="#404040")
botonh.config(fg="white")
botonh.config(font=("Aller", 14), justify="center")


def dinamicgif():
	a=0
	b=0
	Newgif()

raiz.mainloop()
os.system("PAUSE")