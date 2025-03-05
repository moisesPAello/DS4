import csv

def leer_csv(ruta: str) -> list:
    ''' Lee un archivo csv y retorna una lista de diccionarios '''
    with open(ruta, 'r', encoding='utf-8') as archivo:
        return [fila for fila in csv.DictReader(archivo)]
    
def crear_diccionario(archivo: str) -> dict:
    ''' Crea un diccionario a partir de una lista de diccionarios '''
    return {fila['nombre']: fila for fila in leer_csv(archivo)}

def crear_diccionario_titulos(lista: list) -> dict:
    ''' Crea un diccionario a partir de una lista de diccionarios '''
    return {fila['title']: fila for fila in lista}

def buscar_en_titulo(diccionario: dict, palabra: str) -> dict:
    ''' Busca una palabra en los titulos de un diccionario '''
    libros = []
    for titulo, libro in diccionario.items():
        if palabra in titulo.lower():
            libros.append(libro)
    return libros

if __name__ == "__main__":
    archivo_csv = "booklist2000.csv"
    lista_libros = leer_csv(archivo_csv)
    diccionario_libros = crear_diccionario_titulos(lista_libros)
    resultados = buscar_en_titulo(diccionario_libros, "flower")
    print(resultados)
