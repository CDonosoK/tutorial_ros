#!/usr/bin/env python

#Se importan las librerías necesarias
import numpy as np
import cv2

#Funcion que leerá la imagen y la devolverá en formato gris
def leerImagen(nombreImagen, esGris):
    if esGris:
        imagen = cv2.imread(nombreImagen, cv2.IMREAD_GRAYSCALE)
    else:
        imagen = cv2.imread(nombreImagen, cv2.IMREAD_COLOR)
    cv2.imshow("Imagen Original", imagen)
    return imagen

#Función para realizar el thersholding basico
def thresholdingBasico(imagenGris, valorThreshold):
    ret, imagenThreshold = cv2.threshold(imagenGris, valorThreshold, 255, cv2.THRESH_BINARY)
    cv2.imshow("Imagen Threshold Basico", imagenThreshold)

#Función para realizar el thersholding adaptado
def thresholdingAdaptado(imagenGris, valorThreshold):
    imagenGris = cv2.adaptiveThreshold(imagenGris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, valorThreshold, 2)
    cv2.imshow("Imagen Threshold Adaptado", imagenGris)


def main():
    nombreImagen = "./Imagenes/imagenThreshold.png"
    esGris = True
    valorThreshold = 115
    imagenGris = leerImagen(nombreImagen, esGris)
    thresholdingBasico(imagenGris, valorThreshold)
    thresholdingAdaptado(imagenGris, valorThreshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

    