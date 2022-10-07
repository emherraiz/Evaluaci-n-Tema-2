class Producto():
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return self.nombre + " " + str(self.precio)
    def __repr__(self):
        return self.nombre + " " + str(self.precio)
