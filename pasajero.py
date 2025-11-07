
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
