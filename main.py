from pasajero import cargar_pasajeros_csv
from menu_arbol import iniciar_menu
from reserva import cargar_reservas_csv
from app_context import arbol_pasajeros

if __name__ == "__main__":
        
    # --- Cargar datos iniciales desde CSV ---
    ruta = r"pasajeros.csv"
    try:
        cargar_pasajeros_csv(ruta, arbol_pasajeros)
        print("Pasajeros cargados desde CSV")
    except FileNotFoundError:
        print("No se encontró el archivo de pasajeros, comenzando vacío")
    
    ruta2 = r"reservas.csv"
    try:
        cargar_reservas_csv(ruta2)
        print("Reservas cargadas desde CSV")
    except FileNotFoundError:
        print("No se encontró el archivo de reservas, comenzando vacío")
 
    iniciar_menu()