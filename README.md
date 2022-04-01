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

---

#### [Tutorial 04](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-04)
Corresponde al primer ejemplo para la creación de un robot aspiradora básico, dónde se utiliza el simulador turtlesim para la simulación de un robot en 2 dimensiones.

Las siguientes líneas de comando corresponden a como **mover el robot en línea recta**, para ello se debe ejecutar los siguientes comandos:

  - **Terminal N°1:** ```roscore```
  - **Terminal N°2:** ```rosrun turtlesim turtlesim_node```
  - **Terminal N°3:** ```rosrun tutorial-ros movimientoLineal.py```

Las siguientes líneas de comando corresponden a como **hacer que el robot gire en el punto**, para ello se debe ejecutar los siguientes comandos:

  - **Terminal N°1:** ```roscore```
  - **Terminal N°2:** ```rosrun turtlesim turtlesim_node```
  - **Terminal N°3:** ```rosrun tutorial-ros movimientoGiro.py```
  
Las siguientes líneas de comando corresponden a como **hacer que el robot se diriga a un objetivo**, para ello se debe ejecutar los siguientes comandos:

  - **Terminal N°1:** ```roscore```
  - **Terminal N°2:** ```rosrun turtlesim turtlesim_node```
  - **Terminal N°3:** ```rosrun tutorial-ros movimientoObjetivo.py```

Las siguientes líneas de comando corresponden a como **hacer que el robot aparezca inicialmente en una orientación determinada**, para ello se debe ejecutar los siguientes comandos:

  - **Terminal N°1:** ```roscore```
  - **Terminal N°2:** ```rosrun turtlesim turtlesim_node```
  - **Terminal N°3:** ```rosrun tutorial-ros definirOrientacion.py```

Las siguientes líneas de comando corresponden a **la combinación de las funciones anteriores para realizar un robot que se mueva por toda la cuadrilla**, para ello se debe ejecutar los siguientes comandos:

  - **Terminal N°1:** ```roscore```
  - **Terminal N°2:** ```rosrun turtlesim turtlesim_node```
  - **Terminal N°3:** ```rosrun tutorial-ros robotLimpiador2D.py```

---

#### [Tutorial 05](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-05)
Corresponde a la creación de un archivo para ejecutar múltiples nodos al mismo tiempo (sin la necesidad de ejecutar roscore), este caso, se utilizará para ejecutar el enterno visual de turtlesim y también los comandos de movimiento del robot.

  - **Terminal N°1:** ```roslaunch tutorial_ros aspiradora2D.launch```

---

#### [Tutorial 06 [OPCIONAL]](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-06)
Corresponde a la lectura de una imagen mediante la librería de python OpenCV (no se utilizará ROS en este tutorial) y así la verificación de que la instalación de OpenCV esté correcta. Además es necesario ejecutar el archivo directamente desde la carpeta en donde se encuentra.

El archivo **lecturaArchivo.py** corresponde a la lectura de una imagen guardada en memoria.

  - **Terminal N°1:** ``` python lecturaArchivo.py```

El siguiente archivo corresponde a verificar si se puede analizar una imagen en diversas codificaciones, para ello se debe ejecutar el siguiente comando:

  - **Terminal N°1:** ```python lecturaImagen_Color.py```

El siguiente archivo corresponde a la observación de un video (ya sea en memoria o stream) y mostrar ciertas funcionalidades de OpenCV como lo es cambiar a escala de grises.

  - **Terminal N°1:** ```python lecturaCamara.py```

El siguiente archivo corresponde a dibujar elementos o figuras en una imagen o video:

  - **Terminal N°1:** ```python dibujarElementos.py```

---

#### [Tutorial 07](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-07)
Corresponde a la integración de OpenCV con ROS mediante CvBridge:
 - **Terminal N°1:** ```roscore```
 - **Terminal N°2:** ```rosrun usb_cam usb_cam_node```
 - **Terminal N°3:** ```rosrun tutorial_ros cameraROS.py```

---

#### [Tutorial 08](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-08)
Corresponde a la utilización de la técnica de Thresholding para la segmentación de una imagen. Se probará la técnica Thresholding Básica y Thresholding Adaptada.

Además es necesario ejecutar el archivo directamente desde la carpeta en donde se encuentra.

 - **Terminal N°3:** ```python ejemploThresholding.py```

 ---

#### [Tutorial 09](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-09)
Corresponde a la utilización del formato HSV para detectar un color en específico dentro de una imagen, y luego utilizar una máscara para resaltarlo.

Además es necesario ejecutar el archivo directamente desde la carpeta en donde se encuentra.

 - **Terminal N°3:** ```python filtrarColor.py```