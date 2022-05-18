#!/usr/bin/env python

#Se importan las librerías necesarias
import numpy as np
import cv2

#Muchas de las siguientes función son a partir de los tutoriales anteriores
def leerImagenRGB(nombreImagen, mostrar):
    imagen = cv2.imread(nombreImagen)
    if mostrar:
        cv2.imshow("Imagen RGB", imagen)
    return imagen

#La siguiente función es para filtrar una imagen por un rango de valores
def filtrarColor(imagenRGB, valorMin, valorMax, mostrar):
    imagenHSV = cv2.cvtColor(imagenRGB, cv2.COLOR_BGR2HSV)
    if mostrar:
        cv2.imshow("Imagen HSV", imagenHSV)

    #La función cv2.inRange va a retornar la imagen Binaria
    filtro = cv2.inRange(imagenHSV, valorMin, valorMax)
    return filtro

#Función para obtener los contornos de una imagen y mostrarla
def obtenerContornos(imagenBinaria, mostrar):
    contornos, jerarquia = cv2.findContours(
        imagenBinaria, 
        cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE)

    if mostrar:
        cv2.drawContours(
            imagenBinaria,                 #Imagen a procesar
            contornos,                      #Contornos a dibujar
            -1,                             #Indica el contorno que se marcará (-1 para todos)
            (255, 0, 0),                    #Color del contorno
            1)                              #Grosor del contorno
        cv2.imshow("Imagen Contorno", imagenBinaria)
    return contornos

#Función para obtener el centroide de un contorno
def obtenerCentroide(contorno):
    M = cv2.moments(contorno)
    cx = -1
    cy = -1
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
    return cx, cy

#Función que sirve para procesar los contornos y mostrarlos
def dibujarContornos(imagenOriginal, imagenBinaria, listaContornos, mostrar):
    imagenNegra = np.zeros(imagenOriginal.shape, np.uint8)

    for contorno in listaContornos:
        area = cv2.contourArea(contorno)
        if area > 5000:
            ((x, y), radio) = cv2.minEnclosingCircle(contorno)
            cv2.drawContours(imagenNegra, [contorno], -1, (255, 255, 255), 1)
            cv2.drawContours(imagenOriginal, [contorno], -1, (0, 255, 0), 1)
            cx, cy = obtenerCentroide(contorno)
            cv2.circle(imagenNegra, (int(cx), int(cy)), int(radio), (0, 255, 255), 2)
            cv2.circle(imagenOriginal, (int(cx), int(cy)), int(radio), (0, 255, 255), 2)
        
    if mostrar:
        #cv2.imshow("Imagen Negra", imagenNegra)
        cv2.imshow("Imagen Original", imagenOriginal)

def main():
    #Se lee el video
    video = cv2.VideoCapture("./Videos/pelotaTenis_1.mp4")
    #video.open('http://192.168.0.22:8080') #Para acceder a la WebCam vía WiFi

    while True:
        #Se obtienen los frames (imagen tras imagen) y se achican
        ret, frame = video.read()
        #frame = cv2.resize(frame, (0,0), fx=1, fy=1)

        amarilloMin = (30, 100, 20)
        amarilloMax = (60, 240, 255)

        frameBinario = filtrarColor(frame, amarilloMin, amarilloMax, False)
        listaContornos = obtenerContornos(frameBinario, False)
        dibujarContornos(frame, frameBinario, listaContornos, True)

        #Se presiona la tecla ESC para salir y cada frame se demora 10 ms
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()