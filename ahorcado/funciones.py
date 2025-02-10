"""
Funciones auxiliares del juego Ahorcado
"""

import os

def carga_archivo_texto(archivo: str) -> list:
    """
    Carga un archivo de texto y lo convierte en una lista de palabras.
    :param archivo: str
    :return: list
    """
    with open(archivo, 'r', encoding="utf-8") as file:
        oraciones = file.readlines()
    return oraciones


if __name__ == '__main__':
    # Imprimir el directorio actual
    print("Directorio actual:", os.getcwd())
    
    lista_oraciones = carga_archivo_texto('./plantillas/plantilla-0.txt')
    for elemento in lista_oraciones:
        print(elemento)