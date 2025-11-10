import os
import csv
import random
import string

class Vuelo:
    def __init__(self, origen, destino,  duracion):
        self.codigo = self.generar_codigo()
        self.origen = origen
        self.destino = destino
        #self.fecha = fecha
        self.duracion = duracion
        self._pasajeros = [] #privada la lista de pasajeros para que no se pueda acceder desde el atributo
        self._cupo = 100

    def agregar_pasajero(self,pasajero):
    # agrega a la lista el pasajero y quita 1 cupo, Pasa a todo el objeto pasajero
        if pasajero not in self._pasajeros and self._cupo >0 and self._cupo <= 100 : 
            self._pasajeros.append(pasajero)
            self._cupo-=1
        else:
            print("el pasajero ya se encuentra o se supero el limite en este viaje")   
    
    def mostrar_pasajeros(self):
        print("Los pasajeros en este vuelo son:")
        for i in   self._pasajeros:
            print(i.nombre,i.dni)      
         
    def generar_codigo(self):
        letras = ''.join(random.choices(string.ascii_uppercase, k=2))
        numeros = ''.join(random.choices(string.digits, k=3))
        return f"V{letras}{numeros}"

    def __str__(self):
        #return f'codigo: {self.codigo} \nOrigen: {self.origen} \nDestino:{self.destino} \nFecha: {self.fecha}'
        return f'Codigo: {self.codigo} | Origen: {self.origen} → Destino: {self.destino} (Duracion: {self.duracion})'
