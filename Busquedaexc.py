import openpyxl
import pandas as pd
from generador_rutas import rutas

def comparador():
	df = pd.read_excel('DB/Listaprueba1.xlsx', sheet_name='Hoja1', usecols="A:E")
	df2 = pd.read_excel('DB/Primerlista.xlsx', sheet_name='Sheet')

	df3=df2.merge(df[['Estante','Nivel','Columna','Cantidad','Producto']], how ='left', on ='Producto')

	print(df)
	print(df2)
	print(df3)

	df3.to_excel('DB/Listaff.xlsx')

	generador=df3.to_numpy().tolist()


	# generador=[]
	# for row in df3.iter_rows(min_row=1):
	#     productos = row[0].value
	#     generador.append(productos)
	rutas(generador)




