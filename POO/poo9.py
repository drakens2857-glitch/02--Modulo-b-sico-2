class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y)

    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar)

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y

    def __lt__(self, otro):
        return (self.x**2 + self.y**2) < (otro.x**2 + otro.y**2)

    def __gt__(self, otro):
        return (self.x**2 + self.y**2) > (otro.x**2 + otro.y**2)

    def __contains__(self, valor):
        return valor in (self.x, self.y)

    def __call__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"
