import numpy as np
import urllib.request
import cv2
from cv2 import aruco
from cameraCalibration import *

# DE CALIBRACION DE CAMERA IMPORTAR MATRIZ Y COEFICIENTE DE DISTORSION
calibracion = calibracion()
matrix,dist = calibracion.calibracion_cam()
print("Matriz de la camara: ",matrix)
print("Coeficiente de distorsion: ",dist)

# Tamaño de impresión del marcador
MARKER_SIZE = 2.3 # centimetros

# Inicializar los parametros del detector de aruco
parametros = aruco.DetectorParameters_create()

# Cargar el diccionario de aruco
diccionario = aruco.Dictionary_get(aruco.DICT_4X4_250)

# URL que envia arduino para abrir la camara
url="http://192.168.1.2/cam-high.jpg"

window1="DETECCION DE MARCADOR ARUCO"
cv2.namedWindow(window1,cv2.WINDOW_AUTOSIZE)

Estante=0
Nivel=1
Columna=2

zest=21.0
yest=-3.6
xest=7.4

while True:
    img_imp=urllib.request.urlopen(url)

    img_np=np.array(bytearray(img_imp.read()),dtype=np.uint8)

    frame=cv2.imdecode(img_np,-1)

    #frame=cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
    #img=cv2.flip(img,1)

    # Pasamos el frame a formato de color GRAY para leer arucos
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Uso de funcion para detectar marcadores
    esquinas, ids, excluir = aruco.detectMarkers(gray,diccionario,parameters=parametros)

    # Si detectamos esquinas entonces estimamos posicion
    if esquinas:
        rVec, tVec, _ = aruco.estimatePoseSingleMarkers(esquinas,MARKER_SIZE,matrix,dist)

        marcadores_totales = range(0,ids.size)
        tama=ids.size
        #print(tama)
        mdist=[]

        for marcador_ids, marcador_esquinas, i in zip(ids,esquinas,marcadores_totales):

            
            #Dibujar un cuadro alrededor del marcador resaltando su orientacion correcta
            aruco.drawDetectedMarkers(frame,esquinas)

            # Creando puntos en las 4 esquinas para situar texto correctamente
            marcador_esquinas = marcador_esquinas.reshape(4, 2)
            marcador_esquinas = marcador_esquinas.astype(int)
            top_right = marcador_esquinas[0].ravel()
            top_left = marcador_esquinas[1].ravel()
            bottom_right = marcador_esquinas[2].ravel()
            bottom_left = marcador_esquinas[3].ravel()
            
            # Estimacion de la distancia entre la camara y el aruco
            distancia = np.sqrt(
                tVec[i][0][2] ** 2 + tVec[i][0][0] ** 2 + tVec[i][0][1] ** 2
            )
            mdist.append(distancia)

            # Dibujar la posicion del marcador
            cv2.drawFrameAxes(frame, matrix, dist, rVec[i], tVec[i],4,4)

            # Texto del numero de identificador y la distancia
            cv2.putText(
                frame,
                f"id: {ids[i]} Dist: {round(distancia, 2)}",
                top_right,
                cv2.FONT_HERSHEY_PLAIN,
                1.3,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )

            # Texto de la posicion en x & y de la esquina derecha del marcador
            cv2.putText(
                frame,
                f"x:{round(tVec[i][0][0],1)} y:{round(tVec[i][0][1],1)} ",
                bottom_right,
                cv2.FONT_HERSHEY_PLAIN,
                1.0,
                (0, 0, 255),
                2,
                cv2.LINE_AA,
            )
        
        #for j in range(0,tama):
        print(ids)
        ard,ardi=np.where(ids==5)
        print(ard)
        tupv=[]
        if 5 not in ids:
            print('no se encontro aruco')
        else:
            aaa=int(ard)
            print(aaa)
            print(tVec[aaa][0][0])
            print(tVec[aaa][0][1])
            print(mdist[aaa])
        
# """            x=print(round(tVec[0][0][0],1))
 #           Y=print(round(tVec[0][0][1],1))
  #          distac=print(np.sqrt(
   #         tVec[0][0][2] ** 2 + tVec[0][0][0] ** 2 + tVec[0][0][1] ** 2)) """
    
    # Mostramos la ventana para visualizar lo que ve la camara
    cv2.imshow(window1,frame)

    k=cv2.waitKey(1)

    if k==27: # 'ESCAPE'
        break

cv2.destroyAllWindows()