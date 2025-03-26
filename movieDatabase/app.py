"""Programa pincipal de movieDatabase"""
from flask import Flask, render_template, request, redirect, url_for
import random
import movie_clases as mc
import os

app = Flask(__name__)
sistema = mc.SistemaCine()
ruta = 'datos/movies_db - '
actores_csv = ruta + 'actores.csv'
peliculas_csv = ruta + 'peliculas.csv'
usuarios_csv = ruta + 'usuarios.csv'
relaciones_csv = ruta + 'relaciones.csv'

sistema.carga_csv(actores_csv, mc.Actor)
sistema.carga_csv(peliculas_csv, mc.Pelicula)
sistema.carga_csv(usuarios_csv, mc.Usuario)
sistema.carga_csv(relaciones_csv, mc.Relacion)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actores')
def actores():
    """Muestra la lista de actores"""
    actores = sistema.actores.values()
    return render_template('actores.html', actores=actores)

@app.route('/peliculas')
def peliculas():
    """Muestra la lista de peliculas"""
    peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas=peliculas)

if __name__ == '__main__':
    app.run(debug=True)

