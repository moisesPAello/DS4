""" Programa principal del juego de ahorcado """
import string
from random import choice
import unicodedata
import funciones as fn


def main(archivo_texto: str, nombre_plantilla = "plantilla"):
    """ Programa principal del juego de ahorcado """
    # Imprime las plantillas
    plantillas = fn.carga_pantillas(nombre_plantilla)

    # Cargamos palabras
    oraciones = fn.carga_archivo_texto(archivo_texto)

    # Obtenemos palabras
    palabras = fn.obtiene_palabras(oraciones)
    oportunidades = 5
    palabra_random = choice(palabras)

    # Crear abecedario
    abecedario = {letra: letra for letra in string.ascii_lowercase}
    letras_adivinadas = set()

    while oportunidades > 0:
        fn.despliega_plantilla(plantillas, oportunidades)
        fn.adivina_letra(abecedario, palabra_random, letras_adivinadas, oportunidades)

    

if __name__ == "__main__":
    archivo_texto = "./datos/pg15532s.txt"
    main(archivo_texto)



