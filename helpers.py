import os
import platform

def limpiar_pantalla():
    '''_summary_ = 'Funcion que limpia la pantalla'
    '''
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    '''_summary_ = 'Funcion que lee un texto'

    Args:
        longitud_min (int, optional): Longitud minima. Defaults to 0.
        longitud_max (int, optional): Longitud maxima. Defaults to 100.
        mensaje (string, optional): Lee el texto introducido. Defaults to None.

    Returns:
        string: En caso de no introducir texto en la función lo introduces por medio del teclado
    '''

    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
