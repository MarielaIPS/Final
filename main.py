from pasajero import ArbolPasajeros, cargar_pasajeros_csv
from menu_arbol import iniciar_menu
import csv

if __name__ == "__main__":
    arbol = ArbolPasajeros()

    # --- Cargar datos iniciales desde CSV ---
    ruta = r"C:\Users\Davic\Documents\David\UNAB\Primer Año\2do Cuatrimestre\271 - Estructura de Datos\TP FINAL\borrador\version arbol\pasajeros.csv"
    try:
        cargar_pasajeros_csv(ruta, arbol)
        print("✅ Pasajeros cargados desde CSV")
    except FileNotFoundError:
        print("⚠️ No se encontró el archivo de pasajeros, comenzando vacío")

    
    iniciar_menu(arbol)