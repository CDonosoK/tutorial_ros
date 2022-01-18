# TUTORIAL ROS

#### [Tutorial 01](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-01)
Corresponde a un breve ejemplo de como construir un nodo de escritura y lectura bajo el paradigma de comunicación: **Publisher/Subscriber**

 - El **nodoEscritura.py** escribe en el tópico "tutorial01" un mensaje.
 - El **nodoLectura.py** lee dicho tópico y recibe la información enviada.

 Para su utilización se debe ejecutar los siguientes comandos:
 - **Terminal N°1:** ```roscore```
 - **Terminal N°2:** ```rosrun tutorial-ros nodoEscritura.py```
 - **Termianl N°3:** ```rosrun tutorial-ros nodoLectura.py```

 ---

 #### [Tutorial 02](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-02)
 Corresponde a un breve ejemplo de como enviar mensajes personalizados a partir de un nodo de escritura y lectura bajo el paradigma de comunicación: **Publisher/Subscriber**

 - El **nodoEscritura.py** escribe en el tópico "tutorial02" un mensaje personalizado.
 - El **nodoLectura.py** lee dicho tópico y recibe la información enviada.

 Para su utilización se debe ejecutar los siguientes comandos:
 - **Terminal N°1:** ```roscore```
 - **Terminal N°2:** ```rosrun tutorial-ros escritorPersonalizado.py```
 - **Termianl N°3:** ```rosrun tutorial-ros lectorPersonalizado.py```

 ---

  #### [Tutorial 03](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-03)

