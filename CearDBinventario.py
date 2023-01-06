import sqlite3

conexion=sqlite3.connect("Lista.db")
cur = conexion.cursor()
try:
    conexion.execute("""create table Productos (
                              id integer primary key autoincrement,
                              nombre text,
                              cant integer
                        )""")
    print("se creo la tabla articulos")                        
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
Val="leche"
cur.execute("INSERT INTO Productos VALUES (Null,'Leche',9)")
conexion.commit()
conexion.close()