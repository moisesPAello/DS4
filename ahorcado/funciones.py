"""
Funciones auxiliares del juego Ahorcado
"""

import os
import string
import unicodedata
from random import choice

# Función para cargar un archivo de texto
def carga_archivo_texto(archivo: str) -> list:
    """
    Carga un archivo de texto y lo convierte en una lista de palabras.
    :param archivo: str
    :return: list
    """
    if not os.path.exists(archivo):
        print(f"Error: El archivo {archivo} no existe.")
        return []
    
    with open(archivo, 'r', encoding="utf-8") as file:
        oraciones = file.readlines()
    return [oracion.strip() for oracion in oraciones]  # Remove newline characters

# Función para obtener las palabras del texto
def obtiene_palabras(lista_oraciones: list) -> list:
    # Crear un conjunto con palabras alfabéticas
    set_palabras = {palabra for oracion in lista_oraciones for palabra in oracion.split() if palabra.isalpha()}

    # Remover acentos
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ASCII', 'ignore').decode('utf-8') for palabra in set_palabras}

    return list(set_palabras)
    """'''Obtiene las palabras de un texto sin signos de puntuación ni caracteres especiales'''
    texto = ' '.join(lista)[120:]
    # Remover signos de puntuación, números y caracteres especiales
    caracteres_permitidos = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')
    texto = ''.join(c for c in texto if c in caracteres_permitidos)
    palabras = texto.split()
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    return list(set_palabras)"""

# Función para cargar plantillas
def carga_pantillas(nombre_plantilla: str) -> dict:
    '''Carga una plantilla y regresa una lista con las palabras'''
    plantillas = {}
    for i in range(5):  # Cambiado a 5 para cargar solo hasta plantilla-4.txt
        archivo = f'./plantillas/{nombre_plantilla}-{i}.txt'
        plantillas[i] = carga_archivo_texto(archivo)
    return plantillas

# Función para desplegar una plantilla
def despliega_plantilla(diccionario: dict, nivel: int):
    '''Despliega una plantilla del juego'''
    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)

# Función para adivinar una letra
def adivina_letra(abc: dict, palabra: str, adivinadas: list,oportunidades: int):
    """Adivina una letra en la palabra"""
    adivinadas = []
    palabra_oculta = ""
    for letra in palabra:
        if letra in adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "_"
    print(f"Tienes {oportunidades} oportunidades de fallar")
    print(f"El abecedario es: {abc}")
    print(f"La palabra es: {palabra_oculta}")
    letra = input("Ingresa una letra: ")
    letra = letra.lower()
    if letra in abc:
        if abc[letra] == "*":
            print("Ya ingresaste esa letra")
        else:
            abc[letra] = "*"
            if letra in palabra:
                adivinadas.append(letra)
            else:
                oportunidades -= 1


# Código principal
if __name__ == '__main__':
    #Imprime las plantillas
    plantillas = carga_pantillas('plantilla')
    despliega_plantilla(plantillas, 5)

    #Imprime las palabras
    lista_oraciones = carga_archivo_texto('./datos/pg15532s.txt')
    lista_palabras = obtiene_palabras(lista_oraciones)
    print(len(lista_palabras))
    random = choice(lista_palabras)
    print(random)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    oportunidades = 5
    adivina_letra(abcdario, random, adivinadas, oportunidades)







