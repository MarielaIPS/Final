import os
import csv
import random
import string
from grafos_vuelos import vuelos, grafo, dijkstra, obtener_ruta, mostrar_aeropuertos
from app_context import arbol_pasajeros
from pasajero import Pasajero
from vuelo import Vuelo

class Reserva:
    def __init__(self,  pasajero, vuelo):
        self.codigo = self.set_codigo() 
        self.paquete = self.set_paquete()
        self.pasajero = pasajero
        self.vuelo = vuelo

    def set_paquete(self):
        letras = ''.join(random.choices(string.ascii_uppercase, k=2))
        numeros = ''.join(random.choices(string.digits, k=3))
        return f"PK{letras}{numeros}"

    def set_codigo(self):
        caracteres = string.ascii_letters + string.digits
        codigo_lista = [random.choice(caracteres) for _ in range(3)]
        codigo_aleatorio = "".join(codigo_lista)
        return codigo_aleatorio
  
    def __str__(self):
        return (f"Paquete: {self.paquete}\nReserva: {self.codigo}\nCódigo vuelo: {self.vuelo.codigo}\nPasajero: {self.pasajero.nombre} ({self.pasajero.dni})\nVuelo: {self.vuelo.origen} → {self.vuelo.destino}")
    
# Lista global de reservas
reservas = []

def reservar_vuelo():
    dni = int(input("Ingrese DNI del pasajero: "))
    pasajero = arbol_pasajeros.buscar(dni)
    if not pasajero:
        print("Pasajero no encontrado.")
        return

    # Mostrar aeropuertos disponibles (enumerados)
    aeropuertos = sorted(grafo.keys())
    mostrar_aeropuertos()

    try:
        print ("Ingrese los numeros de orden de los aeropuertos")
        num_origen = int(input("Ingrese el número del aeropuerto de origen: "))
        num_destino = int(input("Ingrese el número del aeropuerto de destino: "))

        # Convertir números a nombres
        origen = aeropuertos[num_origen - 1]
        destino = aeropuertos[num_destino - 1]

    except (ValueError, IndexError):
        print("Opción inválida. Intente nuevamente.")
        input("Presione ENTER para continuar...")
        return


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
    
   
    minutos = duracion_total[destino]
    horas = minutos // 60
    minutos_restantes = minutos % 60
    print("\nRuta encontrada:", " ->".join(ruta), f"\nDuracion: {horas}h {minutos_restantes:02d}m")
    print("- "*35)

    paquete = Reserva(None, None).set_paquete()
# Crear reservas por tramo
    for i in range(len(ruta) - 1):
        origen_tramo = ruta[i]
        destino_tramo = ruta[i + 1]

    # Buscar el vuelo correspondiente
        vuelo = next((v for v in vuelos if v.origen == origen_tramo and v.destino == destino_tramo), None)
        if vuelo:
            vuelo.agregar_pasajero(pasajero)
            reserva = Reserva(pasajero, vuelo)
            reserva.paquete = paquete  # mismo paquete en todos los tramos
            reservas.append(reserva)
            guardar_reserva_csv(reserva)
            print(f"Reserva creada para tramo {origen_tramo} -> {destino_tramo}. Código: {reserva.codigo}")
            print("- - - ")
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
    paquetes = []
    for r in reservas_pasajero:
        if r.paquete not in paquetes:
            paquetes.append(r.paquete)

    print("\nPaquetes encontrados para el pasajero:")
    for i, p in enumerate(paquetes, start=1):
        # contar cantidad de tramos por paquete para mostrar info
        n_tramos = sum(1 for r in reservas_pasajero if r.paquete == p)
        print(f"{i}. {p}  (tramos: {n_tramos})")

    try:
        sel = int(input("\nSeleccione el número del paquete a cancelar (0 para abortar): "))
    except ValueError:
        print("Entrada inválida.")
        input("Presione ENTER para continuar...")
        return

    if sel == 0:
        print("Cancelación abortada.")
        input("Presione ENTER para continuar...")
        return

    if sel < 1 or sel > len(paquetes):
        print("Selección fuera de rango.")
        input("Presione ENTER para continuar...")
        return

    paquete_seleccionado = paquetes[sel - 1]
