'''
    Archivo principal de linea
'''
import funciones

def main(m, b):
    X = [x / 10.5 for x in range(1, 101, 10)]
    Y = [funciones.calcular_y(x, m, b) for x in X]
    print("X: ", X)
    print("B: ", Y)
    print()
    coodenadas = list(zip(X, Y))
    print(coodenadas)

if __name__ == "__main__":
    main(2, 3)