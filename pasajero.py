
class Pasajero:
    def __init__(self, nombre, dni, nac):
        self.nombre = nombre
        self.dni = dni
        self.nac = nac
        self.equipaje={}
        self.total_equipaje_cantidad= 0
        self.total_en_kilos=0
        self.h_vuelos = []


    def __str__(self):
      return f'Nombre: {self.nombre} \nDNI: {self.dni} \nNac:{self.nac} \n Equipaje: {self.total_equipaje_cantidad} cantidad'


    def sumatotal_cantidad(self):
      '''funcion que suma los valores del diccionario sirve para que cada vez que se agregue un equipaje la variable total cantidad se actualice'''
      total=sum(self.equipaje.values())
      return total


    def agregar_equipaje(self,tipo,cantidad):
      # verificamos que el tipo de equipaje sea válido
        if tipo not in ("De mano", "De cabina", "De bodega"):
            print("Tipo de equipaje incorrecto.")
            return

        # calculamos el total si se agrega el nuevo peso
        nuevo_total = self.total_equipaje_cantidad + cantidad

        if nuevo_total > 10:
            print("Su equipaje no se agregará, ha superado los 10 equipajes permitidos por pasajero.")
            return

        # si ya existe ese "tipo" de equipaje, sumamos cantidad
        if tipo in self.equipaje:
            self.equipaje[tipo] += cantidad
        else:
            self.equipaje[tipo] = cantidad

        # actualizamos el total
        self.total_equipaje_cantidad = self.sumatotal_cantidad()


    def total_kilos(self):
      de_mano = 5
      de_cabina = 10
      de_bodega = 15
      total_general=0
      for clave, valor in self.equipaje.items():
        if clave == "De mano":
          sub_total = valor * de_mano
          total_general+= sub_total
        elif clave == "De cabina":
          sub_total = valor * de_cabina
          total_general+= sub_total
        elif clave == "De bodega":
          sub_total = valor * de_bodega
          total_general+= sub_total
        print(clave, sub_total)
        self.total_en_kilos=total_general
      print("Este es el total general de kilos ", total_general)




    def eliminar_equipaje(self,tipo,cantidad):
      #verifica si el tipo esta y si los cantidad a  eliminar son menores que los que ya estan
      if tipo in self.equipaje and  self.equipaje[tipo] >= cantidad:
        self.equipaje[tipo]-=cantidad
        print("se elimino", cantidad, "cantidad del equipaje de ", tipo)
        self.total_equipaje_cantidad = self.sumatotal_cantidad()



    def Agregar_vuelo(self,vuelo):
        self.h_vuelos.append(vuelo)

    def eliminar_vuelo(self,vuelo):
      if vuelo in self.h_vuelos:
        self.h_vuelos.remove(vuelo)



p = Pasajero('matias', 30459, 'arg')

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