# Confirmación
    confirm = input(f"¿Confirma cancelar TODO el paquete {paquete_seleccionado}? (s/n): ").lower()
    if confirm != "s":
        print("Cancelación abortada.")
        input("Presione ENTER para continuar...")
        return

    # Eliminar en memoria: todas las reservas con ese paquete
    reservas_a_eliminar = [r for r in reservas if r.paquete == paquete_seleccionado and r.pasajero.dni == dni]

    for r in reservas_a_eliminar:
        # Quitar pasajero solo de ese vuelo
        if pasajero in r.vuelo._pasajeros:
            try:
                r.vuelo._pasajeros.remove(pasajero)
            except ValueError:
                pass
        # eliminar reserva de la lista global si está presente
        if r in reservas:
            reservas.remove(r)

    # Eliminar del archivo CSV todas las filas con ese paquete
    eliminar_paquete_csv(paquete_seleccionado)

    print(f"Se cancelaron {len(reservas_a_eliminar)} reservas del paquete {paquete_seleccionado} para el pasajero {pasajero.nombre}.")
    input("Presione ENTER para continuar...")

def guardar_reserva_csv(reserva, ruta="reservas.csv"):
    archivo_existe = os.path.isfile(ruta)
    with open(ruta, mode="a", newline='', encoding="utf-8") as archivo:
        campos = ["Paquete", "Código", "Vuelo", "Pasajero", "DNI", "Origen", "Destino"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        if not archivo_existe:
            writer.writeheader()
        writer.writerow({
            "Paquete": reserva.paquete,
            "Código": reserva.codigo,
            "Vuelo": reserva.vuelo.codigo,
            "Pasajero": reserva.pasajero.nombre,
            "DNI": reserva.pasajero.dni,
            "Origen": reserva.vuelo.origen,
            "Destino": reserva.vuelo.destino
        })

def eliminar_paquete_csv(paquete, ruta="reservas.csv"):
    
    if not os.path.exists(ruta):
        print("No existe el archivo de reservas.")
        return

    reservas_restantes = []
    eliminado = False

    with open(ruta, mode="r", newline='', encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            # Comparar exactamente con la columna 'Paquete' del CSV
            if fila.get("Paquete") != paquete:
                reservas_restantes.append(fila)
            else:
                eliminado = True

    # Reescribir el archivo sin las filas del paquete eliminado
    with open(ruta, mode="w", newline='', encoding="utf-8") as archivo:
        campos = ["Paquete", "Código", "Vuelo", "Pasajero", "DNI", "Origen", "Destino"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(reservas_restantes)

    if eliminado:
        print(f"El paquete {paquete} fue eliminado del archivo.")
    else:
        print(f"No se encontró el paquete {paquete} en el archivo.")

def cargar_reservas_csv(ruta):
    try:
        with open(ruta, newline='', encoding='utf-8') as f:
            lector = csv.reader(f)
            next(lector, None)  # salta encabezado
            for fila in lector:
                try:
                    paquete = fila[0].strip()
                    codigo = fila[1].strip()
                    vuelo = fila[2].strip()
                    nombre = fila[3].strip()
                    dni = int(fila[4].strip())
                    origen = fila[5].strip()
                    destino = fila[6].strip()

                    
                    pasajero = Pasajero(dni, nombre, "")
                    vuelo = Vuelo(origen, destino, duracion=0)

                    reserva = Reserva(pasajero, vuelo)
                    reserva.paquete = paquete
                    reserva.codigo = codigo

                    reservas.append(reserva)

                except (ValueError, IndexError) as e:
                    print(f"Error en fila: {fila} ({e})")

    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta}")