# Tienda de flores Eli
class Flor:
    def __init__(self, nombre, color, precio):
        self.nombre = nombre
        self.color = color
        self.precio = precio

    def mostrar_info(self):
        print(f"Flor: {self.nombre} | Color: {self.color} | Precio: ${self.precio}")
class Carrito:
    def __init__(self):
        self.flores = []

    def agregar_flor(self, flor):
        self.flores.append(flor)
        print(f"{flor.nombre} agregada al carrito.")

    def mostrar_carrito(self):
        print("\nFlores en el carrito:")
        for flor in self.flores:
            flor.mostrar_info()

    def calcular_total(self):
        total = 0
        for flor in self.flores:
            total += flor.precio
        return total
class TiendaFlores:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []

    def agregar_flor(self, flor):
        self.inventario.append(flor)

    def mostrar_inventario(self):
        print(f"\nInventario de {self.nombre}:")
        for flor in self.inventario:
            flor.mostrar_info()

# Crear tienda de flores Eli
tienda = TiendaFlores("Floristería Primavera")

# Crear tipos de flores
f1 = Flor("Rosa", "Rojo", 1.50)
f2 = Flor("Tulipán", "Rosado", 1.10)
f3 = Flor("Orquídea", "Amarilla", 4.50)

# Agregar flores al inventario
tienda.agregar_flor(f1)
tienda.agregar_flor(f2)
tienda.agregar_flor(f3)

# Mostrar inventario
tienda.mostrar_inventario()

# Crear carrito de compra
carrito = Carrito()

# Agregar flores al carrito
carrito.agregar_flor(f1)
carrito.agregar_flor(f3)

# Mostrar carrito y total
carrito.mostrar_carrito()
print(f"\nTotal a pagar: ${carrito.calcular_total()}")