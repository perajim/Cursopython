def bienvenidos ():
	print("Bienvenido a Agenda Telefonica")
	print("Selecciona una opción: ")
	print("1.- Añadir un registro a la agenda")
	print("2.- Listar el contenido de la agenda")
	print("3.- Buscar por nombre")


def escribir ():
	
	nombre = input ("Introduce el nombre de contacto: ")
	telefono = input("Introduce tu telefono: ")
	agenda = open("agenda_telefonica.csv")
	for n in range(1,40):
		linea = agenda.readline()		
		lineapartida = linea.split(",")
		##print(lineapartida[0])
		if lineapartida[0] != "" :
			memoria = lineapartida[0]
	agenda.close()
	memonum = int(memoria)
	posicion = 0
	posicion = memonum+1
	postr = str(posicion)
	print("Se ha introducio el nombre",nombre, " con el numero", telefono)
	agenda = open("agenda_telefonica.csv",'a')
	agenda.write(postr)
	agenda.write(",")
	agenda.write(nombre)
	agenda.write(",")
	agenda.write(telefono)
	agenda.write("\n")
	agenda.close()
	print("Has elegido Añadirun registroa la agenda")

def listar(fin):	
	agenda = open ("agenda_telefonica.csv")
	numero = 0
	print("Has elegido la opcion listar el contenido de la agenda")
	for i in range(0,fin):
		lectura = agenda.readline()
		print(lectura.replace(",","\t\t"))		
		numero=numero+1
	agenda.close()

def mierror():
	print("La opcion que has elegido no  es valida")

def buscador(nombrebuscado):
	print("Aqui encontramos diferencias")
	agenda = open ("agenda_telefonica.csv")
	for i in range (1,25):
		lectura = agenda.readline()
		partido = lectura.split(",")
		if nombrebuscado == partido[1]:	
			print(partido[1])
	agenda.close
	

