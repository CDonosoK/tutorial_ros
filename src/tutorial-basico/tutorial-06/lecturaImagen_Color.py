#!/usr/bin/env python

import numpy as np
import cv2

#Se lee la imagen que está en la carpeta Imagenes
#El segundo valor indica el tipo de imagen que se va a leer
nombreImagen = "imagenColor"
imagenColor = cv2.imread("./Imagenes/"+nombreImagen+".jpg", cv2.IMREAD_COLOR)

#Se crea la ventana
cv2.namedWindow("Mi primera Ventana", cv2.WINDOW_NORMAL)
cv2.imshow("Mi primera Ventana", imagenColor)

#Se obtienen las dimensiones de la imagen
alto, ancho, canales = imagenColor.shape

#Se decodifica la imagen en el canal RGB y se juntan en una imagen
azul, verde, rojo = cv2.split(imagenColor)
nuevaImagenRGB = np.concatenate((azul, verde, rojo), axis=1)

#Se muestra la imagen
cv2.namedWindow("Codificacion RGB", cv2.WINDOW_NORMAL)
cv2.imshow("Codificacion RGB", nuevaImagenRGB)


cv2.waitKey(0)
cv2.destroyAllWindows()

#Ahora decodificamos la imagen en la codificación HSV
imagenHSV = cv2.cvtColor(imagenColor, cv2.COLOR_BGR2HSV)

#Se obtienen los canales H,S,V y se juntan en una imagen
H, S, V = cv2.split(imagenHSV)
nuevaImagenHSV = np.concatenate((H, S, V), axis=1)

#Se muestra la imagen
cv2.namedWindow("Codificacion HSV", cv2.WINDOW_NORMAL)
cv2.imshow("Codificacion HSV", nuevaImagenHSV)

cv2.waitKey(0)
cv2.destroyAllWindows()

#También se puede transformar una imagen a color a una escala de grises
imagenByN = cv2.cvtColor(imagenColor, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Escala de Grises", cv2.WINDOW_NORMAL)
cv2.imshow("Escala de Grises", imagenByN)

cv2.waitKey(0)
cv2.destroyAllWindows()