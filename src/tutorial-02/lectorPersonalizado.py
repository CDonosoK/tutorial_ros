#!/usr/bin/env python

#Importamos la librería rospy
import rospy

#Importamos el mensaje personalizado
from tutorial_ros.msg import mensajeCustomizado

#Funcion que se ejecuta automaticamente cuando se recibe un mensaje
def chatter_callback(mensaje):
    print("El nodo lector lee: ")
    print("ID: ", mensaje.id)
    print("Nombre: ", mensaje.nombre)
    print("Ubicacion: ", mensaje.ubicacion)
    print("Temperatura: ", mensaje.temperatura)
    print("Humedad: ", mensaje.humedad)

def lector():
    
    #Se debe inicializar el nodo ROS
    nombreNodo = "lector"
    idUnico = True
    rospy.init_node(nombreNodo, anonymous = idUnico)

    #Se crea el objeto Publisher 
    nombreTopico = "tutorial02"
    tipoTopico = mensajeCustomizado #Definido en ROS

    rospy.Subscriber(nombreTopico, tipoTopico, chatter_callback)

    #Se debe indicar que se empiece a escuchar
    rospy.spin()

if __name__ == "__main__":
    lector()


