#!/usr/bin/env python

#Se importa la librería
import rospy, math, time

#Se importan los mensajes que se utilizarán
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

#Funciones realizadas anteriormente
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
        mensajeVelocidad.linear.x = distancia*0.8
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

def robotLimpiador2D(publisher):
    
    #Se declara la posicion inicial del robot
    posicionInicial = Pose()
    posicionInicial.x = 1
    posicionInicial.y = 1
    posicionInicial.theta = 90
    movimientoObjetivo(publisher, 1, 1)

    movimientoGiro(publisher, 30, 90, True)

    for i in range(6):
        if i%2 == 0:
            movimientoObjetivo(publisher, posX, posY+9)
            movimientoGiro(publisher, 30, 90, True)
            movimientoObjetivo(publisher, posX+2, posY)
            movimientoGiro(publisher, 30, 90, True)
        else:
            movimientoObjetivo(publisher, posX, posY-9)
            movimientoGiro(publisher, 30, 90, False)
            movimientoObjetivo(publisher, posX+2, posY)
            movimientoGiro(publisher, 30, 90, False)

    movimientoObjetivo(publisher, posX, posY+9)
    movimientoObjetivo(publisher, 1, 1)

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
        robotLimpiador2D(veloPublisher)

    except rospy.ROSInterruptException:
        rospy.loginfo("Se interrumpió la ejecución del programa")