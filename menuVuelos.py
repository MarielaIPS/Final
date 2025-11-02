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

p0=Pasajero("Juana",9899898,"arg")
p1 = Pasajero('Matias', 30459, 'arg')
p2 = Pasajero('PEDRITO', 9999, 'arg')


p1.agregar_equipaje("De mano",1)
p1.agregar_equipaje("De cabina",9)




brasil = Vuelo('br101', 'BsAs', 'Brasilia', '17/10/2025')
reserva1 = Reserva(p1, brasil)

brasil.agregar_pasajero(p0)
brasil.agregar_pasajero(p1)
brasil.agregar_pasajero(p2)


print("Los cupos disponibles en este vuelo son: ",brasil._cupo)


brasil.mostrar_pasajeros()



p = Pasajero('LORENZO', 387765, 'arg')

p.agregar_equipaje("De mano",1)
p.agregar_equipaje("De cabina",2)
p.agregar_equipaje("De bodega",4)
p.agregar_equipaje("De bodega",1)
print(p.equipaje)

print("La cantidad de equipaje en total es: " ,p.total_equipaje_cantidad)


p.eliminar_equipaje("De bodega",2)


p.total_kilos()

p.total_en_kilos

p.Agregar_vuelo("maiameeeeee")
p.Agregar_vuelo("newzeland")

print(p.h_vuelos)

p.eliminar_vuelo("newzeland")
print(p.h_vuelos)

print(brasil.buscar_pasajero_binaria(p))

brasil.mostrar_pasajeros()