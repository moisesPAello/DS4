"""Programa pincipal de movieDatabase"""
from flask import Flask, render_template, request, redirect, url_for, session, flash
import random
import movie_clases as mc
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Clave secreta para sesiones
sistema = mc.SistemaCine()
ruta = 'datos/movies_db - '
actores_csv = ruta + 'actores.csv'
peliculas_csv = ruta + 'peliculas.csv'
usuarios_csv = ruta + 'usuarios_hashed.csv'  
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

@app.route('/actor/<int:id_actor>')
def actor(id_actor):
    """Muestra la informacion de un actor"""
    actor = sistema.actores[id_actor]
    personajes = sistema.obtener_personajes_por_estrella(id_actor)
    return render_template('actor.html', actor=actor, lista_peliculas=personajes)

@app.route('/peliculas')
def peliculas():
    """Muestra la lista de peliculas"""
    peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas=peliculas)

@app.route('/pelicula/<int:id_pelicula>')
def pelicula(id_pelicula):
    """Muestra la información de una película"""
    pelicula = sistema.peliculas[id_pelicula]
    actores = sistema.obtener_personajes_por_pelicula(id_pelicula)
    return render_template('pelicula.html', pelicula=pelicula, actores=actores)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Maneja el inicio de sesión de usuarios"""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Intentando iniciar sesión con usuario: {username} y contraseña: {password}")
        login_exitoso = sistema.autenticar_usuario(username, password)
        if login_exitoso:
            print(f"Usuario {username} autenticado correctamente")
            session['logged_in'] = True
            session['username'] = sistema.usuario_actual.nombre
            flash('Has iniciado sesión correctamente', 'success')
            return redirect(url_for('index'))
        else:
            print(f"Error de autenticación para usuario: {username}")
            flash('Usuario o contraseña incorrectos', 'danger')
            return render_template('login.html', error='Usuario o contraseña incorrectos')
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Cierra la sesión del usuario"""
    session.pop('username', None)
    flash('Has cerrado sesión correctamente', 'success')
    return redirect(url_for('index'))

@app.route('/agregar_relacion', methods=['GET', 'POST'])
def agregar_relacion():
    """Agrega una relacion entre un actor y una pelicula"""
    if sistema.usuario_actual is None:
            flash('Debes iniciar sesión para agregar una relación', 'danger')
            return redirect(url_for('login'))
    if request.method == 'GET':
        actores = []
        actores_en_sistema = sistema.actores.values()
        for actor in actores_en_sistema:
            actores.append({'id_estrella': actor.id_estrella, 'nombre': actor.nombre})
        actores_en_orden = sorted(actores, key=lambda x: x['nombre'])
        
        peliculas = []
        peliculas_en_sistema = sistema.peliculas.values()
        for pelicula in peliculas_en_sistema:
            peliculas.append({'id_pelicula': pelicula.id_pelicula, 'titulo_pelicula': pelicula.titulo})
        peliculas_en_orden = sorted(peliculas, key=lambda x: x['titulo_pelicula'])
        
        return render_template('agregar_relacion.html', actores=actores_en_orden, peliculas=peliculas_en_orden)
    if request.method == 'POST':
        id_estrella = int(request.form['actorSelect'])
        id_pelicula = int(request.form['movieSelect'])
        personaje = request.form['character']
        sistema.agregar_relacion(id_pelicula, id_estrella, personaje)
        sistema.guardar_csv(relaciones_csv, sistema.relaciones)
        flash('Relación agregada correctamente', 'success')
        return redirect(url_for('actor', id_actor=id_estrella))
    
if __name__ == '__main__':
        app.run(debug=True)