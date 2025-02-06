"""
Este archivo es el punto de entrada a la aplicacion.
Aqui se importan las funciones de tablero.py y se ejecutan.
"""
import tablero

def main():
    """Funcion principal"""
    X = {"Ganador":0, "Perdedor":0, "Empate":0} 
    O = {"Ganador":0, "Perdedor":0, "Empate":0}
    score = {"X":X, "O":O}
    numeros = [str(i) for i in range(1, 10)]
    
    corriendo = True
    while corriendo:
        diccionario = {numero: numero for numero in numeros}
        ganador = tablero.juego(diccionario)
        tablero.actualiza_score(score, ganador)
        tablero.mostrar_score(score)
        respuesta = input("¿Desea jugar otra vez? (s/n): ")
        while respuesta.lower() not in ['s', 'n']:
            respuesta = input("Respuesta no válida. ¿Desea jugar otra vez? (s/n): ")
        if respuesta.lower() == 'n':
            corriendo = False

if __name__ == '__main__':
    main()
