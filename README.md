# TUTORIAL ROS
Made by Clemente Donoso, 📍 Chile 🇨🇱

If you want to contribute monetarily to the creation of the project, you can do so via PayPal: https://paypal.me/cdonosok


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
 Corresponde a un breve ejemplo de como enviar mensajes personalizados a partir de un nodo de escritura y lectura bajo el paradigma de comunicación: **Publisher/Subscriber** (El mensaje personalizado se define en el archivo *msg/mensajeCustomizado.msg*)

 - El **escritorPersonalizado.py** escribe en el tópico "tutorial02" un mensaje personalizado.
 - El **lectorPersonalizado.py** lee dicho tópico y recibe la información enviada.

 Para su utilización se debe ejecutar los siguientes comandos:
 - **Terminal N°1:** ```roscore```
 - **Terminal N°2:** ```rosrun tutorial-ros escritorPersonalizado.py```
 - **Termianl N°3:** ```rosrun tutorial-ros lectorPersonalizado.py```

 ---

  #### [Tutorial 03](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-03)
Corresponde a un breve ejemplo de como utilizar un servicio implementado en un servidor, y así el nodo cliente utiliza la información enviada de vuelta a partir del paradigma de comunicación : **Cliente/Servidor** (El servicio personalizado se define en el archivo *srv/servicioPersonalizado.srv*).

- El **servidorPersonalizado.py** es un servidor que recibe un mensaje personalizado y realiza alguna tarea, es importante que el servidor esté corriendo antes del cliente.
- El **clientePersonalizado.py** es un cliente que utiliza el servicio personalizado para enviar datos

 - **Terminal N°1:** ```roscore```
 - **Terminal N°2:** ```rosrun tutorial-ros servidorPersonalizado.py```
 - **Terminal N°3:** ```rosrun tutorial-ros clientePersonalizado.py```
