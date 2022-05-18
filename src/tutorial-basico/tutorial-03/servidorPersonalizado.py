#!/usr/bin/env python

#Importamos los archivos necesarios para cargar y crear el servicio
from tutorial_ros.srv import servicioPersonalizado, servicioPersonalizadoResponse, servicioPersonalizadoRequest

#Se importa la librería rospy
import rospy


#Función que ejecuta el servidor automáticamente al recibir una petición 
def handle_servicio_personalizado(req):

    print ("Recibido la petición")
    print("Valor 1: {} y Valor 2: {}".format(req.valor1, req.valor2))
    print("Suma de ambos valores: "+str(req.valor1 + req.valor2))
    return servicioPersonalizadoResponse(req.valor1 + req.valor2)


def serverPersonalizado():
    
    #Se crea el servicio
    nombreNodo = "servidorPersonalizado"
    rospy.init_node(nombreNodo)

    #Se crea el servicio y se ejecuta
    nombreServicio = "servicioPersonalizado"
    tipoServicio = servicioPersonalizado
    servicio = rospy.Service(nombreServicio, tipoServicio, handle_servicio_personalizado)
    rospy.spin()

if __name__ == '__main__':
    serverPersonalizado()
