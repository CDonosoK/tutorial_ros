#!/usr/bin/env python

#Importamos la librería rospy y random
import rospy, random

#Importamos el mensaje personalizado
from tutorial_ros.msg import mensajeCustomizado

def escritor():

    #Se debe inicializar el nodo ROS
    nombreNodo = "escritor"
    idUnico = True
    rospy.init_node(nombreNodo, anonymous = idUnico)
    
    #Se crea el objeto Publisher 
    nombreTopico = "tutorial02"
    tipoTopico = mensajeCustomizado #Definido en ROS
    tamanoBuffer = 10 #Cuantos mensajes se van a almacenar si existe delay
    publisher = rospy.Publisher(nombreTopico, tipoTopico, queue_size = tamanoBuffer)

    #Se define la frecuencia en Hertz
    #Cantidad de mensajes que se publican cada segundo
    frecuencia = rospy.Rate(1)

    #Se define el ciclo principal
    while not rospy.is_shutdown():

        #Se define el contenido del mensaje customizado y se envia
        mensaje =  mensajeCustomizado()
        mensaje.id = 1
        mensaje.nombre = "Sensor 01"
        mensaje.ubicacion = "Santiago-Chile"
        mensaje.temperatura = 20.0 + random.randint(0,10)*0.3
        mensaje.humedad = 50.0 + random.randint(0,30)*0.3
        rospy.loginfo("Mensaje enviado: ")
        rospy.loginfo(mensaje)
        publisher.publish(mensaje)
        frecuencia.sleep()

if __name__ == "__main__":
    try:
        escritor()
    except rospy.ROSInterruptException:
        pass