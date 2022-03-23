#!/usr/bin/env python
import numpy as np
import cv2

#Se crea una imagen en blanco de tamaño 512x512
imagenBlanca = np.zeros((512,512,3), np.uint8)

#Se crea una linea (posInicial, posFinal, color, grosor) 
cv2.line(imagenBlanca, (35,35), (512-35,35), (255,0,0), 5)
cv2.namedWindow("Dibujos", cv2.WINDOW_NORMAL)
cv2.imshow("Dibujos", imagenBlanca)
cv2.waitKey(0)

#Se crea un rectangulo (posInicial, posFinal, color, grosor)
cv2.rectangle(imagenBlanca, (50,50), (512-50,512-50), (0,255,0), 5)
cv2.namedWindow("Dibujos", cv2.WINDOW_NORMAL)
cv2.imshow("Dibujos", imagenBlanca)
cv2.waitKey(0)

#Se crea un circulo (posInicial, radio, color, grosor)
cv2.circle(imagenBlanca, (256,256), 180, (0,0,255), 5)
cv2.namedWindow("Dibujos", cv2.WINDOW_NORMAL)
cv2.imshow("Dibujos", imagenBlanca)
cv2.waitKey(0)

#Se crea una elipse (posInicial, radioMayor, radioMenor, color, grosor)
cv2.ellipse(imagenBlanca, (256,256), (180,100), 0, 0, 360, (255,0,255), 5)
cv2.namedWindow("Dibujos", cv2.WINDOW_NORMAL)
cv2.imshow("Dibujos", imagenBlanca)
cv2.waitKey(0)

#Se ingresa un texto en la imagen (posInicial, texto, fuente, tamaño, color, grosor)
cv2.putText(imagenBlanca, "ROS - OpenCV", (140,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 2)
cv2.namedWindow("Dibujos", cv2.WINDOW_NORMAL)
cv2.imshow("Dibujos", imagenBlanca)
cv2.waitKey(0)
cv2.destroyAllWindows()