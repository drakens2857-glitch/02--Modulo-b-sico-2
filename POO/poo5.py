from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def __str__(self):
        return f"Círculo de radio {self.radio}"


class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f"Rectángulo {self.ancho}x{self.alto}"


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def __str__(self):
        return f"Triángulo base {self.base}, altura {self.altura}"


# Ejemplo de uso y polimorfismo
figuras = [
    Circulo(5),
    Rectangulo(4, 6),
    Triangulo(3, 8)
]

for f in figuras:
    print(f"{f}: área = {f.calcular_area():.2f}")
