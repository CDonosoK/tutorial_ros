#!/usr/bin/env python

#Importamos los archivos necesarios para cargar y crear el servicio
from tutorial_ros.srv import servicioPersonalizado, servicioPersonalizadoResponse, servicioPersonalizadoRequest

#Se importan las librerías necesarias
import rospy

def clientePersonalizado(valor1, valor2):
    
    #Nombre del servicio que se utilizará
    nombreServicio = "servicioPersonalizado"

    #Se espera a que el servicio esté activado
    rospy.wait_for_service(nombreServicio)

    try:
        #Se realiza la petición al servicio
        tipoServicio = servicioPersonalizado
        servicio = rospy.ServiceProxy(nombreServicio, tipoServicio)
        respuesta = servicio(valor1, valor2)
        return respuesta.resultado

    except rospy.ROSInterruptException:
        rospy.loginfo("Se interrumpió la ejecución del programa")

if __name__ == '__main__':
    valor1 = input("Ingrese el primer valor: ")
    valor2 = input("Ingrese el segundo valor: ")

    print(clientePersonalizado(int(valor1), int(valor2)))