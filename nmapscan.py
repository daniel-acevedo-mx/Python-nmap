#!/usr/bin/python3

import nmap

nm = nmap.PortScanner()
print ("ingrese los host de su pc o ip\nejemplo: 127.2.3.0/24  es decir que al ultimo digito ingrese de cual a cual analizar")
host=input()
nm.scan(hosts=host,arguments='-n -sP -PE -PA21,23,80,3389')
hosts_list = [(x, nm[x]['status']['state'])for x in nm.all_hosts()]
for host, status in hosts_list:
    print(f'Host: {host} - Estado: {status}')
#print('{0}:{1}'.host)

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
#nm = nmap.PortScanner()
#if argumento2=='y':
#	print("Ingrese el puerto que desea escanear, ejemplo: 22")
#	port= input()
#	nm.scan(ip2, port, arguments='-oX resultado.xml')
#
#	# Puedes acceder a los resultados si es necesario
#	print(nm.csv())
#
#	# Puedes acceder a los resultados directamente desde el archivo XML
#	with open('resultado.xml', 'r') as f:
#	    print(f.read())
#else:
#	print("todo listo")



