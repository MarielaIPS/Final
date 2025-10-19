import random
import string
class Pasajeros:
    def __init__(self, nombre, dni, nac):
        self.nombre = nombre
        self.dni = dni
        self.nac = nac
        #self.set_equipaje(equi)
        self.h_vuelos = []
    def __str__(self):
        return f'nombre: {self.nombre} \ndni: {self.dni} \nnac:{self.nac}'
    # def set_equipaje(self, equi):
    #     equipaje = {
    #         'formato' : '',
    #         'cantidad' : 0
    #     }
    #     if equi in ('De mano', 'De cabina', 'bodega'):
    #         self.equipaje = equipaje.equi
    #     else:
    #         return print('Equipaje incorrecto')


class Vuelo:
    def __init__(self, codigo, origen,destino, fecha):
        self.codigo =codigo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.pasajeros = []
        self.cupo = 100

    #def agregar_pasajero(pasajero):
    # agregar a la lista
    # quitar al cupo    
    def __str__(self):
        return f'codigo: {self.codigo} \norigen: {self.origen} \nDestino:{self.destino} \nFecha: {self.fecha}'

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
  


    # def reservar_vuelo(self, pasajero, vuelo):
    #     self.codigo = '1'
    #     self.pasajero = pasajero
    #     self.vuelo = vuelo

    def __str__(self):
        return f'Codigo de reserva:{self.codigo}\nDatos del vuelo:\n{self.vuelo} \nDatos del pasajero: \n{self.pasajero}'

brasil = Vuelo('br101', 'BsAs', 'Brasilia', '17/10/2025')      
p = Pasajeros('matias', 30459, 'arg')
reserva1 = Reserva(p, brasil)

print(reserva1)



