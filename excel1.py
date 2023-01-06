import openpyxl
from Busquedaexc import comparador

def excel_lista(listapro):
    excel_document = openpyxl.Workbook() #crear un archivo
    #excel_document2 = openpyxl.load_workbook('DB/Primerlista.xlsx') #abrir documento
    sheet=excel_document.active
    #sheet2=excel_document2.active

    #sheet.append(('Estante', 'Nivel', 'Columna', 'producto','Cantidad'))
    sheet.append(('Producto', 'Cantidad'))
    productos = listapro

    for producto in productos:
        sheet.append(producto)

    # sheet["A6"] = 10

    # sheet2["D2"]= "Leche"

    excel_document.save("DB/Primerlista.xlsx")

    comparador()

    #excel_document2.save("DB/Listaprueba1.xlsx")