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
        if ganador is not None:
            print(f"El ganador es {ganador}")
            if ganador == "X":
                X["Ganador"] += 1
                O["Perdedor"] += 1
            elif ganador == "O":
                O["Ganador"] += 1
                X["Perdedor"] += 1
        else:
            print("Empate")
            X["Empate"] += 1
            O["Empate"] += 1
    

if __name__ == '__main__':
    main()
