"""Scrapper para obtener el tipo de cambio del dólar"""

import requests
from bs4 import BeautifulSoup
import os
import argparse
import json

def obtener_pagina(url: str):
    """Obtiene la página web desde internet"""
    respuesta = requests.get(url, timeout=10)
    if respuesta.status_code != 200:
        raise Exception(f"Error al obtener la página {url}: {respuesta.status_code}")
    return respuesta

def guardar_html(respuesta, nombre_archivo: str):
    """Guarda el contenido HTML en un archivo"""
    with open(nombre_archivo, 'wb') as archivo:
        archivo.write(respuesta.content)
    print(f"Página guardada en {nombre_archivo}")

def extraer_tipos_cambio(sopa):
    """Extrae las tasas de cambio del dólar de la página"""
    tipo_cambio = sopa.select_one("h1 strong span.xTimes")
    precio_compra = sopa.select_one(".exchangeRate p:first-child span.xTimes")
    precio_venta = sopa.select_one(".exchangeRate p:last-child span.xTimes")
    
    tabla_bancos = sopa.select("#dllsTable tbody tr")
    
    datos = {
        'tipo_cambio': float(tipo_cambio.text.strip()) if tipo_cambio else None,
        'precio_compra': float(precio_compra.text.strip()) if precio_compra else None,
        'precio_venta': float(precio_venta.text.strip()) if precio_venta else None,
        'precios_bancos': []
    }
    
    for fila in tabla_bancos:
        nombre_banco = fila.select_one('td:first-child').text.strip()
        precios = fila.select('td.xTimes')
        if precios:
            datos['precios_bancos'].append({
                'banco': nombre_banco,
                'compra': float(precios[0].text.strip()) if len(precios) > 0 else None,
                'venta': float(precios[1].text.strip()) if len(precios) > 1 else None
            })
    
    return datos

def main(url: str, archivo_salida: str):
    """Función principal del programa"""
    if not os.path.exists(archivo_salida):
        respuesta = obtener_pagina(url)
        guardar_html(respuesta, archivo_salida)
    else:
        print(f"El archivo {archivo_salida} ya existe. Usando versión guardada.")
        with open(archivo_salida, 'rb') as archivo:
            respuesta = requests.Response()
            respuesta._content = archivo.read()

    sopa = BeautifulSoup(respuesta.content, 'html.parser')
    datos_dolar = extraer_tipos_cambio(sopa)
    
    # Guardar en formato JSON
    archivo_json = archivo_salida.replace('.html', '.json')
    with open(archivo_json, 'w', encoding='utf8') as archivo:
        json.dump(datos_dolar, archivo, indent=2, ensure_ascii=False)
    print(f"Datos guardados en {archivo_json}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrapper para el tipo de cambio del dólar')
    parser.add_argument('--url', type=str, 
                       default='https://www.eldolar.info/es-MX/mexico/dia/hoy', 
                       help='URL de la página a analizar')
    parser.add_argument('--output', type=str, 
                       default='dolar.html',
                       help='Nombre del archivo de salida')
    args = parser.parse_args()
    
    main(args.url, args.output)