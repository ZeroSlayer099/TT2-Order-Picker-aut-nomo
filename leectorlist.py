import pandas as pd
import sqlite3
#from client import client_program


def readbd():


	conn=sqlite3.connect("coordenadasO.db")
	r_df = pd.read_sql("select * from articulos",conn)
	print(r_df)
	coord=r_df.to_numpy().tolist()
	# dfcoor = pd.DataFrame(coordenadas)
	print(coord)
	fila=coord[1]
	print(fila)
	estante=fila[0]
	print(estante)
	nivel=fila[1]
	print(nivel)
	columna=fila[2]
	print(columna)

readbd()