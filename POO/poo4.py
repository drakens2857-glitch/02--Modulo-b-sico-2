class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"{self.marca} {self.modelo} ({self.año})"

    def arrancar(self):
        return f"El vehículo {self.descripcion()} está arrancando."

    def detener(self):
        return f"El vehículo {self.descripcion()} se ha detenido."


class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas=4):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def descripcion(self):
        return f"Auto {self.marca} {self.modelo} ({self.año}) con {self.puertas} puertas"

    def tocar_bocina(self):
        return "¡Beep beep!"


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindrada):
        super().__init__(marca, modelo, año)
        self.cilindrada = cilindrada

    def descripcion(self):
        return f"Motocicleta {self.marca} {self.modelo} ({self.año}) {self.cilindrada}cc"

    def hacer_caballito(self):
        return "La motocicleta está haciendo un caballito."


class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_toneladas):
        super().__init__(marca, modelo, año)
        self.capacidad_toneladas = capacidad_toneladas

    def descripcion(self):
        return f"Camión {self.marca} {self.modelo} ({self.año}) con capacidad de {self.capacidad_toneladas} toneladas"

    def cargar(self):
        return "El camión está cargando mercancía."


# Ejemplo de herencia múltiple
class VehiculoElectrico:
    def cargar_bateria(self):
        return "La batería está cargando."


class AutoElectrico(Auto, VehiculoElectrico):
    def descripcion(self):
        return f"Auto eléctrico {self.marca} {self.modelo} ({self.año})"


# Ejemplo de uso y polimorfismo
vehiculos = [
    Auto("Toyota", "Corolla", 2022, 4),
    Motocicleta("Yamaha", "MT-07", 2021, 689),
    Camion("Volvo", "FH16", 2020, 25),
    AutoElectrico("Tesla", "Model 3", 2023)
]

for v in vehiculos:
    print(v.descripcion())
    print(v.arrancar())
    print(v.detener())
    if isinstance(v, Auto):
        print(v.tocar_bocina())
    if isinstance(v, Motocicleta):
        print(v.hacer_caballito())
    if isinstance(v, Camion):
        print(v.cargar())
    if isinstance(v, AutoElectrico):
        print(v.cargar_bateria())
    print("---")
