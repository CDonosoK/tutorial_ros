#!/usr/bin/env python

#Importamos la librería rospy
import rospy

#Importamos los mensajes que se utilizarán
from std_msgs.msg import String

def escritor():

    #Se debe inicializar el nodo ROS
    nombreNodo = "escritor"
    idUnico = True
    rospy.init_node(nombreNodo, anonymous = idUnico)
    
    #Se crea el objeto Publisher 
    nombreTopico = "tutorial01"
    tipoTopico = String #Definido en ROS
    tamanoBuffer = 10 #Cuantos mensajes se van a almacenar si existe delay
    publisher = rospy.Publisher(nombreTopico, tipoTopico, queue_size = tamanoBuffer)

    #Se define la frecuencia en Hertz
    #Cantidad de mensajes que se publican cada segundo
    frecuencia = rospy.Rate(1)

    #Se define el ciclo principal
    while not rospy.is_shutdown():

        #Se define el mensaje y se envia
        mensaje = "Hola desde el nodo escritor"
        rospy.loginfo(mensaje)
        publisher.publish(mensaje)
        frecuencia.sleep()

if __name__ == "__main__":
    try:
        escritor()
    except rospy.ROSInterruptException:
        pass