#!/usr/bin/env python

import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import sys

bridge = CvBridge()

def imagen_callback(imagenROS):
    global bridge
    
    # Convertimos la imagen ROS a una imagen OpenCV
    try:
        imagenOpenCV = bridge.imgmsg_to_cv2(imagenROS, "bgr8")
    except CvBridgeError as e:
        print(e)
    
    #Ahora se pueden utilizar las funciones de OpenCV
    cv2.putText(imagenOpenCV, "Imagen Obtenida por ROS", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 1)
    cv2.imshow("Imagen Obtenida por ROS", imagenOpenCV)
    cv2.waitKey(3)

def main(args):
    #Se inicializa el nodo ROS
    rospy.init_node('camaraROS', anonymous=True)
    nombreTopico = "/usb_cam/image_raw"
    #Dependiendo de donde se obtendrá la imagen, dependerá el tópico
    rospy.Subscriber(nombreTopico, Image, imagen_callback)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
