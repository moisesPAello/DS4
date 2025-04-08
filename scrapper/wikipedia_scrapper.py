"""
Scrapper para wikipedia
"""
import requests
from bs4 import BeautifulSoup
import os
import argparse

def scrap(url:str):
    """Obtiene pagina desde internet"""
    pagina = requests.get(url,timeout=10)
    if pagina.status_code != 200:
        raise Exception(f"Error al obtener la pagina {url}: {pagina.status_code}")
    return pagina

def guardar_pagina(pagina, nombre_archivo:str):
    """Guarda la pagina en un archivo"""
    with open(nombre_archivo, 'wb') as f:
        f.write(pagina.contente)
    print(f"Pagina guardada en {nombre_archivo}")

def main(url:str, archivo_salida:str):
    """Funcion principal"""
    if not os.path.exists(archivo_salida):
        pagina = scrap(url)
        guardar_pagina(pagina, archivo_salida)
    else:
        print(f"El archivo {archivo_salida} ya existe. No se descargara nuevamente.")
        with open(archivo_salida, 'rb') as f:
            contenido = f.read()
    soup = BeautifulSoup(pagina.content, 'html.parser')
    main_content = soup.find('div', class_='mw-body-content')
    if main_content:
        lis = main_content.find_all('li')
        diccionario_lis = {}
        print(f"Se encontraron {len(lis)} elementos <li> en la pagina")
        for li in lis:
            if li.a is not None:
                diccionario_lis[li.a.text.strip()] = li.a['href']
        lista = [{'pelicula':k, 'link':v} for k,v in diccionario_lis.items()]
        print(lista)
        archivo_salida = archivo_salida.replace('.html', '.json')
        with open(archivo_salida, 'w', encoding='utf8') as f:
            f.write(str(lista))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrapper para wikipedia')
    parser.add_argument('--url', type=str, required=True, help='URL de la pagina a scrapear')
    parser.add_argument('--output', type=str, required=True, help='Nombre del archivo de salida', default='wiki.html')
    args = parser.parse_args()
    url = args.url
    output = args.output
    if not url:
        url = 'https://es.wikipedia.org/wiki/Anexo:Pel%C3%ADculas_de_ciencia_ficci%C3%B3n#1955'
    if not output:
        output = 'wiki.html'
    
    main(args.url, args.archivo_salida)