"""Programa principal de libros web"""
from flask import Flask, render_template, request
import funciones as fn

app = Flask(__name__)

arrchivo_csv = "booklist2000.csv"
coleccion_libros = fn.leer_csv(arrchivo_csv)
coleccion_libros_por_titulo = fn.crear_diccionario(coleccion_libros, 'title')
coleccion_libros_por_autor = fn.crear_diccionario(coleccion_libros, 'author')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/titulo', methods=['GET', 'POST'])
def buscar_titulo():
    """Página de búsqueda por título"""
    titulo_buscar = request.form['titulo']
    resultado = fn.buscar_diccionario(coleccion_libros_por_titulo, titulo_buscar)
    return render_template('resultado.html', resultado=resultado)

@app.route('/autor')
def autor():
    return "Página de búsqueda por autor"

if __name__ == "__main__":
    app.run(debug=True)