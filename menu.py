import os
import helpers

def iniciar():
    while True:
        helpers.limpiar_pantalla()
        print("========================")
        print('Bienvenido al examen')
        print("========================")
        print('1 - 2. Ejercicio 1')
        print('3 - 4. Ejercicio 3')
        print('5. Ejercicio 4')
        print('6. Salir')
        print("========================")

        opcion = input('> ')

        helpers.limpiar_pantalla()

        if opcion == '1' or opcion == '2':
            ejercicio1()

        elif opcion == '3' or opcion == '4':
            ejercicio3()

        elif opcion == '5':
            ejercicio5()

        else:
            break

        input('\nPresione una tecla para continuar...')
        
