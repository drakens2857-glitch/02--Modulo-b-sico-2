class Cuenta:
    _contador = 0

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo
        Cuenta._contador += 1

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    @classmethod
    def total_cuentas(cls):
        return cls._contador

    @staticmethod
    def validar_monto(monto):
        return isinstance(monto, (int, float)) and monto >= 0
