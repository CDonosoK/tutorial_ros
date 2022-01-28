#!/usr/bin/env python

#Se importa la librería
import rospy, math, time

#Se importan los mensajes que se utilizarán
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

#Función auxiliar la cual actualizará los datos constamente
def funcionCallback(mensaje):
    global posX, posY, giro
    posX = mensaje.x
    posY = mensaje.y
    giro = mensaje.theta

def movimientoObjetivo(velocidadTopico, objetivoX, objetivoY):

    #Se declara el tipo de mensaje que se utilizará
    mensajeVelocidad = Twist()
    global posX, posY, giro 

    while True:

        #Se calcula la distancia entre el robot y el objetivo
        distancia = abs(math.sqrt((objetivoX - posX)**2 + (objetivoY-posY)**2))

        #Se orienta el robot hacia el objetivo
        anguloDeseado = math.atan2(objetivoY - posY, objetivoX - posX)
        velocidadAngular = (anguloDeseado - giro)*4
        
        #Se modifica la velocidad (lineal y angular)
        mensajeVelocidad.linear.x = distancia*0.5
        mensajeVelocidad.angular.z = velocidadAngular

        #Se publica la velocidad en el tópico
        velocidadTopico.publish(mensajeVelocidad)
        rospy.loginfo("Distancia al objetivo: {}".format(distancia))
        rospy.loginfo("Ángulo hacia el objetivo: {}".format(anguloDeseado))

        if distancia <= 0.5:
            rospy.loginfo("Se alcanzó el objetivo")
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
        #Posición X del objetivo y Posición Y del objetivo
        movimientoObjetivo(veloPublisher, 10, 10)

    except rospy.ROSInterruptException:
        rospy.loginfo("Se interrumpió la ejecución del programa")

    

