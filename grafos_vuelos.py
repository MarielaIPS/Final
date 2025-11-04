import heapq
from vuelo import Vuelo

# Se crea el grafo apartir de la lista de vuelos, se filtra los aeropuertos repetidos
def construir_grafo(vuelos):
    grafo = {}
    for vuelo in vuelos:
        if vuelo.origen not in grafo:
            grafo[vuelo.origen] = {}
        if vuelo.destino not in grafo:
            grafo[vuelo.destino] = {}
        grafo[vuelo.origen][vuelo.destino] = vuelo.duracion
    return grafo


#la funcion dijkstra se encarga de de recorrer el grafo por la ruta de menor duracion
def dijkstra(grafo, origen):
    duracion_total = {nodo: float('inf') for nodo in grafo}
    duracion_total[origen] = 0
    predecesores = {nodo: None for nodo in grafo}
    
    cola = [(0, origen)]
    
    while cola:
        duracion_actual, nodo_actual = heapq.heappop(cola)
        
        if duracion_actual > duracion_total[nodo_actual]:
            continue
        
        for vecino, duracion in grafo[nodo_actual].items():
            duracion_acumulada = duracion_actual + duracion
            if duracion_acumulada < duracion_total[vecino]:
                duracion_total[vecino] = duracion_acumulada
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola, (duracion_acumulada, vecino))
    
    return duracion_total, predecesores

#se obtiene la ruta []
def obtener_ruta(predecesores, destino):
    ruta = []
    actual = destino
    while actual is not None:
        ruta.insert(0, actual)
        actual = predecesores[actual]
    return ruta

#muestra la lista de aeropuertos apartir del grafo
def mostrar_aeropuertos():
    print("---------------------------------------\n")
    print("---Lista de aeropuertos disponibles:\n")
    for i, aeropuerto in enumerate(sorted(grafo.keys()), 1):
        print(f"{i:2d}. {aeropuerto}")
    print("---------------------------------------")


#-----------------------------------------------------------------------
vuelos = [
    # Sudamérica
    Vuelo("Buenos Aires (Ezeiza)", "Santiago de Chile", 120),
    Vuelo("Santiago de Chile", "Buenos Aires (Ezeiza)", 140),  # viento en contra
    Vuelo("Buenos Aires (Ezeiza)", "São Paulo (Guarulhos)", 160),
    Vuelo("São Paulo (Guarulhos)", "Buenos Aires (Ezeiza)", 180),
    Vuelo("Santiago de Chile", "São Paulo (Guarulhos)", 190),
    Vuelo("São Paulo (Guarulhos)", "Santiago de Chile", 210),

    # América del Sur → América del Norte
    Vuelo("Buenos Aires (Ezeiza)", "Miami (EE.UU.)", 530),   # oeste→este (más corto)
    Vuelo("Buenos Aires (Ezeiza)", "Ciudad de México", 500),  
    Vuelo("Miami (EE.UU.)", "Buenos Aires (Ezeiza)", 600),  # este→oeste (más largo)
    Vuelo("São Paulo (Guarulhos)", "Miami (EE.UU.)", 510),
    Vuelo("Miami (EE.UU.)", "São Paulo (Guarulhos)", 570),
    Vuelo("Miami (EE.UU.)", "Atlanta (EE.UU.)", 120),
    Vuelo("Atlanta (EE.UU.)", "Nueva York (JFK)", 140),

    # América → Europa
    Vuelo("Nueva York (JFK)", "Londres (Heathrow)", 400),   # oeste→este
    Vuelo("Londres (Heathrow)", "Nueva York (JFK)", 460),   # este→oeste
    Vuelo("Londres (Heathrow)", "París (Charles de Gaulle)", 70),
    Vuelo("París (Charles de Gaulle)", "Frankfurt (Alemania)", 70),
    Vuelo("Frankfurt (Alemania)", "Dubái (Emiratos Árabes Unidos)", 370),
    Vuelo("Dubái (Emiratos Árabes Unidos)", "Frankfurt (Alemania)", 410),

    # Europa → Asia
    Vuelo("Londres (Heathrow)", "Tokio (Haneda)", 670),   # oeste→este
    Vuelo("Tokio (Haneda)", "Londres (Heathrow)", 740),   # este→oeste
    Vuelo("Tokio (Haneda)", "Hong Kong (China)", 230),
    Vuelo("Hong Kong (China)", "Singapur (Changi)", 210),
    Vuelo("Singapur (Changi)", "Hong Kong (China)", 240),
    Vuelo("Singapur (Changi)", "Doha (Qatar)", 440),
    Vuelo("Doha (Qatar)", "Dubái (Emiratos Árabes Unidos)", 70),
    Vuelo("Dubái (Emiratos Árabes Unidos)", "Doha (Qatar)", 80),

    # Asia ↔ Oceanía
    Vuelo("Tokio (Haneda)", "Sídney (Australia)", 590),
    Vuelo("Sídney (Australia)", "Tokio (Haneda)", 640),

    # Asia ↔ América
    Vuelo("Tokio (Haneda)", "Los Ángeles (EE.UU.)", 530),   # oeste→este (más corto)
    Vuelo("Los Ángeles (EE.UU.)", "Tokio (Haneda)", 610),   # este→oeste (más largo)
    Vuelo("Los Ángeles (EE.UU.)", "Ciudad de México", 230),
    Vuelo("Ciudad de México", "Los Ángeles (EE.UU.)", 240),

    # África ↔ Europa
    Vuelo("Johannesburgo (Sudáfrica)", "Londres (Heathrow)", 590),
    Vuelo("Johannesburgo (Sudáfrica)", "Miami (EE.UU.)", 590),
    Vuelo("Londres (Heathrow)", "Johannesburgo (Sudáfrica)", 640),
]

# Construye el grafo
grafo = construir_grafo(vuelos)
# Ejecuta Dijkstra
duracion, predecesores = dijkstra(grafo, "Buenos Aires (Ezeiza)")

# Obtener mejor ruta 
def calcular_vuelo(destino):
    ruta = obtener_ruta(predecesores, destino)
    print("Ruta más corta:", " → ".join(ruta))
    minutos = duracion[destino]
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return print(f"Duracion total: {horas}h {minutos_restantes:02d}m")
    

# calcular_vuelo("Sídney (Australia)")
# print(grafo)

