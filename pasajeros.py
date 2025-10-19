from vuelo import  Vuelo
from reserva import Reserva

class Pasajeros:
    def __init__(self, nombre, dni, nac):
        self.nombre = nombre
        self.dni = dni
        self.nac = nac
        self.equipaje={} # cree la funcion para agregar equipaje
        self.h_vuelos = []

    def __str__(self):
        return f'nombre: {self.nombre} \ndni: {self.dni} \nnac:{self.nac}'


    def agregar_equipaje(self,tipo,cantidad):
      if tipo in ("De mano","De cabina","De bodega"):
        self.equipaje[tipo]=cantidad
      else :
        print("equipaje incorrecto")
        
        
p1 = Pasajeros('Matias', 30459, 'arg')
p2 = Pasajeros('PEDRITO', 9999, 'arg')
p3 = Pasajeros('Sofia',78789789789, 'arg')
#print(p)
p1.agregar_equipaje("De mano",1)
p1.agregar_equipaje("De cabina",9)

print(p1.equipaje)


brasil = Vuelo('br101', 'BsAs', 'Brasilia', '17/10/2025')
reserva1 = Reserva(p1, brasil)

brasil.agregar_pasajero(p1)
brasil.agregar_pasajero(p2)
brasil.agregar_pasajero(p3)
#print(brasil._cupo)

brasil.mostrar_pasajeros()
#print(reserva1)
#print(reserva1.codigo)