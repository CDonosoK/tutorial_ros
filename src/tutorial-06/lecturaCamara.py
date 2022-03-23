#!/usr/bin/env python
import numpy as np
import cv2

#video = cv2.VideoCapture(0) Para acceder a la WebCam
#Para acceder a un archivo de video
video = cv2.VideoCapture('./Videos/pelotaTenis.mp4')

while True:
    #Se obtienen los frames (imagen tras imagen)
    ret, frame = video.read()
    cv2.namedWindow("Video", cv2.WINDOW_AUTOSIZE)

    #Se cambia la imagen a escala de grises
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Se puede cambiar el tamaño de la imagen
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    cv2.imshow('Video', frame)

    #Se presiona la tecla ESC para salir y cada frame se demora 10 ms
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()