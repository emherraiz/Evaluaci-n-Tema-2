class Producto():
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'El producto {self.nombre} con codigo {self.codigo} tiene un precio de {self.precio}'
