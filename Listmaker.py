import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from Test import AddItem
#from Test import PryName

conn = sqlite3.connect('DB/Database.db')
c = conn.cursor()

class Table(tk.Frame):
    def __init__(self, parent=None, title="", headers=[], height=10, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._title = tk.Label(self, text=title, background="#1B1B1B", font=("Downlink", 18,),fg="white")
        self._headers = headers
        self._tree = ttk.Treeview(self,
                                  height=height,
                                  columns=self._headers, 
                                  show="headings")
        self._title.pack(side=tk.TOP, fill="x")

        
        # Agregamos dos scrollbars 
        vsb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self._tree.xview)
        hsb.pack(side='bottom', fill='x')

        self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._tree.pack(side="left")

        for header in self._headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=True,
                              width=tkFont.Font().measure(header.title()))

    def add_row(self, row):
        self._tree.insert('', 'end', values=row)
        for i, item in enumerate(row):
            col_width = tkFont.Font().measure(item)
            if self._tree.column(self._headers[i], width=None) < col_width:
                    self._tree.column(self._headers[i], width=col_width)

def ListGenPRY():

    raiz=Tk()
    raiz.title("Moni-カ")
    raiz.iconbitmap("Recursos/Grafico/Monika2.ico")
    raiz.title("Generador de lisstas")
    raiz.geometry('200x350')
    raiz.configure(bg="#2C2C2E")
    raiz.focus_set()
    raiz.grab_set()
    headers = (u"ID",   u"Nombre")
    inventario_tab = Table(raiz, title="Lista", headers=headers)
    inventario_tab.pack()
    c.execute("SELECT id,Nombre FROM Proyectos")

    for row in c:
        inventario_tab.add_row(row)
    
    frame=Frame(raiz)
    frame.config(bg="#202020")
    frame.pack(side=tk.TOP,fill="x")
    #frame.place(x=0, y=25)
    frame.config(width="1180", height="290")
    frame.config(cursor="hand2")

    label=Label(frame,text="Numero:")
    label.pack(side=tk.LEFT)
    label.config(fg="white")
    label.config(bg="#202020")
    label.config(font=("SourceSansPro-Regular",14), justify="left")

    label1=Entry(frame)
    label1.insert(END,"0")
    label1.pack(side=tk.LEFT)
    label1.config(fg="black")
    label1.config(bg="white")
    label1.config(font=("SourceSansPro-Light",12))
    label1.focus_set()

    def Read():
        global ID
        ID=int(label1.get())
    def Trigger():
        Read()
        pry=[]
        c.execute("SELECT Nombre From Proyectos")
        for namae in c:
            namae[0]
            pry.append(namae[0])
        name=pry[ID-1]
        titulovent="Moni-カ Proyecto: "+name
        raiz2=Tk()
        raiz2.title(titulovent)
        raiz2.resizable(0,0)
        raiz2.iconbitmap("Recursos/Grafico/Monika2.ico")
        raiz2.geometry("1280x720+10+10")
        raiz2.config(bg="black")
        raiz2.config(bd=1)
        raiz2.config(cursor="heart")
        raiz2.focus_set()

        subframe=Frame(raiz2)
        subframe.config(bg="#202020")
        subframe.pack(side=tk.TOP,fill="x")
        #subframe.place(x=0, y=25)
        subframe.config(width="1180", height="290")
        subframe.config(cursor="hand2")


    boton=Button(raiz,text="OK",command=Trigger)
    boton.pack(side=tk.TOP,fill="x")
    #boton.config(width="13",height="1")
    boton.config(bg="#404040")
    boton.config(fg="white")
    boton.config(font=("SourceSansPro-Regular", 14), justify="center")

    raiz.mainloop()

ListGenPRY()