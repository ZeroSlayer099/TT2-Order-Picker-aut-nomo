import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import pandas as pd
from Test import AddItem


# class Table(tk.Frame):
#     def __init__(self, parent=None, title="", headers=[], height=20, *args, **kwargs):
#         tk.Frame.__init__(self, parent, *args, **kwargs)
#         self._title = tk.Label(self, text=title, background="#1B1B1B", font=("Downlink", 18,),fg="white")
#         self._headers = headers
#         self._tree = ttk.Treeview(self,
#                                   height=height,
#                                   columns=self._headers, 
#                                   show="headings")
#         self._title.pack(side=tk.TOP, fill="x")

        
#         # Agregamos dos scrollbars 
#         vsb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
#         vsb.pack(side='right', fill='y')
#         hsb = ttk.Scrollbar(self, orient="horizontal", command=self._tree.xview)
#         hsb.pack(side='bottom', fill='x')

#         self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
#         self._tree.pack(side="left")

#         for header in self._headers:
#             self._tree.heading(header, text=header.title())
#             self._tree.column(header, stretch=True,
#                               width=tkFont.Font().measure(header.title()))

#     def add_row(self, row):
#         self._tree.insert('', 'end', values=row)
#         for i, item in enumerate(row):
#             col_width = tkFont.Font().measure(item)
#             if self._tree.column(self._headers[i], width=None) < col_width:
#                     self._tree.column(self._headers[i], width=col_width)

