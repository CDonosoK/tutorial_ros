#!/usr/bin/env python

#Se importa la librería

import rospy, math, time

#Se importan los mensajes que se utilizarán
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

#Función auxiliar la cual actualizará los datos constamente
def funcionCallback(mensaje):
    global posX, posY, Giro
    posX = mensaje.x
    posY = mensaje.y
    Giro = mensaje.theta

def movimientoLineal(velocidadTopico, velocidad, distancia, haciaDelante):
    
    #Se declara el tipo de mensaje que se utilizará
    mensajeVelocidad = Twist()
    global posX, posY

    #Guardamos las posiciones iniciales
    X0, Y0 = posX, posY

    #Se forza que la velocidad sea positiva o negativa según se indique
    if haciaDelante:
        mensajeVelocidad.linear.x = abs(velocidad)
    else:
        mensajeVelocidad.linear.x = -abs(velocidad)

    #Para calcular la distancia recorrida
    distanciaRecorrida = 0

    #La frecuencia está seteada en 10 acciones por segundo
    frecuencia = rospy.Rate(10)

    while True:
        
        rospy.loginfo("Distancia recorrida: {}".format(distanciaRecorrida))
        velocidadTopico.publish(mensajeVelocidad)

        frecuencia.sleep()

        #Se calcula la distancia recorrida
        distanciaRecorrida = math.sqrt((posX - X0)**2 + (posY - Y0)**2)
        
        #Verificamos si se ha alcanzado la distancia deseada
        if not (distanciaRecorrida < distancia):
            rospy.loginfo("Se llegó")
            break
    
    #Se detiene el robot
    mensajeVelocidad.linear.x = 0
    velocidadTopico.publish(mensajeVelocidad)

if __name__ == "__main__":
    try:
        #Se inicializa el nodo
        rospy.init_node("turtle_motion_pose", anonymous = True)

        #Se escriben los datos en el tópico correspondiente
        nombreTopico_velocidad = "turtle1/cmd_vel"
        veloPublisher = rospy.Publisher(nombreTopico_velocidad, Twist, queue_size = 10)

        #Se suscribe al tópico correspondiente
        nombreTopico_posicion = "turtle1/pose"
        posPublisher = rospy.Subscriber(nombreTopico_posicion, Pose, funcionCallback)
        time.sleep(2)

        #Se llama a la función movimiento
        # Velocidad 10 metros por segundos, distancia de 4 metros, movimiendo hacia adelante
        movimientoLineal(veloPublisher, 5, 4, False)

    except rospy.ROSInterruptException:
        rospy.loginfo("Se interrumpió la ejecución del programa")