"""
Funciones auxiliares del juego Ahorcado
"""

import os

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

#Funcion para obtener las palabras del texto
def obtiene_palabras(lista: list) -> list:
    '''Obtiene las palabras de un texto'''
    texto = ' '.join(lista)[120:]
    palabras = texto.split()
    minusculas = [palabra.lower() for palabra in palabras]
    set_palabras = set(minusculas)
    return list(set_palabras)

# Función para cargar plantillas
def carga_pantillas(nombre_plantilla: str) -> dict:
    '''Carga una plantilla y regresa una lista con las palabras'''
    plantillas = {}
    for i in range(5):  # Cambiado a 5 para cargar solo hasta plantilla-4.txt
        archivo = f'./ahorcado/plantillas/{nombre_plantilla}-{i}.txt'
        plantillas[i] = carga_archivo_texto(archivo)
    return plantillas

# Función para desplegar una plantilla
def despliega_plantilla(diccionario: dict, nivel: int):
    '''Despliega una plantilla del juego'''
    if nivel in diccionario:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)

# Código principal
if __name__ == '__main__':
    # Imprimir el directorio actual
    print("Directorio actual:", os.getcwd())
    
    plantillas = carga_pantillas('plantilla')
    despliega_plantilla(plantillas, 4)
    lista_oraciones = carga_archivo_texto('ahorcado\datos\pg15532s.txt')
    lista_oraciones = obtiene_palabras(lista_oraciones)
    if lista_oraciones:
        print(lista_oraciones[120:150])
        texto = ' '.join(lista_oraciones[120:150])
        print(texto)








