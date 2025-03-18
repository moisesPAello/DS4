"""Programa principal de libros web"""
from flask import Flask, render_template, request
import funciones as fn

app = Flask(__name__)

arrchivo_csv = "booklist2000.csv"
coleccion_libros = fn.leer_csv(arrchivo_csv)
coleccion_libros_titulo = fn.crear_diccionario(coleccion_libros, 'title')
coleccion_libros_autor = fn.crear_diccionario(coleccion_libros, 'author')
coleccion_libros_id = fn.crear_diccionario(coleccion_libros,'id')

@app.route('/')
def inicio():
    ''' Página de inicio de la aplicación '''
    return render_template('incio.html')

@app.route('/titulos', methods =['GET','POST'])
def busqueda_titulo():
    ''' Página de búsqueda por título '''
    resultado = []
    if request.method == 'POST':
        titulo = request.form['titulo']
        resultado = fn.buscar_diccionario(coleccion_libros_titulo, titulo)
        print(titulo)
        print(resultado)
    return render_template('titulo.html', coleccion_libros_titulo=resultado)

@app.route('/titulo', methods=['GET','POST'])
def title():
    '''Pagina de busqueda por titulo'''
    print(request.method)
    resultado = []
    if request.method == 'POST':
        titulo = request.form.get('serchInput', '')
        resultado = fn.buscar_diccionario(coleccion_libros_titulo, titulo)
    return render_template('titulos.html', coleccion_libros_titulo=resultado)        

@app.route('/libro/<id>', methods =['GET'])
def libro(id:str):
    ''' Página de información de un libro '''
    if id in coleccion_libros_id:
        libro = coleccion_libros_id[id]
        return render_template('libros.html', libro=libro)
    else:
        return render_template('libros.html', libro=None)
    titulo = request.args.get('id')
    libro = diccionario_id[id]
    return render_template('libros.html', libro=libro)
    

@app.route('/letra/', methods = ['GET'])
def por_letra():
    ''' Página de búsqueda por letra '''
    return render_template('letra.html', coleccion_libros = [])

@app.route('/letra/<letra>', methods = ['GET'])
def busqueda_letra(letra:str):
    ''' Página de búsqueda por letra '''
    resultado = fn.libros_empezando_con(coleccion_libros, letra)
    return render_template('letra.html', coleccion_libros=resultado)
    
if __name__ == '__main__':
    app.run(debug=True)