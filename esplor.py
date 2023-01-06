from tkinter import *
import tkinter as tk
from tkinter import ttk
from os import listdir, sep
from os.path import isdir, join, abspath

raiz=Tk()#creación de ventana
raiz.title("Sistema de recolección")
raiz.resizable(0,0)
raiz.iconbitmap("Recursos/Grafico/cheemspng.ico")
raiz.geometry("1280x720+5+5")
raiz.config(bg="black")
raiz.config(bd=1)#borde

#raiz.config(relief="flat")#borde
#raiz.config(cursor="heart")#cambiar forma del cursor

# frame1=Frame()#se crea un frame
# frame1.pack()#side="(rigth, bottom, etc)" anclado de frame por lado, anchor="(n,s,w,e)" coordenadas de anclado con cardinales, fill expansión en ejes (x,y,both,none), expand="true" para y, 
# frame1.config(bg="#303030")
# frame1.config(width="1280",height="720")
# frame1.config(bd=1)#borde
# #frame1.config(relief="flat")#borde
# frame1.config(cursor="hand2")#cambiar forma del cursor

# label1=Label(frame1, text="Sistema de recolección")
# #label1.pack()#empaquetar, se acomoda de acuerdo al tamaño del label
# label1.place(x=50, y=0)#posición del label
# label1.config(fg="white")
# label1.config(bg="#303030")
# label1.config(font=("Downlink",40))

# frameline=Frame(frame1)
# frameline.place(x=50, y=60)
# frameline.config(bg="white")
# frameline.config(width="1180", height="10")


class Application(tk.Frame):
    
    def __init__(self, main_window):
        main_window.geometry("720x480")
        super().__init__(main_window)
        #main_window.title("Explorador de archivos y carpetas")

        frame1=Frame()#se crea un frame
        frame1.pack()#side="(rigth, bottom, etc)" anclado de frame por lado, anchor="(n,s,w,e)" coordenadas de anclado con cardinales, fill expansión en ejes (x,y,both,none), expand="true" para y, 
        frame1.config(bg="#303030")
        frame1.config(width="1280",height="720")
        frame1.config(bd=1)#borde
        #frame1.config(relief="flat")#borde
        frame1.config(cursor="hand2")#cambiar forma del cursor

        label1=Label(frame1, text="Sistema de recolección")
        #label1.pack()#empaquetar, se acomoda de acuerdo al tamaño del label
        label1.grid(row=0, column=0, sticky="nsew")#posición del label
        label1.config(fg="white")
        label1.config(bg="#303030")
        label1.config(font=("Downlink",40))

        frameline=Frame(frame1)
        frameline.grid(row=1, column=0, sticky="nsew")
        frameline.config(bg="white")
        frameline.config(width="1180", height="10")

        self.treeview = ttk.Treeview(frame1)
        self.treeview.grid(row=2, column=0, sticky="nsew")
        
        # Asociar el evento de expansión de un elemento con la
        # función correspondiente.
        self.treeview.tag_bind(
            "fstag", "<<TreeviewOpen>>", self.item_opened)
        
        # Expandir automáticamente.
        # for w in (self, main_window):
        #     w.rowconfigure(0, weight=1)
        #     w.columnconfigure(0, weight=1)
        
        # self.grid(row=2, column=0, sticky="nsew")
        
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

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()