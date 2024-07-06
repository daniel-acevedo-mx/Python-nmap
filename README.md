# Python-nmap

#buenos dias o noches profesor
#en esta parte se envia la tarea de nmap, como tal tuve algunas dificultades en telegram se podra notar

#para empezar con esta tarea se necesita saber que tipo de red es la que se va a necesitar es decir puente h en las dos maquitas tanto kali y ubuntu metaxploitable 
#una vez estado en red puente h se necesita realizar unas pequeñas pruebas, principalmente se hace un ping en kali "ping 8.8.8.8" este es de un servidor de google el cual te responde 
#ese ping se quita con mayus+c.

#en dado caso de que el ping no de respuesta hay que verificar la configuracion de la red 

#posteriormente tanto en las dos maquinas utilizar el comando: "ifconfig" este nos dara la ip que necesitamos 
#nota: las ips tienen que ser distintas de las dos maquinas,

#posteriormente instalar la libreria nmap para python con el comando 
#"pip3 install nmap" o "pip3 install python-nmap"
#despues de esto vamos a hablar del codigo, se comienza importando nmap
#El primer input nos indica que host se va a analizar, recordemos que si queremos analizar todos se copia la ip,
#pero en el ultimo punto se pone 0/24 esto nos indica que se va a analizar todos. Ejemplo: 127.0.12.0/24

#luego de analizarse el script te arroja cual quieres usar en un input
#el input que sigue te pregunta que de que tipo de rapides lo haga o "T4 o T5", esto siempre se contesta con t mayuscula
#el siguiente input pregunta si el tipo de puerto que salga se quiere agregar un  "-on" lo cual se refiere que se haga un reporte,
#este se contesta con y o n minusculas.

#ya que da el analicis de los puertos se elige uno e igual te dice cuales estan abiertos.

#al elegir uno hace el analicis e igual lo puedes abrir.

##en la parte de los scan es algo laborioso pero funcinal esto debido a que despues de estos como se necesita solo alguna informacion y ponerla adecuada 
#para la facil visualizacion y mas aparte ir analizando cada host, y puerto con un for el cual con la presencia de un contador que indica si si esta activo o cerrado el puerto 

#es importante lo de -on el cual se identifica como un argumento puesto a que se utiliza con la nmap normal es decir que se reciben parametros.
#de igual forma el control de -on como es uno simple se acude a solo una impresion que es un puesto y un host que requiere nuestro scan.



import nmap

nm = nmap.PortScanner()
print ("ingrese los host de su pc o ip\nejemplo: 127.2.3.0/24  es decir que al ultimo digito ingrese de cual a cual analizar")
host=input()
nm.scan(hosts=host,arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, nm[x]['status']['state'])for x in nm.all_hosts()]
for host, status in hosts_list:
    print('{0}:{1}'.host)

print("Ingresa host a analizar: \n")
ip=input()

ip2=ip.strip()
puertos_abiertos="-p "
argumento=input("ingreasa si deseas argumento T4 o T5\n")

nm = nmap.PortScanner()
results = nm.scan(hosts=ip,arguments="-sT -n -Pn "+str(argumento))
count=0
print (results)
print("\nHost : %s" % ip)
print("State : %s" % nm[ip].state())
for proto in nm[ip].all_protocols():
	print("Protocol : %s" % proto)
	print()
	lport = nm[ip][proto].keys()
	sorted(lport)
	for port in lport:
		print ("port : %s\tstate : %s" % (port, nm[ip][proto][port]["state"]))
		if count==0:
			puertos_abiertos=puertos_abiertos+str(port)
			count=1
		else:
			puertos_abiertos=puertos_abiertos+","+str(port)

print("\nPuertos abiertos: "+ puertos_abiertos +" "+str(ip))

argumento2=input("deseas agregar argumento para guardar el reporte en un txt ? y/n?\n")
nm = nmap.PortScanner()
if argumento2=='y':
	print("Ingrese el puerto que desea escanear, ejemplo: 22")
	port= input()
	nm.scan(ip2, port, arguments='-oX resultado.xml')

#	# Puedes acceder a los resultados si es necesario
print(nm.csv())
#
#	# Puedes acceder a los resultados directamente desde el archivo XML
	with open('resultado.xml', 'r') as f:
#	    print(f.read())
else:
	print("todo listo")

