# Python-nmap

buenos dias o noches profesor
en esta parte se envia la tarea de nmap, como tal tuve algunas dificultades en telegram se podra notar

para empezar con esta tarea se necesita saber que tipo de red es la que se va a necesitar es decir puente h en las dos maquitas tanto kali y ubuntu metaxploitable 
una vez estado en red puente h se necesita realizar unas pequeñas pruebas, principalmente se hace un ping en kali "ping 8.8.8.8" este es de un servidor de google el cual te responde 
ese ping se quita con mayus+c.

en dado caso de que el ping no de respuesta hay que verificar la configuracion de la red 

posteriormente tanto en las dos maquinas utilizar el comando: "ifconfig" este nos dara la ip que necesitamos 
nota: las ips tienen que ser distintas de las dos maquinas,

posteriormente instalar la libreria nmap para python con el comando 
"pip3 install nmap" o "pip3 install python-nmap"
despues de esto vamos a hablar del codigo, se comienza importando nmap
El primer input nos indica que host se va a analizar, recordemos que si queremos analizar todos se copia la ip,
pero en el ultimo punto se pone 0/24 esto nos indica que se va a analizar todos. Ejemplo: 127.0.12.0/24

luego de analizarse el script te arroja cual quieres usar en un input
el input que sigue te pregunta que de que tipo de rapides lo haga o "T4 o T5", esto siempre se contesta con t mayuscula
el siguiente input pregunta si el tipo de puerto que salga se quiere agregar un  "-on" lo cual se refiere que se haga un reporte,
este se contesta con y o n minusculas.

ya que da el analicis de los puertos se elige uno e igual te dice cuales estan abiertos.

al elegir uno hace el analicis e igual lo puedes abrir.

en la parte de los scan es algo laborioso pero funcinal esto debido a que despues de estos como se necesita solo alguna informacion y ponerla adecuada 
para la facil visualizacion y mas aparte ir analizando cada host, y puerto con un for el cual con la presencia de un contador que indica si si esta activo o cerrado el puerto 

es importante lo de -on el cual se identifica como un argumento puesto a que se utiliza con la nmap normal es decir que se reciben parametros.
de igual forma el control de -on como es uno simple se acude a solo una impresion que es un puesto y un host que requiere nuestro scan.




