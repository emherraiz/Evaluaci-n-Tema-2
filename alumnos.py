class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobado(self):
        if self.nota >= 5:
            return True
        else:
            return False

    def __str__(self):
        return f'El alumno {self.nombre} tiene una nota de {self.nota}'
