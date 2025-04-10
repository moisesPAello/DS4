"""Scrapper para obtener el tipo de cambio del dólar"""

import requests
from bs4 import BeautifulSoup
import os
import argparse
import json
from datetime import datetime

# Agregar esta constante al inicio del archivo
CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "data")

def crear_carpeta_datos():
    """Crea la carpeta data si no existe"""
    if not os.path.exists(CARPETA_DATOS):
        os.makedirs(CARPETA_DATOS)
        print(f"Carpeta creada: {CARPETA_DATOS}")

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
    # Crear carpeta data si no existe
    crear_carpeta_datos()
    
    # Construir rutas completas para los archivos
    ruta_html = os.path.join(CARPETA_DATOS, archivo_salida)
    ruta_json = os.path.join(CARPETA_DATOS, archivo_salida.replace('.html', '.json'))
    
    if not os.path.exists(ruta_html):
        respuesta = obtener_pagina(url)
        guardar_html(respuesta, ruta_html)
    else:
        print(f"El archivo {ruta_html} ya existe. Usando versión guardada.")
        with open(ruta_html, 'rb') as archivo:
            respuesta = requests.Response()
            respuesta._content = archivo.read()

    sopa = BeautifulSoup(respuesta.content, 'html.parser')
    datos_dolar = extraer_tipos_cambio(sopa)
    
    # Agregar fecha y hora de la consulta
    datos_dolar['fecha_consulta'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(ruta_json, 'w', encoding='utf8') as archivo:
        json.dump(datos_dolar, archivo, indent=2, ensure_ascii=False)
    print(f"Datos guardados en {ruta_json}")

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