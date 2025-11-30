class Persona:

    def __init__(self, nombre, edad, email="sin_email@ejemplo.com"):
        
        if not isinstance(nombre, str) or len(nombre.strip()) == 0:
            raise ValueError("El nombre debe ser un texto no vacío")
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un número entero positivo")

        self.nombre = nombre.strip().title()
        self.edad = edad
        self.email = email.lower()
        self._activo = True
        self.__id_interno = id(self)

    def saludar(self):
        
        return f"¡Hola! Mi nombre es {self.nombre} y tengo {self.edad} años."

    def cumplir_años(self):
        
        self.edad += 1
        return f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años."

    def cambiar_email(self, nuevo_email):
        
        if "@" not in nuevo_email or "." not in nuevo_email:
            raise ValueError("Email inválido")
        self.email = nuevo_email.lower()
        return f"Email actualizado a: {self.email}"

    def __str__(self):
        
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"

    def __repr__(self):
       
        return f"Persona('{self.nombre}', {self.edad}, '{self.email}')"

    def __eq__(self, otra_persona):
        
        if not isinstance(otra_persona, Persona):
            return False
        return self.nombre == otra_persona.nombre and self.edad == otra_persona.edad

    def __lt__(self, otra_persona):
        
        return self.edad < otra_persona.edad

    @property
    def es_mayor_edad(self):
        
        return self.edad >= 18

    @property
    def activo(self):
        
        return self._activo

    @activo.setter
    def activo(self, valor):
        
        if not isinstance(valor, bool):
            raise ValueError("El estado activo debe ser True o False")
        self._activo = valor

    @classmethod
    def desde_string(cls, datos_string):
        
        try:
            nombre, edad, email = datos_string.split(',')
            return cls(nombre.strip(), int(edad.strip()), email.strip())
        except ValueError:
            raise ValueError("Formato inválido. Use: 'Nombre,Edad,Email'")

    @staticmethod
    def es_nombre_valido(nombre):
        
        return isinstance(nombre, str) and len(nombre.strip()) > 0 and nombre.strip().isalpha()


p1 = Persona("María", 25, "maria@correo.com")
p2 = Persona.desde_string("Carlos,30,carlos@correo.com")

print(p1.saludar())
print(p1.cumplir_años())
print(p2)
print(p1 == p2)
print(p1.es_mayor_edad)
