#Programa principal del juego del ahorcado

import argparse
import os
import string
import unicodedata
from random import choice
import funciones as fn

def main(archivo_texto:str, nombre_plantilla = 'plantilla'):
    #Programa orincipal del juego del ahorcado
    
    #Cargamos las plntillas
    plantillas =fn.carga_pantillas(nombre_plantilla)
    
    #Cargamos la oraciones
    oraciones = fn.carga_archivo_texto(archivo_texto)
    
    #Obtenemos las palabras
    palabras = fn.obten_palabras(oraciones)
    oportunidades = 5      #5 oprtunidades de fallar
    palabra_random = choice(palabras)  #Elegimos una palabra al azar 
    abecedario = {letra:letra for letra in string.ascii_lowercase}
    adivinadas = set()
    
    while oportunidades > 0:
        fn.despliega_plantilla(plantillas, oportunidades)
        oportunidades = fn.adivina_letra(abecedario, palabra_random, adivinadas, oportunidades)
     
        if palabra_random == ''.join([letra if letra in adivinadas else '_' for letra in palabra_random]):
            print("Felicidades adivinaste la palabra")     
            break
        
    fn.despliega_plantilla(plantillas, oportunidades)
    print(f"La palabra era: ", {palabra_random})    
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Juego del ahorcado")
    archivo = './datos/pg15532.txt'
    parser.add_argument("-a", "--archivo", help = "Archivo de texto con palabras a adivinar", default = "./datos/pg15532.txt")
    args = parser.parse_args()
    archivo = args.archivo
    if os.stat(archivo) is False:
        print(f"El archivo {archivo} no existe")
    else:
        main(archivo)


