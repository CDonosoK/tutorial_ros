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

#Función definida anteriormente en el archivo movimientoGiro.py
def movimientoGiro(velocidadTopico, velocidadAngular_, anguloGiro, sentidoGiro):
    
    mensajeVelocidad = Twist()
    #Se convierte la velocidad a radianes
    velocidadAngular = math.radians(abs(velocidadAngular_))

    #Se fuerza que el sentido de giro sea positivo o negativo
    if sentidoGiro:
        mensajeVelocidad.angular.z = -abs(velocidadAngular)
    else:
        mensajeVelocidad.angular.z = abs(velocidadAngular)

    #La frecuencia está seteada en 10 acciones por segundo
    frecuencia = rospy.Rate(10)
    t0 = rospy.Time.now().to_sec()

    while True:
        velocidadTopico.publish(mensajeVelocidad)

        #Se calcula el ángulo recorrido
        t1 = rospy.Time.now().to_sec()
        anguloActual = (t1 - t0) * velocidadAngular_
        rospy.loginfo("Angulo recorrido: {}".format(anguloActual))
        frecuencia.sleep()

        #Verificamos si se ha alcanzado el ángulo deseado
        if not (anguloActual < anguloGiro):
            rospy.loginfo("Se llegó")
            break
    
    #Se detiene el robot
    mensajeVelocidad.angular.z = 0
    velocidadTopico.publish(mensajeVelocidad)

def definirOrientacion(topicoVelocidad, velocidad, angulo):

    #Se calcula el angulo deseado
    anguloRadiantes = math.radians(angulo) - giro

    sentidoGiro = False
    if anguloRadiantes <0:
        sentidoGiro = True
    else:
        sentidoGiro = False

    movimientoGiro(topicoVelocidad, velocidad, math.degrees(abs(anguloRadiantes)), sentidoGiro)


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
        definirOrientacion(veloPublisher, 30, 90)

    except rospy.ROSInterruptException:
        rospy.loginfo("Se interrumpió la ejecución del programa")
    