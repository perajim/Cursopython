# v0.1
import modulos

def principal():
	modulos.bienvenidos()
	opcion = input(">")


	print("Has elegido la opcion",opcion)

	if opcion =="1":
		modulos.escribir()
		principal()
	elif opcion == "2":
		print("Cuantos registros quieres ver")
		registros=input(">")
		registrosnumero = int(registros)
		modulos.listar(registrosnumero)
		principal()
	elif opcion == "3":
		print("Dime el nombre de la persona que estas buscando")
		nombrebuscado=input(">")
		modulos.buscador(nombrebuscado)
		principal()
	else :
		modulos.mierror()
		principal()

principal()