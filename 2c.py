agenda = open ("agenda_telefonica.csv")

##print (agenda.read())


##for i in range(0,25):
##	print(agenda.readline())

numero = 0
while  numero<25:
	print(agenda.readline())
	numero=numero+1

print("Ya hemos terminado de leer el archivo")