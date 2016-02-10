# v0.1


def bienvenidos ():
	print("Bienvenido a Agenda Telefonica")
	print("Selecciona una opción: ")
	print("1.- Añadir un registro a la agenda")
	print("2.- Listar el contenido de la agenda")

def escribir ():
	agenda = open("agenda_telefonica.csv",'a')
	nombre = input ("Introduce el nombre de contacto: ")
	telefono = input("Introduce tu telefono: ")
	posicion = input("Introduce la posicion")
	print("Se ha introducio el nombre",nombre, " con el numero", telefono)
	agenda.write(posicion)
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

bienvenidos()
opcion = input(">")


print("Has elegido la opcion",opcion)

if opcion =="1":
	escribir()
elif opcion == "2":
	print("Cuantos registros quieres ver")
	registros=input(">")
	registrosnumero = int(registros)
	listar(registrosnumero)
else :
	mierror()