class Tienda():
    def __init__(self):
        self.productos = []  # Lista de tuplas: (nombre, precio)

    def agregar_productos(self, prod1, prod2, prod3):
        try:
            self.productos = []  # Limpiar lista anterior
            for prod, precio in [prod1, prod2, prod3]:
                if prod == "" or precio == "":
                    return "Todos los campos deben ser llenados"
                precio = float(precio)
                self.productos.append((prod, precio))
            return True
        except:
            return "Los precios deben ser números válidos"

    def total_normal(self):
        total = 0
        for _, precio in self.productos:
            total += precio
        return total

    def total_iva(self):
        total = self.total_normal()
        total_iva = total * 1.16  # IVA 16%
        return total_iva

    def total_descuento(self):
        total = self.total_normal()
        total_desc = total * 0.80  # 20% de descuento
        return total_desc