import Levenshtein

def test_string_similarity(str1: str, str2: str, test_name: str = "") -> None:
    """Ejecuta pruebas completas de similitud entre dos cadenas
    
    Args:
        str1: Primera cadena a comparar
        str2: Segunda cadena a comparar
        test_name: Nombre identificador de la prueba
    """
    print(f"\nPrueba: {test_name}")
    print("-" * 50)
    print(f"Cadena 1: {str1}")
    print(f"Cadena 2: {str2}")
    
    # Distancia de Levenshtein
    distance = Levenshtein.distance(str1, str2)
    print(f"Distancia de Levenshtein: {distance}")
    
    # Ratio de similitud
    ratio = Levenshtein.ratio(str1, str2)
    print(f"Ratio de similitud: {ratio:.2f}")
    
    # Ratio de similitud por conjuntos
    set_ratio = Levenshtein.setratio(str1, str2)
    print(f"Ratio de similitud (set): {set_ratio:.2f}")
    
    try:
        # Distancia de Hamming (solo para cadenas de igual longitud)
        if len(str1) == len(str2):
            hamming = Levenshtein.hamming(str1, str2)
            print(f"Distancia de Hamming: {hamming}")
        else:
            print("Distancia de Hamming: No aplicable (longitudes diferentes)")
    except Exception as e:
        print(f"Error al calcular distancia Hamming: {str(e)}")

def main():
    """Ejecuta una serie de pruebas con diferentes tipos de cadenas"""
    # Prueba 1: Cadenas similares
    test_string_similarity(
        "Hola, ¿cómo estás?",
        "Hola, ¿cómo te va?",
        "Frases similares"
    )
    
    # Prueba 2: Cadenas idénticas
    test_string_similarity(
        "La vida es bella",
        "La vida es bella",
        "Frases idénticas"
    )
    
    # Prueba 3: Cadenas completamente diferentes
    test_string_similarity(
        "Buenos días",
        "Hasta luego",
        "Frases diferentes"
    )
    
    # Prueba 4: Una cadena vacía
    test_string_similarity(
        "Hola mundo",
        "",
        "Comparación con cadena vacía"
    )
    
    # Prueba 5: Cadenas con números y símbolos
    test_string_similarity(
        "User123!@#",
        "User124!@#",
        "Cadenas con caracteres especiales"
    )
    
    # Prueba 6: Cadenas con mayúsculas y minúsculas
    test_string_similarity(
        "Python Programming",
        "python programming",
        "Sensibilidad a mayúsculas/minúsculas"
    )

if __name__ == '__main__':
    main()
