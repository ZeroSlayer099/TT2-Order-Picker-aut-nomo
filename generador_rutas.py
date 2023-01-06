from operator import itemgetter, attrgetter
import openpyxl
import pandas as pd
from BD_order import finalbd

def rutas(listaprod):

    Lista_pedidos = listaprod

    lista_final=sorted(Lista_pedidos, key=itemgetter(2,3,4))
    #print(lista_final)

    def multisort(xs, specs):
         for key, reverse in reversed(specs):
             xs.sort(key=itemgetter(key), reverse=reverse)
         return xs

    print(multisort(list(lista_final), ((2, False), (3, False),(4,False))))
    listaordenada=multisort(list(lista_final), ((2, False), (3, False),(4,False)))
    excel_ordenado = openpyxl.Workbook() #crear un archivo
    #excel_document2 = openpyxl.load_workbook('DB/Primerlista.xlsx') #abrir documento
    sheet=excel_ordenado.active
    sheet.append(('Producto', 'Cantidad','Estante','Nivel','Columna', 'Total producto'))
    productos = listaordenada

    for producto in productos:
        sheet.append(producto)

    excel_ordenado.save("DB/ListaOrder.xlsx")

    finalbd()



# def multisort(xs, specs):
# 	for key, reverse in reversed(specs):
# 		lfff=sorted(list(xs),key=itemgetter(key), reverse=reverse)
# 		print(lfff)
# 	return xs
	
# multisort(list(Lista_pedidos), ((2, True), (0, False)))