def catalogar(lista, ruedas = 0):
    '''Devuelve el numero de ruedas de los vehiculos de la lista

    Args:
        lista (list): Lista de vehiculos
        ruedas (int, optional): Numero de ruedas. Defaults to 0.
    '''
    if ruedas == 0:
        for i in lista:
            print(i)
    else:
        suma = 0
        for i in lista:
            if i.get_ruedas() == ruedas:
                suma +=1

        print(f'Se han encontrado {suma} vehiculos con {ruedas} ruedas')
