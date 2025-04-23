import csv
import os

def leer_csv(ruta_archivo: str) -> list[dict[str, str]]:
    """Lee un archivo CSV y devuelve una lista de diccionarios con frases y autores"""
    try:
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo_csv:
            lector = csv.reader(archivo_csv)
            frases = []
            for fila in lector:
                if len(fila) >= 2:
                    frases.append({
                        'frase': fila[0].strip('"'),
                        'autor': fila[1].strip('"')
                    })
            return frases
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        return []

def obtener_frases(frases: list[dict[str, str]]) -> list[str]:
    """Devuelve una lista con solo las frases"""
    return [frase['frase'] for frase in frases]

def imprimir_frases(frases: list[str]) -> None:
    """Imprime las frases en un formato legible
    
    Args:
        frases: Lista de frases a imprimir
    """
    for frase in frases:
        print(frase)

def main():
    """Función principal para ejecutar el script"""
    ruta_archivo_frases = os.path.join(os.path.dirname(__file__), 'data', 'frases.csv')
    tabla_frases = leer_csv(ruta_archivo_frases)
    frases = obtener_frases(tabla_frases)
    print("Frases de películas:")
    imprimir_frases(frases)

    ruta_archivo_frases_consolidadas = os.path.join(os.path.dirname(__file__), 'data', 'frases_consolidadas.csv')
    tabla_frases_consolidadas = leer_csv(ruta_archivo_frases_consolidadas)
    frases_consolidadas = obtener_frases(tabla_frases_consolidadas)
    print("\nFrases consolidadas:")
    imprimir_frases(frases_consolidadas)

if __name__ == '__main__':
    main()