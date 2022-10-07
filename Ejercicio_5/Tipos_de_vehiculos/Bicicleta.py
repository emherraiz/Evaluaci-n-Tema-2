from Tipos_de_vehiculos.Vehiculo import Vehiculo
class Bicicleta(Vehiculo):
    '''Clase Bicicleta que hereda de Vehiculo

    Args:
        Vehiculo (Class): Clase Vehiculo
    '''
    def __init__(self, color, ruedas, tipo):
        '''Constructor de la clase Bicicleta'''
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        '''Devuelve el tipo de bicicleta'''
        return f'{Vehiculo.__str__(self)} Tipo {self.tipo}\n'
