import csv

def leer_csv(ruta: str) -> list:
    ''' Lee un archivo csv y retorna una lista de diccionarios '''
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return [fila for fila in csv.DictReader(archivo)]
    
def crear_diccionario(libros: list, llave: str) -> dict:
    ''' Crea un diccionario a partir de una lista de diccionarios '''
    return {fila[llave]: fila for fila in libros}

def buscar_diccionario(diccionario: dict, palabra: str) -> list:
    ''' Busca una palabra en los titulos de un diccionario '''
    libros = []
    for titulo, libro in diccionario.items():
        if palabra in titulo.lower():
            libros.append(libro)
    return libros

def libros_empezando_con(coleccion_libros_por_titulo: dict, letra: str) -> dict:
    ''' Busca los libros que empiezan con la letra '''
    return {titulo: libro for titulo, libro in coleccion_libros_por_titulo.items() if titulo.lower().startswith(letra.lower())}

if __name__ == "__main__":
    archivo_csv = "booklist2000.csv"
    coleccion_libros = leer_csv(archivo_csv)

    coleccion_libros_por_titulo = crear_diccionario(coleccion_libros, 'title')
    titulo_buscar = "ring"
    libros_buscados_por_titulo = buscar_diccionario(coleccion_libros_por_titulo, titulo_buscar)
    print(libros_buscados_por_titulo)

    coleccion_libros_por_autor = crear_diccionario(coleccion_libros, 'author')
    autor_buscar = "Tolkien"
    libros_buscados_por_autor = buscar_diccionario(coleccion_libros_por_autor, autor_buscar)
    print(libros_buscados_por_autor)

    letra = "b"
    libros_empezando_con_letra = libros_empezando_con(coleccion_libros_por_titulo, letra)
    print(f"libros que empizan con {letra}: {len(libros_empezando_con_letra)}")

