
class Vuelo:
    def __init__(self, codigo, origen,destino, fecha):
        self.codigo =codigo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
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
              
    
    
    def __str__(self):
        return f'codigo: {self.codigo} \norigen: {self.origen} \nDestino:{self.destino} \nFecha: {self.fecha}'
