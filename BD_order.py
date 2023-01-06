import openpyxl
import pandas as pd
import sqlite3
from client import client_program


def finalbd():

	df = pd.read_excel("DB/ListaOrder.xlsx",sheet_name='Sheet', usecols="C:E") #en tu caso es un excel
	coordenadas=df.to_numpy().tolist()
	dfcoor = pd.DataFrame(coordenadas)
	print(dfcoor)
	conn=sqlite3.connect("coordenadas.db")
	# try:
	#     conexion.execute("""create table articulos (
	#                               Estante text,
	#                               Nivel text,
	#                               Columna text
	#                         )""")
	#     print("se creo la tabla articulos")                        
	# except sqlite3.OperationalError:
	# 	print("La tabla articulos ya existe")
	table_name='articulos'
	query = f'Create table if not Exists {table_name} (Estante text, Nivel text, Columna text)'
	conn.execute(query)
	dfcoor.to_sql(table_name,conn,if_exists='replace',index=False)
	conn.commit()
	conn.close()
	client_program()

#finalbd()