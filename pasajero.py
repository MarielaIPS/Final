import csv
import os

class Pasajero:
    def __init__(self, dni, nombre, nac):
        self.dni = dni
        self.nombre = nombre
        self.nac = nac
        self.equipaje = {}
        self.total_equipaje_cantidad = 0
        self.total_en_kilos = 0
        self.h_vuelos = []

    def __str__(self):
        return f"{self.nombre.ljust(20)} | {str(self.dni).ljust(10)} | {self.nac.ljust(15)} | {str(self.total_equipaje_cantidad).ljust(8)} | {str(self.total_kilos()).ljust(8)}"

    def sumatotal_cantidad(self):
        return sum(self.equipaje.values())

    def agregar_equipaje(self, tipo, cantidad):
        if tipo not in ("De mano", "De cabina", "De bodega"):
            print("Tipo de equipaje incorrecto.")
            return

        nuevo_total = self.total_equipaje_cantidad + cantidad
        if nuevo_total > 10:
            print("Supera el máximo de 10 equipajes.")
            return

        self.equipaje[tipo] = self.equipaje.get(tipo, 0) + cantidad
        self.total_equipaje_cantidad = self.sumatotal_cantidad()

    def eliminar_equipaje(self, tipo, cantidad):
        if tipo in self.equipaje and self.equipaje[tipo] >= cantidad:
            self.equipaje[tipo] -= cantidad
            print(f"Eliminado {cantidad} de {tipo}")
            self.total_equipaje_cantidad = self.sumatotal_cantidad()
        else:
            print("Cantidad inválida o tipo no encontrado.")

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
            self.total_en_kilos=total_general
        return  total_general

def cargar_pasajeros_csv(ruta, arbol):
    with open(ruta, newline='', encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector)  # saltar encabezado
        for fila in lector:
            try:
                dni = int(fila[0].strip())
                nombre = fila[1].strip()
                nac = fila[2].strip()
                pasajero = Pasajero(dni, nombre, nac)
                arbol.insertar(pasajero)
            except (ValueError, IndexError):
                print(f"Fila inválida: {fila}")

def agregar_pasajero_csv(dni, nombre, nacionalidad, ruta_csv):
    existe = False
    with open(ruta_csv, newline='', encoding="utf-8") as csvfile:
        lector = csv.reader(csvfile)
        encabezado = next(lector)  # saltar encabezado
        for fila in lector:
            if str(fila[0]).strip() == str(dni).strip():
                existe = True
                break

    if existe:
        print(f"\nEl pasajero con DNI {dni} ya existe en el archivo CSV. No se agregó.\n")
        return

    # Si no existe, lo agregamos al final del archivo
    with open(ruta_csv, "a", newline='', encoding="utf-8") as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow([dni, nombre, nacionalidad])

    print(f"\nPasajero con DNI {dni} agregado correctamente al archivo CSV.\n")

def eliminar_pasajero_csv(dni, ruta_csv):
    """Elimina del archivo CSV el pasajero con el DNI indicado."""
    pasajeros_restantes = []

    with open(ruta_csv, newline='', encoding="utf-8") as csvfile:
        lector = csv.reader(csvfile)
        encabezado = next(lector)  # Leemos el encabezado

        for fila in lector:
            # fila[0] es el DNI
            if str(fila[0]).strip() != str(dni).strip():
                pasajeros_restantes.append(fila)

    # Reescribimos el archivo con los pasajeros restantes
    with open(ruta_csv, "w", newline='', encoding="utf-8") as csvfile:
        escritor = csv.writer(csvfile)
        escritor.writerow(encabezado)
        escritor.writerows(pasajeros_restantes)

    print(f"\nPasajero con DNI {dni} eliminado correctamente del archivo CSV.\n")