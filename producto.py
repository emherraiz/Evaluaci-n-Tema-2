'''Esta es la solución al ejercicio 2

Returns:
    class: Producto
'''
class Producto():
    '''_summary_ = 'Clase que representa un producto' '''

    def __init__(self, codigo, nombre, precio):
        '''Constructor de la clase alumno

        Args:
            codigo (int): Codigo del producto
            nombre (string): Nombre del alumno
            nota (float): Nota del alumno
        '''

        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        '''_summary_ = 'Funcion que nos devuelve el nombre del producto'

        Returns:
            string: Devuelve un string con el nombre, el codigo y el precio del producto
        '''
        return f'El producto {self.nombre} con codigo {self.codigo} tiene un precio de {self.precio}'
