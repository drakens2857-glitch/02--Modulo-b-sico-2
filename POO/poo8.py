class ListaPersonalizada:
    def __init__(self):
        self._datos = []

    def __len__(self):
        return len(self._datos)

    def __getitem__(self, indice):
        return self._datos[indice]

    def __setitem__(self, indice, valor):
        self._datos[indice] = valor

    def __iter__(self):
        self._indice = 0
        return self

    def __next__(self):
        if self._indice < len(self._datos):
            valor = self._datos[self._indice]
            self._indice += 1
            return valor
        raise StopIteration

    def agregar(self, valor):
        self._datos.append(valor)

    def generar(self):
        for d in self._datos:
            yield d
