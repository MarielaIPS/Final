import csv
import os
#from main import arbol

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
        return f"{self.nombre.ljust(20)} | {str(self.dni).ljust(10)} | {self.nac.ljust(15)} | {str(self.total_equipaje_cantidad).ljust(8)} | {str(self.total_en_kilos).ljust(8)}"

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
        print(clave, sub_total)
        self.total_en_kilos=total_general
      print("Este es el total general de kilos ", total_general)

class NodoArbol:
    def __init__(self, pasajero):
        self.pasajero = pasajero
        self.izq = None
        self.der = None
        self.altura = 1


class ArbolPasajeros:
    def __init__(self):
        self.raiz = None

    # -------------------------
    # Métodos utilitarios AVL
    # -------------------------
    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _balance(self, nodo):
        return self._altura(nodo.izq) - self._altura(nodo.der) if nodo else 0

    def _rotar_derecha(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        return x

    def _rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        return y

    # -------------------------
    # Inserción balanceada
    # -------------------------
    def _insertar(self, nodo, pasajero):
        if not nodo:
            return NodoArbol(pasajero)

        if pasajero.dni < nodo.pasajero.dni:
            nodo.izq = self._insertar(nodo.izq, pasajero)
        elif pasajero.dni > nodo.pasajero.dni:
            nodo.der = self._insertar(nodo.der, pasajero)
        else:
            print("DNI duplicado, no se insertó.")
            return nodo

        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
        balance = self._balance(nodo)

        # Rotaciones
        if balance > 1 and pasajero.dni < nodo.izq.pasajero.dni:
            return self._rotar_derecha(nodo)
        if balance < -1 and pasajero.dni > nodo.der.pasajero.dni:
            return self._rotar_izquierda(nodo)
        if balance > 1 and pasajero.dni > nodo.izq.pasajero.dni:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)
        if balance < -1 and pasajero.dni < nodo.der.pasajero.dni:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)

        return nodo

    def insertar(self, pasajero):
        self.raiz = self._insertar(self.raiz, pasajero)

    # -------------------------
    # Búsqueda por DNI
    # -------------------------
    def _buscar(self, nodo, dni):
        if not nodo:
            return None
        if dni == nodo.pasajero.dni:
            return nodo.pasajero
        elif dni < nodo.pasajero.dni:
            return self._buscar(nodo.izq, dni)
        else:
            return self._buscar(nodo.der, dni)

    def buscar(self, dni):
        return self._buscar(self.raiz, dni)

    # -------------------------
    # Eliminación balanceada
    # -------------------------
    def _nodo_minimo(self, nodo):
        actual = nodo
        while actual.izq:
            actual = actual.izq
        return actual

    def _eliminar(self, nodo, dni):
        if not nodo:
            return nodo

        if dni < nodo.pasajero.dni:
            nodo.izq = self._eliminar(nodo.izq, dni)
        elif dni > nodo.pasajero.dni:
            nodo.der = self._eliminar(nodo.der, dni)
        else:
            # Nodo encontrado
            if not nodo.izq:
                return nodo.der
            elif not nodo.der:
                return nodo.izq

            # Nodo con dos hijos
            sucesor = self._nodo_minimo(nodo.der)
            nodo.pasajero = sucesor.pasajero
            nodo.der = self._eliminar(nodo.der, sucesor.pasajero.dni)

        # Actualizar altura
        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
        balance = self._balance(nodo)

        # Rotaciones necesarias
        if balance > 1 and self._balance(nodo.izq) >= 0:
            return self._rotar_derecha(nodo)
        if balance > 1 and self._balance(nodo.izq) < 0:
            nodo.izq = self._rotar_izquierda(nodo.izq)
            return self._rotar_derecha(nodo)
        if balance < -1 and self._balance(nodo.der) <= 0:
            return self._rotar_izquierda(nodo)
        if balance < -1 and self._balance(nodo.der) > 0:
            nodo.der = self._rotar_derecha(nodo.der)
            return self._rotar_izquierda(nodo)

        return nodo
 
    def eliminar(self, dni):
        self.raiz = self._eliminar(self.raiz, dni)

    # -------------------------
    # Recorrido inorden (ordenado por DNI)
    # -------------------------
    def mostrar_inorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
            if nodo is None:
                print("No hay pasajeros cargados.")
                return
        # Imprimir encabezado una sola vez
        print(f"{'Nombre'.ljust(20)} | {'DNI'.ljust(10)} | {'Nacionalidad'.ljust(15)} | {'Equipaje'.ljust(8)} | {'Peso total'.ljust(8)}")
        print("-" * 70)
        self._contador =0
        self._mostrar_inorden_rec(nodo)
        print("-" * 70)
        print(f"Total de pasajeros: {self._contador}")

    def _mostrar_inorden_rec(self, nodo):
        if nodo is None:
            return
        self._mostrar_inorden_rec(nodo.izq)
        p = nodo.pasajero
        print(f"{p.nombre.ljust(20)} | {str(p.dni).ljust(10)} | {p.nac.ljust(15)} | {str(p.total_equipaje_cantidad).ljust(8)} | {str(p.total_en_kilos).ljust(8)}")
        self._contador +=1
        self._mostrar_inorden_rec(nodo.der)

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
