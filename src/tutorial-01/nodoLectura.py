#!/usr/bin/env python

#Importamos la librería rospy
import rospy

#Importamos la libreria que se va a utilizar
from std_msgs.msg import String

#Funcion que se ejecuta automaticamente cuando se recibe un mensaje
def chatter_callback(mensaje):
    print("El nodo lector lee: ", mensaje.data)

def lector():
    
    #Se debe inicializar el nodo ROS
    nombreNodo = "lector"
    idUnico = True
    rospy.init_node(nombreNodo, anonymous = idUnico)

    #Se crea el objeto Publisher 
    nombreTopico = "tutorial01"
    tipoTopico = String #Definido en ROS

    rospy.Subscriber(nombreTopico, tipoTopico, chatter_callback)

    #Se debe indicar que se empiece a escuchar
    rospy.spin()

if __name__ == "__main__":
    lector()
