'''
Funciones auxiliares para el programa "linea"
'''


def calcular_y(x, m, b):
    '''
        Calcula "y" de a cuerdo a la pendiente "m" y 
        el punto de interseccion en y "b"
        Retorna el valor de "y"
    '''
    return m * x + b


if __name__ == "__main__":
    x = 0
    m = 8
    b = 2
    y = calcular_y(x, m, b)
    print(y)
    if y == 2:
        print("Pruba exitosa")
    else:
        print("Error")
