# v0.1
import modulos

modulos.bienvenidos()
opcion = input(">")


print("Has elegido la opcion",opcion)

if opcion =="1":
	modulos.escribir()
elif opcion == "2":
	print("Cuantos registros quieres ver")
	registros=input(">")
	registrosnumero = int(registros)
	modulos.listar(registrosnumero)
elif opcion == "3":
	print("Dime el nombre de la persona que estas buscando")
	nombrebuscado=input(">")
	modulos.buscador(nombrebuscado)
else :
	modulos.mierror()