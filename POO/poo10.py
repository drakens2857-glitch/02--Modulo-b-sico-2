class Singleton:
    _instancia = None
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia


class FactoryVehiculo:
    @staticmethod
    def crear(tipo, marca):
        if tipo == "auto":
            return Auto(marca)
        if tipo == "moto":
            return Motocicleta(marca)
        return None


class Observer:
    def __init__(self):
        self._suscriptores = []

    def suscribir(self, s):
        self._suscriptores.append(s)

    def notificar(self, mensaje):
        for s in self._suscriptores:
            s.actualizar(mensaje)


class Suscriptor:
    def actualizar(self, mensaje):
        print(f"Notificación recibida: {mensaje}")


class Strategy:
    def __init__(self, algoritmo):
        self.algoritmo = algoritmo

    def ejecutar(self, datos):
        return self.algoritmo(datos)


def algoritmo_a(datos):
    return sum(datos)


def algoritmo_b(datos):
    return max(datos)
