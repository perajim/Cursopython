agenda = open("agenda_telefonica.csv",'a')
##print(agenda.read())
##agenda.truncate()

nombre = input ("Introduce el nombre de contacto: ")
telefono = input("Introduce tu telefono: ")
print("Se ha introducio el nombre",nombre, " con el numero", telefono)

agenda.write(nombre)
agenda.write(",")
agenda.write(telefono)
agenda.write("\n")
agenda.close()

