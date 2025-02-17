"""
Funciones auxiliares del juego Ahorcado
"""

import os
import string
import unicodedata
from random import choice

# Función para cargar un archivo de texto
def carga_archivo_texto(archivo:str)->list:
    '''Carga un archivo de texto y regresa una lista con las palabras'''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

# Función para obtener las palabras del texto
def obten_palabras(lista: list)->list:
    #Obtiene las palabras de un texto
    texto = ' '.join(lista[120:])
    palabras = texto.split()
    
    #Convertimos a minusculas
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    
    #Removemos signos de puntuación y caracteres especiales
    set_palabras = {palabra.strip(string.punctuation) for palabra in set_palabras}
    
    #Removemos números, parentesis, corchetes y otros caracteres
    set_palabras = {palabra for palabra in set_palabras if palabra.isalpha()}

    #Removemos acentos    
    set_palabras = {unicodedata.normalize('NFKD', palabra).encode('ascii', 'ignore').decode('ascii') for palabra in set_palabras}
    
    return list(set_palabras)

# Función para cargar plantillas
def carga_pantillas(nombre_plantilla:str)->dict:
    '''Carga una plantilla y regresa una lista con las palabras'''
    plantillas = {}
    for i in range(5):
        plantillas[i] = carga_archivo_texto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

# Función para desplegar una plantilla
def despliega_plantilla(diccionario:list, nivel:int):
    '''Despliega una plantilla del juego'''
    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)

# Función para adivinar una letra
def adivina_letra(abc:dict, palabra:str, letras_adivinadas:set, oportunidades:int)->int:
    #Adivina una letra de una palabra
    
    palabra_oculta = ""
    
    for letra in palabra:
        if letra in letras_adivinadas:
            palabra_oculta += letra
        else:
            palabra_oculta += "_"
    print(f"Tienes {oportunidades} oportunidades de fallar")
    abcd = ' '.join(abc.values())
    print(f"El abecesario es {abcd}")
    print(f"La palabra es {palabra_oculta}")  
        
    letra = input('Ingresa una letra: ')
    letra = letra.lower()
    if letra in abc:
        if abc[letra] == "*":
            print('Ya adivianaste esa letra')
        else:
            abc[letra] = "*"
            if letra in palabra:
                letras_adivinadas.add(letra)
            else:
                oportunidades -= 1
    return oportunidades


# Código principal
if __name__ == '__main__':
    #Imprime las plantillas
    plantillas = carga_pantillas('plantilla')
    despliega_plantilla(plantillas, 4)

    #Imprime las palabras
    lista_oraciones = carga_archivo_texto('./datos/pg15532s.txt')
    lista_palabras = obtiene_palabras(lista_oraciones)
    print(len(lista_palabras))
    random = choice(lista_palabras)
    print(random)
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    oportunidades = 5
    t = adivina_letra(abcdario, random, adivinadas, oportunidades)
    print(t)







