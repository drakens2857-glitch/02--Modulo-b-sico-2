import json
import pickle

class GestorArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def escribir_texto(self, contenido):
        with open(self.nombre, "w", encoding="utf-8") as f:
            f.write(contenido)

    def leer_texto(self):
        with open(self.nombre, "r", encoding="utf-8") as f:
            return f.read()

    def guardar_json(self, datos):
        with open(self.nombre, "w", encoding="utf-8") as f:
            json.dump(datos, f)

    def cargar_json(self):
        with open(self.nombre, "r", encoding="utf-8") as f:
            return json.load(f)

    def guardar_pickle(self, objeto):
        with open(self.nombre, "wb") as f:
            pickle.dump(objeto, f)

    def cargar_pickle(self):
        with open(self.nombre, "rb") as f:
            return pickle.load(f)
