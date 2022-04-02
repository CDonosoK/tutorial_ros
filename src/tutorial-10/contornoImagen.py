#!/usr/bin/env python

#Se importan las librerías necesarias
import numpy as np
import cv2

#Función que sirve para leer una imagen y mostrarla
def leerImagenRGB(nombreImagen, mostrar):
    imagen = cv2.imread(nombreImagen)
    if mostrar:
        cv2.imshow("Imagen RGB", imagen)
    return imagen

#Función que sirve para convertir una imagen a escala de grises y mostrarla
def convertirEscalaGrises(imagen, mostrar):
    imagenGrises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    if mostrar:
        cv2.imshow("Imagen Grises", imagenGrises)
    return imagenGrises

#Función que sirve para convertir una imagen a binaria y mostrarla
def convertirBinaria(imagen, mostrar, esAdaptativa):
    if esAdaptativa:
        imagenBinaria = cv2.adaptiveThreshold(
            imagen,                             #Imagen a procesar
            255,                                #Umbral máximo
            cv2.ADAPTIVE_THRESH_MEAN_C,         #Método de ajuste
            cv2.THRESH_BINARY,                  #Tipo de umbralización
            5,                                  #Tamaño de la región de ajuste
            20)                                 #Valor de cambio
    else:
        imagenBinaria = cv2.threshold(
            imagen,                             #Imagen a procesar
            0,                                  #Umbral mínimo
            255,                                #Umbral máximo
            cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    if mostrar:
        cv2.imshow("Imagen Binaria", imagenBinaria)
    return imagenBinaria

#Función que sirve para obtener los contornos de una imagen y mostrarla
def obtenerContornos(imagenOriginal, imagenBinaria, mostrar):
    contornos, jerarquia = cv2.findContours(
        imagenBinaria, 
        cv2.RETR_TREE, 
        cv2.CHAIN_APPROX_SIMPLE)

    if mostrar:
        cv2.drawContours(
            imagenOriginal,                 #Imagen a procesar
            contornos,                      #Contornos a dibujar
            -1,                             #Indica el contorno que se marcará (-1 para todos)
            (255, 0, 0),                    #Color del contorno
            1)                              #Grosor del contorno
        cv2.imshow("Imagen Contorno", imagenOriginal)
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
def procesarContornos(imagenOriginal, imagenBinaria, listaContornos, mostrar):
    imagenNegra = np.zeros(imagenOriginal.shape, np.uint8)

    for contorno in listaContornos:
        area = cv2.contourArea(contorno)
        if area > 100:
            ((x, y), radio) = cv2.minEnclosingCircle(contorno)
            cv2.drawContours(imagenNegra, [contorno], -1, (255, 255, 255), 1)
            cx, cy = obtenerCentroide(contorno)
            cv2.circle(imagenNegra, (int(cx), int(cy)), 2, (0, 255, 255), 2)
        
    if mostrar:
        cv2.imshow("Imagen Negra", imagenNegra)

def main():
    nombreImagen = "./Imagenes/herramientas.jpg"
    imagenRGB = leerImagenRGB(nombreImagen, True)
    imagenGrises = convertirEscalaGrises(imagenRGB, False)
    imagenBinaria = convertirBinaria(imagenGrises, False, False)

    contornos = obtenerContornos(imagenRGB, imagenBinaria, False)
    procesarContornos(imagenRGB, imagenBinaria, contornos, True)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

