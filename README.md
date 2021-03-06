# TUTORIAL ROS
Made by Clemente Donoso, 馃搷 Chile 馃嚚馃嚤

If you want to contribute monetarily to the creation of the project, you can do so via PayPal: https://paypal.me/cdonosok

Si quieres saber m谩s sobre [ROS](https://www.ros.org/), la instalaci贸n y sus paquetes puedes hacer click **[aqu铆](https://trail-dichondra-73f.notion.site/Robot-Operating-System-ROS-723ce4c7636f431c8746896f83c09882)**


#### [Tutorial 01](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-basico/tutorial-01)
Corresponde a un breve ejemplo de como construir un nodo de escritura y lectura bajo el paradigma de comunicaci贸n: **Publisher/Subscriber**

 - El **nodoEscritura.py** escribe en el t贸pico "tutorial01" un mensaje.
 - El **nodoLectura.py** lee dicho t贸pico y recibe la informaci贸n enviada.

 Para su utilizaci贸n se debe ejecutar los siguientes comandos:
 - **Terminal N掳1:** ```roscore```
 - **Terminal N掳2:** ```rosrun tutorial-ros nodoEscritura.py```
 - **Termianl N掳3:** ```rosrun tutorial-ros nodoLectura.py```

---

 #### [Tutorial 02](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-basico/tutorial-02)
 Corresponde a un breve ejemplo de como enviar mensajes personalizados a partir de un nodo de escritura y lectura bajo el paradigma de comunicaci贸n: **Publisher/Subscriber** (El mensaje personalizado se define en el archivo *msg/mensajeCustomizado.msg*)

 - El **escritorPersonalizado.py** escribe en el t贸pico "tutorial02" un mensaje personalizado.
 - El **lectorPersonalizado.py** lee dicho t贸pico y recibe la informaci贸n enviada.

 Para su utilizaci贸n se debe ejecutar los siguientes comandos:
 - **Terminal N掳1:** ```roscore```
 - **Terminal N掳2:** ```rosrun tutorial-ros escritorPersonalizado.py```
 - **Termianl N掳3:** ```rosrun tutorial-ros lectorPersonalizado.py```

---

  #### [Tutorial 03](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-basico/tutorial-03)
Corresponde a un breve ejemplo de como utilizar un servicio implementado en un servidor, y as铆 el nodo cliente utiliza la informaci贸n enviada de vuelta a partir del paradigma de comunicaci贸n : **Cliente/Servidor** (El servicio personalizado se define en el archivo *srv/servicioPersonalizado.srv*).

- El **servidorPersonalizado.py** es un servidor que recibe un mensaje personalizado y realiza alguna tarea, es importante que el servidor est茅 corriendo antes del cliente.
- El **clientePersonalizado.py** es un cliente que utiliza el servicio personalizado para enviar datos

 - **Terminal N掳1:** ```roscore```
 - **Terminal N掳2:** ```rosrun tutorial-ros servidorPersonalizado.py```
 - **Terminal N掳3:** ```rosrun tutorial-ros clientePersonalizado.py```

---

#### [Tutorial 04](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-basico/tutorial-04)
Corresponde al primer ejemplo para la creaci贸n de un robot aspiradora b谩sico, d贸nde se utiliza el simulador turtlesim para la simulaci贸n de un robot en 2 dimensiones.

Las siguientes l铆neas de comando corresponden a como **mover el robot en l铆nea recta**, para ello se debe ejecutar los siguientes comandos:

  - **Terminal N掳1:** ```roscore```
  - **Terminal N掳2:** ```rosrun turtlesim turtlesim_node```
  - **Terminal N掳3:** ```rosrun tutorial-ros movimientoLineal.py```

Las siguientes l铆neas de comando corresponden a como **hacer que el robot gire en el punto**, para ello se debe ejecutar los siguientes comandos:

  - **Terminal N掳1:** ```roscore```
  - **Terminal N掳2:** ```rosrun turtlesim turtlesim_node```
  - **Terminal N掳3:** ```rosrun tutorial-ros movimientoGiro.py```
  
Las siguientes l铆neas de comando corresponden a como **hacer que el robot se diriga a un objetivo**, para ello se debe ejecutar los siguientes comandos:

  - **Terminal N掳1:** ```roscore```
  - **Terminal N掳2:** ```rosrun turtlesim turtlesim_node```
  - **Terminal N掳3:** ```rosrun tutorial-ros movimientoObjetivo.py```

Las siguientes l铆neas de comando corresponden a como **hacer que el robot aparezca inicialmente en una orientaci贸n determinada**, para ello se debe ejecutar los siguientes comandos:

  - **Terminal N掳1:** ```roscore```
  - **Terminal N掳2:** ```rosrun turtlesim turtlesim_node```
  - **Terminal N掳3:** ```rosrun tutorial-ros definirOrientacion.py```

Las siguientes l铆neas de comando corresponden a **la combinaci贸n de las funciones anteriores para realizar un robot que se mueva por toda la cuadrilla**, para ello se debe ejecutar los siguientes comandos:

  - **Terminal N掳1:** ```roscore```
  - **Terminal N掳2:** ```rosrun turtlesim turtlesim_node```
  - **Terminal N掳3:** ```rosrun tutorial-ros robotLimpiador2D.py```

---

#### [Tutorial 05](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-basico/tutorial-05)
Corresponde a la creaci贸n de un archivo para ejecutar m煤ltiples nodos al mismo tiempo (sin la necesidad de ejecutar roscore), este caso, se utilizar谩 para ejecutar el enterno visual de turtlesim y tambi茅n los comandos de movimiento del robot.

  - **Terminal N掳1:** ```roslaunch tutorial_ros aspiradora2D.launch```

---

#### [Tutorial 06 [OPCIONAL]](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-basico/tutorial-06)
Corresponde a la lectura de una imagen mediante la librer铆a de python OpenCV (no se utilizar谩 ROS en este tutorial) y as铆 la verificaci贸n de que la instalaci贸n de OpenCV est茅 correcta. Adem谩s es necesario ejecutar el archivo directamente desde la carpeta en donde se encuentra.

El archivo **lecturaArchivo.py** corresponde a la lectura de una imagen guardada en memoria.

  - **Terminal N掳1:** ``` python lecturaArchivo.py```

El siguiente archivo corresponde a verificar si se puede analizar una imagen en diversas codificaciones, para ello se debe ejecutar el siguiente comando:

  - **Terminal N掳1:** ```python lecturaImagen_Color.py```

El siguiente archivo corresponde a la observaci贸n de un video (ya sea en memoria o stream) y mostrar ciertas funcionalidades de OpenCV como lo es cambiar a escala de grises.

  - **Terminal N掳1:** ```python lecturaCamara.py```

El siguiente archivo corresponde a dibujar elementos o figuras en una imagen o video:

  - **Terminal N掳1:** ```python dibujarElementos.py```

---

#### [Tutorial 07](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-basico/tutorial-07)
Corresponde a la integraci贸n de OpenCV con ROS mediante CvBridge:
 - **Terminal N掳1:** ```roscore```
 - **Terminal N掳2:** ```rosrun usb_cam usb_cam_node```
 - **Terminal N掳3:** ```rosrun tutorial_ros cameraROS.py```

---

#### [Tutorial 08](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-basico/tutorial-08)
Corresponde a la utilizaci贸n de la t茅cnica de Thresholding para la segmentaci贸n de una imagen. Se probar谩 la t茅cnica Thresholding B谩sica y Thresholding Adaptada.

Adem谩s es necesario ejecutar el archivo directamente desde la carpeta en donde se encuentra.

 - **Terminal N掳1:** ```python ejemploThresholding.py```

 ---

#### [Tutorial 09](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-basico/tutorial-09)
Corresponde a la utilizaci贸n del formato HSV para detectar un color en espec铆fico dentro de una imagen, y luego utilizar una m谩scara para resaltarlo.

Adem谩s es necesario ejecutar el archivo directamente desde la carpeta en donde se encuentra.

 - **Terminal N掳1:** ```python filtrarColor.py```

 ---

#### [Tutorial 10 [OPCIONAL]](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-basico/tutorial-10)
Corresponde a la utilizaci贸n de la t茅cnica de detecci贸n de contornos en una imagen a trav茅s de un threshold adaptado o b谩sico. Luego tambi茅n se cuenta con una funci贸n auxiliar
para el procesamiento de los contornos, por ejemplo, calcular el 谩rea de la figura.

Adem谩s es necesario ejecutar el archivo directamente desde la carpeta en donde se encuentra.

 - **Terminal N掳1:** ```python contornoImagen.py```

 ---

#### [Tutorial 11](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-basico/tutorial-11)
Corresponde a la uni贸n de los 煤ltimos 3 t贸picos, para identificar una pelota dentro de la imagen, detectar sus contornos y resaltar el centro de esta misma.

Adem谩s es necesario ejecutar el archivo directamente desde la carpeta en donde se encuentra.

 - **Terminal N掳1:** ```python resaltarPelota.py```

Luego con el siguiente comando, se puede traquear la pelota dentro de un video.

 - **Terminal N掳2:** ```python traquearPelota.py```

#### [Tutorial 12](https://github.com/CDonosoK/tutorial_ros/tree/master/src/tutorial-basico/tutorial-12)
Corresponde a la uni贸n de los 煤ltimos 3 t贸picos, para identificar una pelota dentro de la imagen, detectar sus contornos y resaltar el centro de esta misma.

Adem谩s es necesario ejecutar el archivo directamente desde la carpeta en donde se encuentra.

 - **Terminal N掳1:** ```python procesarLidar.py```
