from vuelo import Vuelo
from reserva import Reserva
from pasajero import Pasajero, ArbolPasajeros, cargar_pasajeros_csv
import os

# ===============================
#   CLASE DEL MENÚ (igual que antes)
# ===============================
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


# ===============================
#   OBJETOS GLOBALES DE TRABAJO
# ===============================
arbol_pasajeros = ArbolPasajeros()
vuelos = []
reservas = []


# ===============================
#   FUNCIONES DE ACCIÓN
# ===============================
def crear_pasajero():
    dni = int(input("DNI: "))
    nombre = input("Nombre y apellido: ")
    nac = input("Nacionalidad: ")
    pasajero = Pasajero(dni, nombre, nac)
    arbol_pasajeros.insertar(pasajero)
    print("✅ Pasajero creado e insertado en el árbol.")


def listar_pasajeros():
    print("\n--- LISTADO DE PASAJEROS ---")
    arbol_pasajeros.mostrar_inorden()
"""
def menu_cargar_csv():
    os.system("cls" if os.name == "nt" else "clear")
    print("=== CARGAR PASAJEROS DESDE CSV ===")
    ruta = input("Ingrese la ruta completa del archivo CSV: ")
    try:
        cargar_pasajeros_csv(ruta, arbol_pasajeros)
        print("\n✅ Archivo cargado correctamente.")
    except Exception as e:
        print(f"\n❌ Error al cargar el archivo: {e}")
    input("Presione Enter para continuar...")
"""
def crear_vuelo():
    codigo = input("Código del vuelo: ")
    origen = input("Origen: ")
    destino = input("Destino: ")
    fecha = input("Fecha (dd/mm/aaaa): ")
    vuelo = Vuelo(codigo, origen, destino, fecha)
    vuelos.append(vuelo)
    print("✅ Vuelo creado.")


def listar_vuelos():
    print("\n--- LISTADO DE VUELOS ---")
    if not vuelos:
        print("No hay vuelos registrados.")
        return
    for v in vuelos:
        print(v)
        print("-" * 30)


def reservar_vuelo():
    dni = int(input("DNI del pasajero: "))
    pasajero = arbol_pasajeros.buscar(dni)
    if not pasajero:
        print("❌ Pasajero no encontrado.")
        return

    if not vuelos:
        print("❌ No hay vuelos disponibles.")
        return

    print("\nVuelos disponibles:")
    for i, v in enumerate(vuelos, 1):
        print(f"{i}. {v.codigo} - {v.origen} → {v.destino} ({v.fecha})")

    opcion = int(input("Seleccione vuelo: ")) - 1
    vuelo = vuelos[opcion]
    vuelo.agregar_pasajero(pasajero)
    reserva = Reserva(pasajero, vuelo)
    reservas.append(reserva)
    print(f"✅ Reserva creada. Código: {reserva.codigo}")


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
        print("❌ Pasajero no encontrado.")
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
            print("⚠️ Opción inválida.")
            continue

        if opc == 0:
            break

        tipos = {1: "De mano", 2: "De cabina", 3: "De bodega"}
        if opc not in tipos:
            print("❌ Opción inválida.")
            continue

        bulto = tipos[opc]
        try:
            cant_bulto = int(input("Ingrese la cantidad de bultos: "))
        except ValueError:
            print("⚠️ Cantidad inválida.")
            continue

        pasajero.agregar_equipaje(bulto, cant_bulto)
        print(f"✅ Equipaje '{bulto}' agregado correctamente. Total: {pasajero.total_equipaje_cantidad}")
        input("Presione Enter para continuar...")

# ===============================
#   CONSTRUCCIÓN DEL ÁRBOL
# ===============================
menu_principal = NodoMenu("MENÚ PRINCIPAL")

# Submenú PASAJEROS
pasajeros = NodoMenu("Gestión de pasajeros")
pasajeros.agregar_submenu(NodoMenu("Crear pasajero", crear_pasajero))
pasajeros.agregar_submenu(NodoMenu("Listar pasajeros", listar_pasajeros))

# submenu de equipaje
equipaje = NodoMenu("Gestión de Equipaje")
equipaje.agregar_submenu(NodoMenu("Agregar equipaje a pasajero", menu_equipaje))


# Submenú VUELOS
vuelos_menu = NodoMenu("Gestión de vuelos")
vuelos_menu.agregar_submenu(NodoMenu("Crear vuelo", crear_vuelo))
vuelos_menu.agregar_submenu(NodoMenu("Listar vuelos", listar_vuelos))

# Submenú RESERVAS
reservas_menu = NodoMenu("Gestión de reservas")
reservas_menu.agregar_submenu(NodoMenu("Crear reserva", reservar_vuelo))
reservas_menu.agregar_submenu(NodoMenu("Listar reservas", listar_reservas))

# Armar árbol principal
menu_principal.agregar_submenu(pasajeros)
menu_principal.agregar_submenu(equipaje)
menu_principal.agregar_submenu(vuelos_menu)
menu_principal.agregar_submenu(reservas_menu)

# ===============================
#   EJECUTAR MENÚ
# ===============================
def iniciar_menu(arbol):
    global arbol_pasajeros
    arbol_pasajeros = arbol
    menu_principal.ejecutar()