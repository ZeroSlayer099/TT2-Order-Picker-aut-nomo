#!/usr/bin/env python
# -*- coding: utf-8 -*-


import socket


def client_program():
    host = "192.168.1.3"#socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    
    while True:
        f = open("coordenadas.db", "rb")
        content = f.read(1024)
        
        while content:
            # Enviar contenido.
            client_socket.send(content)
            content = f.read(1024)
        
        break
    
    # Se utiliza el caracter de código 1 para indicar
    # al cliente que ya se ha enviado todo el contenido.
    try:
        client_socket.send(chr(1))
    except TypeError:
        # Compatibilidad con Python 3.
        client_socket.send(bytes(chr(1), "utf-8"))
    
    # Cerrar conexión y archivo.
    client_socket.close()
    f.close()
    print("El archivo ha sido enviado correctamente.")


if __name__ == "__main__":
    client_program()