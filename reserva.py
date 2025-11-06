
import random
import string
from grafos_vuelos import vuelos, grafo, dijkstra, obtener_ruta, mostrar_aeropuertos
from app_context import arbol_pasajeros

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

# Lista global de reservas
reservas = []

def reservar_vuelo():
    dni = int(input("Ingrese DNI del pasajero: "))
    pasajero = arbol_pasajeros.buscar(dni)
    if not pasajero:
        print("Pasajero no encontrado.")
        return

# Mostrar aeropuertos disponibles
    mostrar_aeropuertos()
    print ("copie y pegue los nombres correspondientes a los aeropuertos de Origen y Destino ")
    origen = input("Ingrese aeropuerto de origen: ")
    destino = input("Ingrese aeropuerto de destino: ")

# Validar aeropuertos
    if origen not in grafo or destino not in grafo:
        print("Uno de los aeropuertos no existe en el sistema.")
        return

# Ejecutar Dijkstra desde el origen
    duracion_total, predecesores = dijkstra(grafo, origen)
    ruta = obtener_ruta(predecesores, destino)

    if len(ruta) < 2:
        print("No se encontró ruta válida entre los aeropuertos.")
        return

    print("\nRuta encontrada:", " ->".join(ruta))

# Crear reservas por tramo
    for i in range(len(ruta) - 1):
        origen_tramo = ruta[i]
        destino_tramo = ruta[i + 1]

    # Buscar el vuelo correspondiente
        vuelo = next((v for v in vuelos if v.origen == origen_tramo and v.destino == destino_tramo), None)
        if vuelo:
            vuelo.agregar_pasajero(pasajero)
            reserva = Reserva(pasajero, vuelo)
            reservas.append(reserva)
            print(f"Reserva creada para tramo {origen_tramo} -> {destino_tramo}. Código: {reserva.codigo}")
        else:
            print(f"No se encontró vuelo directo entre {origen_tramo} y {destino_tramo}.")


def cancelar_reserva():
    dni = int(input("Ingrese DNI del pasajero para cancelar su reserva: "))
    pasajero = arbol_pasajeros.buscar(dni)
    if not pasajero:
        print("Pasajero no encontrado.")
        input("Presione ENTER para continuar...")
        return

# Buscar todas las reservas asociadas a ese pasajero
    reservas_pasajero = [r for r in reservas if r.pasajero.dni == dni]

    if not reservas_pasajero:
        print("No hay reservas activas para este pasajero.")
        input("Presione ENTER para continuar...")
        return

    print("\nReservas encontradas:")
    for r in reservas_pasajero:
        print(f"🔹 {r.vuelo.origen} → {r.vuelo.destino} (Código {r.codigo})")

    confirm = input("\n¿Desea cancelar TODO el paquete de viaje? (s/n): ").lower()
    if confirm != "s":
        print("Cancelación abortada.")
        input("Presione ENTER para continuar...")
        return

# Eliminar todas las reservas del pasajero
    for r in reservas_pasajero:
    # Sacar al pasajero del vuelo
        if pasajero in r.vuelo._pasajeros:
            r.vuelo._pasajeros.remove(pasajero)
        reservas.remove(r)

    print(f"Se cancelaron {len(reservas_pasajero)} reservas del pasajero {pasajero.nombre}.")
    input("Presione ENTER para continuar...")