def reporte():

    df = pd.read_excel('DB/Listaprueba1.xlsx', sheet_name='Hoja1', usecols="A:F")

    raiz=Tk()#creación de ventana
    raiz.title("Sistema de recolección")
    raiz.iconbitmap("Recursos/Grafico/cheemspng.ico")
    #raiz=tk.Toplevel(None,bg="#2C2C2E")
    raiz.title("Inventario")
    raiz.geometry('1250x500')
    raiz.configure(bg="#2C2C2E")
    raiz.focus_set()
    raiz.grab_set()
    headers = (u"Estante",   u"Nivel", u"Columna",
                        u"Producto", u"Cantidad", u"Nombre"
                        )
    # inventario_tab = Table(raiz, title="Inventario", headers=headers)
    # inventario_tab.pack(pady=10, padx=10)

    listinventario=df.to_numpy().tolist()
    print(listinventario)

    frame1=Frame(raiz)
    frame1.place(x=0, y=0)
    frame1.config(bg="#303030")
    frame1.config(width="1250",height="500")
    frame1.config(bd=1)
    frame1.config(cursor="arrow")

    treeview = ttk.Treeview(frame1, height=20, columns=('#1','#2','#3','#4','#5','#6'))
    treeview.grid(row=0, column=0, sticky="nsew", pady=5, padx=5)
    treeview['show'] = 'headings'
    #treeview.bind("<Double-Button-1>", doubleClickTabla)
    treeview.heading("#1", text="Estante", anchor=CENTER)
    treeview.heading("#2", text="Nivel", anchor=CENTER)
    treeview.heading("#3", text="Columna", anchor=CENTER)
    treeview.heading("#4", text="Producto", anchor=CENTER)
    treeview.heading("#5", text="Cantidad", anchor=CENTER)
    treeview.heading("#6", text="Nombre", anchor=CENTER)

    vsb = ttk.Scrollbar(frame1, orient="vertical", command=treeview.yview)
    vsb.grid(row=0, column=1, sticky="nsw", pady=5, padx=5)
    hsb = ttk.Scrollbar(frame1, orient="horizontal", command=treeview.xview)
    hsb.grid(row=1, column=0, sticky="new", pady=5, padx=5)

    treeview.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

    p=0

    for item in listinventario:
        prod = treeview.insert("",'end', values=listinventario[p] )
        p=p+1


    # c.execute("SELECT Item,Unidades,Descripción,Ubicación,Disponibilidad FROM Inventario")


    # for row in inventario_tab:
    #     inventario_tab.add_row(row)

    # subtitle= tk.Label(text="Añadir a inventario:", background="#1B1B1B", font=("Downlink", 16,),fg="white")
    # subtitle.pack(side=tk.TOP,fill="x")
    
    # frame=Frame(raiz)
    # frame.config(bg="#202020")
    # frame.pack(side=tk.TOP,fill="x")
    # #frame.place(x=0, y=25)
    # frame.config(width="1180", height="290")
    # frame.config(cursor="hand2")

    # label=Label(frame,text="Nombre del item:")
    # label.pack(side=tk.LEFT)
    # label.config(fg="white")
    # label.config(bg="#202020")
    # label.config(font=("SourceSansPro-Regular",14), justify="left")

    # label1=Entry(frame)
    # label1.insert(END,"Nombre del item")
    # label1.pack(side=tk.LEFT,fill="x")
    # label1.config(fg="black")
    # label1.config(bg="white")
    # label1.config(font=("SourceSansPro-Light",12))
    # label1.focus_set()
    
    # label2=Label(frame,text="Unidades:")
    # label2.pack(side=tk.LEFT)
    # label2.config(fg="white")
    # label2.config(bg="#202020")
    # label2.config(font=("SourceSansPro-Regular",14), justify="left")

    # label3=Entry(frame)
    # label3.insert(END,"Unidades")
    # label3.pack(side=tk.LEFT,fill="x")
    # label3.config(fg="black")
    # label3.config(bg="white")
    # label3.config(font=("SourceSansPro-Light",12))
    # label3.focus_set()

    # frame2=Frame(raiz)
    # frame2.config(bg="#202020")
    # frame2.pack(side=tk.TOP,fill="x")
    # #frame.place(x=0, y=25)
    # frame2.config(width="1180", height="290")
    # frame2.config(cursor="hand2")

    # label4=Label(frame2,text="Descripción:")
    # label4.pack(side=tk.LEFT)
    # label4.config(fg="white")
    # label4.config(bg="#202020")
    # label4.config(font=("SourceSansPro-Regular",14), justify="left")

    # label5=Entry(frame2)
    # label5.insert(END,"Inserte Descripción")
    # label5.pack(side=tk.TOP,fill="x")
    # label5.config(fg="black")
    # label5.config(bg="white")
    # label5.config(font=("SourceSansPro-Light",12))
    # label5.focus_set()

    # frame3=Frame(raiz)
    # frame3.config(bg="#202020")
    # frame3.pack(side=tk.TOP,fill="x")
    # #frame.place(x=0, y=25)
    # frame3.config(width="1180", height="290")
    # frame3.config(cursor="hand2")

    # label6=Label(frame3,text="Ubicación:")
    # label6.pack(side=tk.LEFT)
    # label6.config(fg="white")
    # label6.config(bg="#202020")
    # label6.config(font=("SourceSansPro-Regular",14), justify="left")

    # label7=Entry(frame3)
    # label7.insert(END,"Lugar en el que está")
    # label7.pack(side=tk.LEFT,fill="x")
    # label7.config(fg="black")
    # label7.config(bg="white")
    # label7.config(font=("SourceSansPro-Light",12))
    # label7.focus_set()

    # label8=Label(frame3,text="Disponibilidad:")
    # label8.pack(side=tk.LEFT)
    # label8.config(fg="white")
    # label8.config(bg="#202020")
    # label8.config(font=("SourceSansPro-Regular",14), justify="left")

    # label9=Entry(frame3)
    # label9.insert(END,"Si/No")
    # label9.pack(side=tk.LEFT,fill="x")
    # label9.config(fg="black")
    # label9.config(bg="white")
    # label9.config(font=("SourceSansPro-Light",12))
    # label9.focus_set()

    # def Read():
    #     global Item
    #     global Unidades 
    #     global Descrip
    #     global Location
    #     global Disponibilidad
    #     Item=label1.get()
    #     Unidades=label3.get()
    #     Descrip=label5.get()
    #     Location=label7.get()
    #     Disponibilidad=label9.get()

    # def Close():
    #     raiz.destroy()
    #     reporte()

    
    # def Trigger():
    #     Read()
    #     AddItem(Item,Unidades,Descrip,Location,Disponibilidad)
    #     Close()

    # boton=Button(raiz,text="Añadir",command=Trigger)
    # boton.pack(side=tk.TOP,fill="x")
    # #boton.config(width="13",height="1")
    # boton.config(bg="#404040")
    # boton.config(fg="white")
    # boton.config(font=("SourceSansPro-Regular", 14), justify="center")

    raiz.mainloop()

#reporte()