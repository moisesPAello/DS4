"""
Funciones auxiliares para el programa "linea"
"""


def calcular_y(x: float, m: float, b: float)->float:
    """
        Calcula "y" de a cuerdo a la pendiente "m" y 
        el punto de interseccion en y "b"
        Retorna el valor de "y"
    """
    return m * x + b

def test_linea():
    """
    Comprobamos calcular_y()
    """
    y = calcular_y(0.0, 2.0, 3.0)
    return y

if __name__ == "__main__":
    if test_linea() == 3.0:
        print("Test exitoso")
    else:
        print("Error")
