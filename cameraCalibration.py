import numpy as np
import cv2
import glob

class calibracion():
    def __init__(self):
        self.tablero = (9,6)
        self.tam_frame = (800,600)

        #Criterio
        self.criterio = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,30,0.001)

        #Preparacion de los puntos del tablero
        self.puntos_obj = np.zeros((self.tablero[0]*self.tablero[1],3),np.float32)
        self.puntos_obj[:,:2] = np.mgrid[0:self.tablero[0],0:self.tablero[1]].T.reshape(-1,2)

        #Guardar los puntos en 3D y los puntos de imagen 2D
        self.puntos_3d = []
        self.puntos_img = []

    def calibracion_cam(self):
        fotos = glob.glob('calib[0-5].png')
        for foto in fotos:
            #print(foto)
            img = cv2.imread(foto)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            # Buscar las esquinas del tablero
            ret,esquinas = cv2.findChessboardCorners(gray,self.tablero,None)
            
            if ret == True:
                self.puntos_3d.append(self.puntos_obj)
                esquinas2 = cv2.cornerSubPix(gray,esquinas,(11,11),(-1,-1),self.criterio)
                self.puntos_img.append(esquinas)
                #cv2.drawChessboardCorners(img,self.tablero,esquinas2,ret)
                #cv2.imshow("img",img)

        # Calibracion de la camara
        ret,cameraMatrix,dist,rvecs,tvecs = cv2.calibrateCamera(self.puntos_3d,self.puntos_img,
                                            self.tam_frame,None,None)

        return cameraMatrix,dist


    
