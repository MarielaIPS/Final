from vuelo import  Vuelo
from reserva import Reserva
from pasajero import Pasajero
import os


# MENU
os.system("cls")
opcion = 1
while (opcion >= 1 and opcion <= 3):
    print ("1.ingresar pasajero")
    print ("2.nueva reserva")
    print ("3.Buscar vuelo")
    print ("Cualquier otro valor para salir")

    opcion = int(input("Ingrese una opcion: "))    
   
    if (opcion == 1):
        nomape = input("ingrese nombre y apellido del pasajero: ")
        dni = input("ingrese documento del pasajero: ")
        nacionalidad = input("ingrese nacionalidad del pasajero: ")
        p1 = Pasajero(nomape, dni, nacionalidad)
   
    if (opcion == 2):
        pass

    if (opcion == 3):
        pass

p1 = Pasajero('Matias', 30459, 'arg')
p2 = Pasajero('PEDRITO', 9999, 'arg')

#print(p)
p1.agregar_equipaje("De mano",1)
p1.agregar_equipaje("De cabina",9)

#print(p.equipaje)


brasil = Vuelo('br101', 'BsAs', 'Brasilia', '17/10/2025')
reserva1 = Reserva(p1, brasil)

brasil.agregar_pasajero(p1)
brasil.agregar_pasajero(p2)

print(brasil._cupo)

brasil.mostrar_pasajeros()
#print(reserva1)
#print(reserva1.codigo)
