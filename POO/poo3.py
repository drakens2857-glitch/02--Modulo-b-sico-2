class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        if not isinstance(nombre, str) or len(nombre.strip()) == 0:
            raise ValueError("El nombre debe ser un texto no vacío")
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio debe ser un número positivo")
        if not isinstance(stock, int) or stock < 0:
            raise ValueError("El stock debe ser un número entero positivo")

        self.nombre = nombre.strip().title()
        self.categoria = categoria.strip().title()
        self.precio = float(precio)
        self.stock = stock

    def actualizar_stock(self, cantidad):
        if not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un número entero")
        self.stock += cantidad
        if self.stock < 0:
            self.stock = 0

    def valor_total(self):
        return self.precio * self.stock

    def __str__(self):
        return f"{self.nombre} ({self.categoria}) - ${self.precio:.2f} | Stock: {self.stock}"


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if any(p.nombre == producto.nombre for p in self.productos):
            raise ValueError("El producto ya existe en el inventario")
        self.productos.append(producto)

    def listar_productos(self):
        return [str(p) for p in self.productos]

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if p.nombre.lower() == nombre.lower()]

    def filtrar_por_categoria(self, categoria):
        return [p for p in self.productos if p.categoria.lower() == categoria.lower()]

    def filtrar_por_precio(self, minimo, maximo):
        return [p for p in self.productos if minimo <= p.precio <= maximo]

    def eliminar_producto(self, nombre):
        for i, p in enumerate(self.productos):
            if p.nombre.lower() == nombre.lower():
                del self.productos[i]
                return True
        return False

    def reporte_inventario(self):
        return {
            "total_productos": len(self.productos),
            "valor_total": sum(p.valor_total() for p in self.productos),
            "stock_bajo": [p for p in self.productos if p.stock < 5]
        }


# Ejemplo de uso
inv = Inventario()
inv.agregar_producto(Producto("Laptop", "Tecnología", 2500, 10))
inv.agregar_producto(Producto("Mouse", "Accesorios", 50, 3))
inv.agregar_producto(Producto("Teclado", "Accesorios", 120, 7))

print(inv.listar_productos())
print(inv.buscar_por_nombre("Laptop"))
print(inv.filtrar_por_categoria("Accesorios"))
print(inv.filtrar_por_precio(50, 200))
print(inv.reporte_inventario())
