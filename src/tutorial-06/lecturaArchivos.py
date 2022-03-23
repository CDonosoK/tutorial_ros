#!/usr/bin/env python

import numpy as np
import cv2

#Se lee la imagen que está en la carpeta Imagenes
#El segundo valor indica el tipo de imagen que se va a leer
nombreImagen = "OpenCV_Logo"
imagen = cv2.imread("./Imagenes/"+nombreImagen+".png", cv2.IMREAD_COLOR)

#Se crea la ventana
cv2.namedWindow("Mi primera Ventana", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Mi primera Ventana", imagen)

#Para que la ventana no se cierre automáticamente
#Debemos apretar la tecla 0 para continuar.
cv2.waitKey(0)

#Se guarda una imagen copiada en la carpeta Imagenes
cv2.imwrite("./Imagenes/"+nombreImagen+"_copia.png", imagen)

#Si queremos saber la forma de la imagen se puede realizar 
#donde se entrega una tupla con el número de filas (alto), columnas (ancho) y canales
print(imagen.shape)

#Si se desea saber el tamaño (píxeles) de la imagen se puede realizar 
#Multiplicación del alto por el ancho
print(imagen.size)

#Si se desea acceder a un pixel en específico se puede realizar
#Por ejemplo se accederá al pixel en la fila 10 y columna 3
print(imagen[10][3])

#Si se desea acceder a un canal en específico se puede realizar
#Por ejemplo se accederá al canal 0
print(imagen[:, :, 0])

