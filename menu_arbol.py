from reserva import Reserva, reservas, reservar_vuelo, cancelar_reserva
from pasajero import Pasajero, eliminar_pasajero_csv, agregar_pasajero_csv
from grafos_vuelos import mostrar_aeropuertos, vuelos
from app_context import arbol_pasajeros
import os


#   CLASE DEL MENÚ

class NodoMenu:
    def __init__(self, nombre, accion=None):
        self.nombre = nombre
        self.accion = accion
        self.submenus = []

    def agregar_submenu(self, submenu):
        self.submenus.append(submenu)

    def ejecutar(self):
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"\n=== {self.nombre} ===")
            for i, submenu in enumerate(self.submenus, 1):
                print(f"{i}. {submenu.nombre}")
            print("0. Volver / Salir")

            opcion = input("\nSeleccione una opción: ")

            if opcion == "0":
                break
            try:
                submenu = self.submenus[int(opcion) - 1]
                if submenu.submenus:
                    submenu.ejecutar()
                elif submenu.accion:
                    submenu.accion()
                input("\nPresione Enter para continuar...")
            except (IndexError, ValueError):
                print("Opción inválida.")


#   FUNCIONES DE ACCIÓN

def crear_pasajero():
    dni = int(input("DNI: "))
    nombre = input("Nombre y apellido: ")
    nac = input("Nacionalidad: ")
    pasajero = Pasajero(dni, nombre, nac)
    arbol_pasajeros.insertar(pasajero)
    print("--Pasajero creado e insertado en el árbol.")
    ruta = r"pasajeros.csv"
    agregar_pasajero_csv(dni, nombre, nac, ruta)

def listar_pasajeros():
    print("\n--- LISTADO DE PASAJEROS ---")
    arbol_pasajeros.mostrar_inorden()

def menu_buscar_pasajero():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== BUSCAR PASAJERO ===")
    dni = int(input("Ingrese DNI: "))
    pasajero = arbol_pasajeros.buscar(dni)
    if pasajero:
        encabezado=(f"{'Nombre'.ljust(20)} | {'DNI'.ljust(10)} | {'Nacionalidad'.ljust(15)} | {'Equipaje'.ljust(8)} | {'Peso total'.ljust(8)}")
        print("\nPasajero encontrado:\n", encabezado," \n", pasajero)
    else:
        print("\nNo se encontró ningún pasajero con ese DNI.")
    
def menu_eliminar_pasajero():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== ELIMINAR PASAJERO ===")
    dni = int(input("Ingrese DNI: "))
    arbol_pasajeros.eliminar(dni)
    print(f"\nPasajero con DNI {dni} ELIMINADO:\n")
    ruta = r"pasajeros.csv"
    eliminar_pasajero_csv(dni, ruta)

def listar_vuelos():
    print("---------------------------------------\n")
    print("---Lista de vuelos disponibles:\n")
    for i, aeropuerto in enumerate(vuelos ,1):
        print(f"{i:2d}. {aeropuerto}")
    print("---------------------------------------")

def listar_reservas():
    print("\n--- RESERVAS ---")
    if not reservas:
        print("No hay reservas registradas.")
        return
    for r in reservas:
        print(r)
        print("-" * 40)

def menu_equipaje():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== GESTIÓN DE EQUIPAJE ===")
    dni = int(input("Ingrese el DNI del pasajero: "))
    pasajero = arbol_pasajeros.buscar(dni)

    if not pasajero:
        print("Pasajero no encontrado.")
        input("Presione Enter para continuar...")
        return

    while True:
        print("\n------ AGREGAR EQUIPAJE ------")
        print("1. Equipaje de mano")
        print("2. Equipaje de cabina")
        print("3. Equipaje de bodega")
        print("0. Volver")
        print("------------------------------")

        try:
            opc = int(input("Ingrese una opción: "))
        except ValueError:
            print("Opción inválida.")
            continue

        if opc == 0:
            break

        tipos = {1: "De mano", 2: "De cabina", 3: "De bodega"}
        if opc not in tipos:
            print("Opción inválida.")
            continue

        bulto = tipos[opc]
        try:
            cant_bulto = int(input("Ingrese la cantidad de bultos: "))
        except ValueError:
            print("Cantidad inválida.")
            continue

        pasajero.agregar_equipaje(bulto, cant_bulto)
        print(f"Equipaje '{bulto}' agregado correctamente. Total: {pasajero.total_equipaje_cantidad}")
        

# Construye menú principal
menu_principal = NodoMenu("MENÚ PRINCIPAL")

# Submenú pasajeros
pasajeros = NodoMenu("Gestión de pasajeros")
pasajeros.agregar_submenu(NodoMenu("Crear pasajero", crear_pasajero))
pasajeros.agregar_submenu(NodoMenu("Listar pasajeros", listar_pasajeros))
pasajeros.agregar_submenu(NodoMenu("Eliminar pasajeros", menu_eliminar_pasajero))
pasajeros.agregar_submenu(NodoMenu("Buscar pasajero por DNI", menu_buscar_pasajero))

# Submenú equipaje
equipaje = NodoMenu("Gestión de Equipaje")
equipaje.agregar_submenu(NodoMenu("Agregar equipaje a pasajero", menu_equipaje))

# Submenú vuelos
vuelos_menu = NodoMenu("Gestión de vuelos")
vuelos_menu.agregar_submenu(NodoMenu("Listar vuelos", listar_vuelos))
vuelos_menu.agregar_submenu(NodoMenu("Listar Aeropuertos", mostrar_aeropuertos))

# Submenú reservas
reservas_menu = NodoMenu("Gestión de reservas")
reservas_menu.agregar_submenu(NodoMenu("Crear reserva", reservar_vuelo))
reservas_menu.agregar_submenu(NodoMenu("Eliminar reserva", cancelar_reserva))
reservas_menu.agregar_submenu(NodoMenu("Listar reservas", listar_reservas))

# Armar árbol principal
menu_principal.agregar_submenu(pasajeros)
menu_principal.agregar_submenu(equipaje)
menu_principal.agregar_submenu(vuelos_menu)
menu_principal.agregar_submenu(reservas_menu)

# Ejecuta menú
def iniciar_menu():
    global arbol_pasajeros
    menu_principal.ejecutar()