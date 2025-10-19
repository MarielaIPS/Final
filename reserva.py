
import random
import string

class Reserva:
    def __init__(self,  pasajero, vuelo):
        self.codigo = self.set_codigo() 
        self.pasajero = pasajero
        self.vuelo = vuelo

    def set_codigo(self):
        caracteres = string.ascii_letters + string.digits
        codigo_lista = [random.choice(caracteres) for _ in range(3)]
        codigo_aleatorio = "".join(codigo_lista)
        return codigo_aleatorio
  
    def __str__(self):
        return f'Codigo de reserva:{self.codigo}\nDatos del vuelo:\n{self.vuelo} \nDatos del pasajero: \n{self.pasajero}'
