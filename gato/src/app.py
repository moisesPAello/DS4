"""
Este archivo es el punto de entrada a la aplicacion.
Aqui se importan las funciones de tablero.py y se ejecutan.
"""
import tablero

def main():
    """Funcion principal"""
    numeros = [str(i) for i in range(1, 10)]
    diccionario = {numero: numero for numero in numeros}
    ganador = tablero.juego(diccionario)
    if ganador is None:
        print("Empate")
    else:
        print(f"El ganador es {ganador}")

if __name__ == '__main__':
    main()
