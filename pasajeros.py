
class Pasajeros:
    def __init__(self, nombre, dni, nac):
        self.nombre = nombre
        self.dni = dni
        self.nac = nac
        self.equipaje = {}
        self.total_equipaje_kilos = 0
        self.h_vuelos = []

    def __str__(self):
      return f'Nombre: {self.nombre} \nDNI: {self.dni} \nNac:{self.nac} \n Equipaje: {self.total_equipaje_kilos} Kilos'


    def sumatotal_kilos(self):
      total=sum(self.equipaje.values())
      return total

    def agregar_equipaje(self,tipo,cantidad):
      de_mano = 5
      de_cabina = 10
      de_bodega = 15
      # verificamos que el tipo de equipaje sea válido
      if tipo not in ("De mano", "De cabina", "De bodega"):
          print("Tipo de equipaje incorrecto.")
          return
      
      if tipo in self.equipaje:
          self.equipaje[tipo] += cantidad
      else:
          self.equipaje[tipo] = cantidad
         
      for clave, valor in self.equipaje.items():
          if clave == "De mano": 
            sub_total = valor * de_mano
          elif clave == "De cabina": 
            sub_total = valor * de_cabina
          elif clave == "De bodega": 
            sub_total = valor * de_bodega
      self.total_equipaje_kilos += sub_total
      print(clave, sub_total)

      # if nuevo_total > 100:
      #     print("Su equipaje no se agregará, ha superado los 100 kilos permitidos por pasajero.")
      #     return
      # actualizamos el total

    def eliminar_equipaje(self,tipo,kilos):
      #verifica si el tipo esta y si los kilos a  eliminar son menores que los que ya estan
      if tipo in self.equipaje and  self.equipaje[tipo] >= kilos:
        self.equipaje[tipo]-=kilos
        print("se elimino", kilos, "Kilos del equipaje de ", tipo)
        self.total_equipaje_kilos = self.sumatotal_kilos()


p = Pasajeros('matias', 30459, 'arg')

p.agregar_equipaje("De mano",1)
p.agregar_equipaje("De cabina",1)
p.agregar_equipaje("De bodega",1)
p.agregar_equipaje("De bodega",1)
p.agregar_equipaje("De bodega",1)
print(p.equipaje)

print("El total es: " ,p.total_equipaje_kilos)


p.eliminar_equipaje("De bodega",20)


print(p)

print(p.equipaje)