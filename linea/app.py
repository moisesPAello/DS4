"""
    Archivo principal de linea
"""
import argparse
import funciones

def main(m: float, b: float):
    """
    Funciona principal que calcula las coordenadas 
    de una linea recta
    recibimos m y b
    Regresa: nada
    """
    X = [x / 10.0 for x in range(1, 101, 5)]
    Y = [funciones.calcular_y(x, m, b) for x in X]
    print("X: ", X)
    print("B: ", Y)
    coodenadas = list(zip(X, Y))
    print(coodenadas)
    funciones.grafica_linea(X, Y, m, b)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Calcula las coordenadas de una linea recta")
    parser.add_argument("-m", type = float, help = "Pendiente", default = 3.0)
    parser.add_argument("-b", type = float, help = "Inteserccion en y", default = 3.0)
    args = parser.parse_args()
    main(args.m, args.b)
