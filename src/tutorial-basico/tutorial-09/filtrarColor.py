#!/usr/bin/env python

import numpy as np
import cv2
import imutils

#Se accede al video 
imagenOriginal = cv2.imread('./Imagenes/pelotaTenis_1.jpg')
cv2.imshow('Imagen Original', imagenOriginal)

#Luego se convierte la imagen al formato HSV
imagenHSV = cv2.cvtColor(imagenOriginal, cv2.COLlaunchOR_BGR2HSV)
cv2.imshow('Imagen HSV', imagenHSV)

#Se delimita el rango en donde estará el color de interés (H, S, V)
#La regla general es que el mínimo tendrá S y V más bajos que el máximo
amarilloMin = (30, 120, 50)
amarilloMax = (50, 255, 255)

#Se crea una mascara con el rango de color de interés
mascara = cv2.inRange(imagenHSV, amarilloMin, amarilloMax)
cv2.imshow('Mascara', mascara)




cv2.waitKey(0)
cv2.destroyAllWindows