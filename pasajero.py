from vuelo import  Vuelo
from reserva import Reserva

class Pasajero:
    def __init__(self, nombre, dni, nac):
        self.nombre = nombre
        self.dni = dni
        self.nac = nac
        self.equipaje={} 
        self.h_vuelos = []

    def __str__(self):
        return f'nombre: {self.nombre} \ndni: {self.dni} \nnac:{self.nac}'


    def agregar_equipaje(self,tipo,cantidad):
      if tipo in ("De mano","De cabina","De bodega"):
        self.equipaje[tipo]=cantidad
      else :
        print("equipaje incorrecto")
        
        
