#!/usr/bin/env python

import numpy as np
import cv2

#Se lee la imagen que está en la carpeta Imagenes
nombreImagen = "OpenCV_Logo"
imagen = cv2.imread("./Imagenes/"+nombreImagen+".png")

#Se crea la ventana
cv2.namedWindow("Mi primera Ventana", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Mi primera Ventana", imagen)

#Para que la ventana no se cierre automáticamente
#Debemos apretar la tecla 0 para continuar.
cv2.waitKey(0)

#Se guarda una imagen copiada en la carpeta Imagenes
cv2.imwrite("./Imagenes/"+nombreImagen+"_copia.png", imagen)


