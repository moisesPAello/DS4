import json
from datetime import datetime
import os

# Definir la ruta de los datos
CARPETA_DATOS = os.path.join(os.path.dirname(__file__), "data")

def cargar_datos(archivo: str):
    """Carga los datos del archivo JSON"""
    ruta_archivo = os.path.join(CARPETA_DATOS, archivo)
    with open(ruta_archivo, 'r', encoding='utf8') as f:
        return json.load(f)

def mostrar_resumen(datos: dict):
    """Muestra el resumen del tipo de cambio"""
    print("\n=== MONITOR DE TIPO DE CAMBIO MXN/USD ===")
    print("=" * 40)
    print(f"Tipo de Cambio: ${datos['tipo_cambio']:.2f}")
    print(f"Precio Compra: ${datos['precio_compra']:.2f}")
    print(f"Precio Venta:  ${datos['precio_venta']:.2f}")
    print("=" * 40)

def mostrar_tabla_bancos(datos: dict):
    """Muestra la tabla de precios por banco"""
    print("\n=== PRECIOS POR BANCO ===")
    print("-" * 50)
    print(f"{'Banco':<20} {'Compra':>10} {'Venta':>10}")
    print("-" * 50)
    
    for banco in datos['precios_bancos']:
        nombre = banco['banco'][:20]
        compra = f"${banco['compra']:.2f}" if banco['compra'] else "N/A"
        venta = f"${banco['venta']:.2f}" if banco['venta'] else "N/A"
        print(f"{nombre:<20} {compra:>10} {venta:>10}")
    print("-" * 50)

def analizar_mejores_opciones(datos: dict):
    """Analiza y muestra las mejores opciones para compra/venta"""
    bancos = datos['precios_bancos']
    
    # Filtrar bancos con datos válidos
    bancos_validos = [b for b in bancos if b['compra'] and b['venta']]
    
    if not bancos_validos:
        print("\nNo hay suficientes datos para hacer recomendaciones")
        return
    
    # Encontrar mejor banco para comprar dólares (precio más bajo)
    mejor_compra = min(bancos_validos, key=lambda x: x['venta'])
    
    # Encontrar mejor banco para vender dólares (precio más alto)
    mejor_venta = max(bancos_validos, key=lambda x: x['compra'])
    
    print("\n=== RECOMENDACIONES ===")
    print("=" * 50)
    print("Para COMPRAR dólares:")
    print(f"👉 {mejor_compra['banco']:<20} ${mejor_compra['venta']:.2f}")
    print(f"   Ahorras hasta ${max(b['venta'] for b in bancos_validos) - mejor_compra['venta']:.2f} por dólar")
    
    print("\nPara VENDER dólares:")
    print(f"👉 {mejor_venta['banco']:<20} ${mejor_venta['compra']:.2f}")
    print(f"   Ganas hasta ${mejor_venta['compra'] - min(b['compra'] for b in bancos_validos):.2f} por dólar")
    print("=" * 50)

def main():
    """Función principal"""
    try:
        datos = cargar_datos('dolar.json')
        mostrar_resumen(datos)
        mostrar_tabla_bancos(datos)
        analizar_mejores_opciones(datos)
        
        if 'fecha_consulta' in datos:
            print(f"\nÚltima actualización: {datos['fecha_consulta']}")
        
    except FileNotFoundError:
        print("Error: No se encontró el archivo dolar.json")
        print("Ejecuta primero el scrapper para obtener los datos.")
    except json.JSONDecodeError:
        print("Error: El archivo JSON está mal formado")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()