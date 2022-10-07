
'''Script del ejercicio 1

Returns:
    class: Alumnos
'''
class Alumno():
    '''Esta es la clase alumno la cual nos vale para crear objetos de tipo alumno
    '''
    def __init__(self, nombre, nota):
        '''Constructor de la clase alumno

        Args:
            nombre (string): Nombre del alumno
            nota (float): Nota del alumno
        '''
        self.nombre = nombre
        self.nota = nota

    def aprobado(self):
        '''Funcion que nos dice si el alumno esta aprobado o no
        '''
        if self.nota >= 5:
            return True
        else:
            return False

    def __str__(self):
        return f'El alumno {self.nombre} tiene una nota de {self.nota}'

