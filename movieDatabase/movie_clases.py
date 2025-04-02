from datetime import datetime
import csv
from hashlib import sha256

class Actor:
    """Clase para representar un actor"""
    def __init__(self, id_estrella, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen):
        self.id_estrella = int(id_estrella)
        self.nombre = nombre
        try:
            self.fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
        except ValueError:
            self.fecha_nacimiento = None
        self.ciudad_nacimiento = ciudad_nacimiento
        self.url_imagen = url_imagen

    def to_dict(self):
        """Devuelve un diccionario con los datos del actor"""
        return {
            'id_estrella': self.id_estrella,
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento.strftime('%Y-%m-%d') if self.fecha_nacimiento else None,
            'ciudad_nacimiento': self.ciudad_nacimiento,
            'url_imagen': self.url_imagen
        }
    
    def __str__(self):
        """Metodo para imprimir el objeto Actor"""
        return self.nombre

class Pelicula:
    """Clase para representar una película"""
    def __init__(self, id_pelicula, titulo, fecha_lanzamiento, url_poster):
        self.id_pelicula = int(id_pelicula)  # Cast to int
        self.titulo = titulo
        try:
            self.fecha_lanzamiento = datetime.strptime(fecha_lanzamiento, '%Y-%m-%d')
        except ValueError:
            self.fecha_lanzamiento = None
        self.url_poster = url_poster

    def to_dict(self):
        """Devuelve un diccionario con los datos de la película"""
        return {
            'id_pelicula': self.id_pelicula,
            'titulo': self.titulo,
            'fecha_lanzamiento': self.fecha_lanzamiento.strftime('%Y-%m-%d') if self.fecha_lanzamiento else None,
            'url_poster': self.url_poster
        }
    
    def __str__(self):
        """Metodo para imprimir el objeto Pelicula"""
        return f'{self.titulo} ({self.fecha_lanzamiento.year if self.fecha_lanzamiento else "Sin fecha"})'

class Relacion:
    """Clase para representar la relación entre actores y películas"""
    def __init__(self, id_relacion, id_estrella, id_pelicula, personaje=None):
        self.id_relacion = int(id_relacion)
        self.id_estrella = int(id_estrella)
        self.id_pelicula = int(id_pelicula)
        self.personaje = personaje

    def to_dict(self):
        """Devuelve un diccionario con los datos de la relación"""
        return {
            'id_relacion': self.id_relacion,
            'id_pelicula': self.id_pelicula,
            'id_estrella': self.id_estrella,
            'personaje': self.personaje
        }

class Usuario:
    """Clase para representar un usuario"""
    def __init__(self, username, nombre, email, password):
        self.username = username
        self.nombre = nombre
        self.email = email
        self.password = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        """Devuelve el hash de una contraseña"""
        return sha256(password.encode()).hexdigest()

    def to_dict(self):
        """Devuelve un diccionario con los datos del usuario"""
        return {
            'nombre': self.nombre,
            'email': self.email,
            'username': self.username,
            'password': self.password
        }
    
    def __str__(self):
        """Metodo para imprimir el objeto Usuario"""
        return self.nombre
    
class SistemaCine:
    """Clase para representar el sistema de cine"""
    def __init__(self):
        self.actores = {}
        self.peliculas = {}
        self.relaciones = {}
        self.usuarios = {}
        self.usuario_actual = None
        self.idx_actor = 0
        self.idx_pelicula = 0
        self.idx_relacion = 0

    def carga_csv(self, archivo, clase):
        """Método para cargar datos desde un archivo CSV"""
        try:
            with open(archivo, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if clase == Actor:
                        actor = Actor(
                            id_estrella=row['id_estrella'],
                            nombre=row['nombre'],
                            fecha_nacimiento=row['fecha_nacimiento'],
                            ciudad_nacimiento=row['ciudad_nacimiento'],
                            url_imagen=row['url_imagen']
                        )
                        self.actores[actor.id_estrella] = actor
                    elif clase == Pelicula:
                        pelicula = Pelicula(
                            id_pelicula=row['id_pelicula'],
                            titulo=row['titulo_pelicula'],
                            fecha_lanzamiento=row['fecha_lanzamiento'],
                            url_poster=row['url_poster']
                        )
                        self.peliculas[pelicula.id_pelicula] = pelicula
                    elif clase == Relacion:
                        relacion = Relacion(
                            id_relacion=row['id_relacion'],
                            id_estrella=row['id_estrella'],
                            id_pelicula=row['id_pelicula'],
                            personaje=row.get('personaje', None)
                        )
                        self.relaciones[relacion.id_relacion] = relacion
                    elif clase == Usuario:
                        usuario = Usuario(
                            username=row['username'],
                            nombre=row['nombre_completo'],
                            email=row['email'],
                            password=row['password']
                        )
                        self.usuarios[usuario.username] = usuario
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {archivo}")
        except Exception as e:
            print(f"Error al cargar el archivo {archivo}: {e}")

        if clase == Actor:
            self.idx_actor = max([int(k) for k in self.actores.keys()]) + 1 if self.actores else 0
        elif clase == Pelicula:
            self.idx_pelicula = max([int(k) for k in self.peliculas.keys()]) + 1 if self.peliculas else 0
        elif clase == Relacion:
            self.idx_relacion = max([int(k) for k in self.relaciones.keys()]) + 1 if self.relaciones else 0

    def guardar_csv(self, archivo, objetos):
            if not objetos:
                return
            with open(archivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=next(iter(objetos.values())).to_dict().keys())
                writer.writeheader()
                for obj in objetos.values():
                    writer.writerow(obj.to_dict())

    def autenticar_usuario(self, username, password):
        """Método para autenticar un usuario"""
        if username in self.usuarios:
            usuario = self.usuarios[username]
            if usuario.password == usuario.hash_password(password):
                self.usuario_actual = usuario
                return True
        return False

    def obtener_peliculas_por_actor(self, id_estrella):
        """Metodo para obtener las peliculas de un actor"""
        ids_peliculas = [relacion.id_pelicula for relacion in self.relaciones.values() if relacion.id_estrella == id_estrella]
        return [self.peliculas[id_pelicula] for id_pelicula in ids_peliculas]
    
    def obtener_actores_por_pelicula(self, id_pelicula):
        """Metodo para obtener los actores de una pelicula"""
        ids_actores = [relacion.id_estrella for relacion in self.relaciones.values() if relacion.id_pelicula == id_pelicula]
        return [self.actores[id_actor] for id_actor in ids_actores]

    def obtener_personajes_por_pelicula(self, id_pelicula):
        """Método para obtener los actores de una película con sus personajes"""
        actores_info = []
        for relacion in self.relaciones.values():
            if relacion.id_pelicula == id_pelicula:
                actor = self.actores.get(relacion.id_estrella)
                if actor:
                    actores_info.append({"actor": actor, "personaje": relacion.personaje})
        return actores_info

    def obtener_personajes_por_estrella(self, id_estrella):
        personajes = []
        for rel in self.relaciones.values():
            if rel.id_estrella == id_estrella:
                pelicula = self.peliculas.get(rel.id_pelicula)
                if pelicula:
                    personajes.append({"personaje": rel.personaje, "pelicula": pelicula})
        return personajes

    def buscar_pelicula_por_titulo(self, titulo):
        """Metodo para buscar una pelicula por titulo"""
        return [pelicula for pelicula in self.peliculas.values() if titulo.lower() in pelicula.titulo.lower()]
    
    def buscar_actor_por_nombre(self, nombre):
        """Metodo para buscar un actor por nombre"""
        return [actor for actor in self.actores.values() if nombre.lower() in actor.nombre.lower()]

    def agregar_pelicula(self, titulo, fecha_lanzamiento, url_poster):
        """Metodo para agregar una pelicula"""
        if self.usuario_actual:
            self.idx_pelicula += 1
            pelicula = Pelicula(self.idx_pelicula, titulo, fecha_lanzamiento, url_poster)
            self.peliculas[pelicula.id_pelicula] = pelicula
            return pelicula

    def agregar_actor(self, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen):
        """Metodo para agregar un actor"""
        if self.usuario_actual:
            self.idx_actor += 1
            actor = Actor(self.idx_actor, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen)
            self.actores[actor.id_estrella] = actor
            return actor

    def agregar_relacion(self, id_pelicula, id_estrella, personaje=None):
        """Metodo para agregar una relacion"""
        if self.usuario_actual:    
            self.idx_relacion += 1
            relacion = Relacion(self.idx_relacion, id_estrella, id_pelicula, personaje)
            self.relaciones[relacion.id_relacion] = relacion
            return relacion
    
    def agregar_usuario(self, username, nombre, email, password):
        """Metodo para agregar un usuario"""
        if not self.usuarios or self.usuario_actual:
            if username not in self.usuarios:
                usuario = Usuario(username, nombre, email, password)
                self.usuarios[username] = usuario
                return usuario
            else:
                print(f"Error: El usuario {username} ya existe")
        else:
            print("Error: Debe iniciar sesión para agregar usuarios")
        return None
    
if __name__ == "__main__":
    # Crear instancia del sistema
    sistema = SistemaCine()
    
    # Rutas a los archivos CSV
    ruta_actores = "datos/movies_db - actores.csv"
    ruta_peliculas = "datos/movies_db - peliculas.csv"
    ruta_relaciones = "datos/movies_db - relaciones.csv"
    ruta_usuarios = "datos/movies_db - usuarios_hashed.csv"
    
    print("\n===== CARGANDO DATOS =====")
    sistema.carga_csv(ruta_actores, Actor)
    sistema.carga_csv(ruta_peliculas, Pelicula)
    sistema.carga_csv(ruta_relaciones, Relacion)
    sistema.carga_csv(ruta_usuarios, Usuario)
    
    print(f"\n===== ESTADÍSTICAS =====")
    print(f"Actores cargados: {len(sistema.actores)}")
    print(f"Películas cargadas: {len(sistema.peliculas)}")
    print(f"Relaciones cargadas: {len(sistema.relaciones)}")
    print(f"Usuarios cargados: {len(sistema.usuarios)}")
    
    # Pruebas de autenticación
    print("\n===== PRUEBAS DE AUTENTICACIÓN =====")
    # Intento de autenticación con credenciales correctas
    if sistema.autenticar_usuario("Moises", "12345"):
        print(f"Autenticación exitosa. Usuario actual: {sistema.usuario_actual.nombre}")
    else:
        print("Autenticación fallida con credenciales correctas.")
    
    # Intento de autenticación con credenciales incorrectas
    if sistema.autenticar_usuario("usuario_inexistente", "contraseña_incorrecta"):
        print("Error: Se autenticó con credenciales incorrectas")
    else:
        print("Autenticación fallida correctamente con credenciales incorrectas.")
    
    # Pruebas de búsqueda de actores
    print("\n===== PRUEBAS DE BÚSQUEDA DE ACTORES =====")
    actores_encontrados = sistema.buscar_actor_por_nombre("Steve")
    if actores_encontrados:
        print(f"Se encontraron {len(actores_encontrados)} actores:")
        for actor in actores_encontrados:
            print(f"- {actor}")
    else:
        print("No se encontraron actores con ese nombre")
    
    # Pruebas de búsqueda de películas
    print("\n===== PRUEBAS DE BÚSQUEDA DE PELÍCULAS =====")
    peliculas_encontradas = sistema.buscar_pelicula_por_titulo("the")
    if peliculas_encontradas:
        print(f"Se encontraron {len(peliculas_encontradas)} películas:")
        for pelicula in peliculas_encontradas:
            print(f"- {pelicula}")
    else:
        print("No se encontraron películas con ese título")
    
    # Pruebas de relaciones (películas de un actor)
    print("\n===== PELÍCULAS DE UN ACTOR =====")
    try:
        # Usar el primer actor encontrado o uno específico si existe
        actor_prueba = actores_encontrados[0] if actores_encontrados else sistema.actores[1]
        print(f"Películas de {actor_prueba.nombre}:")
        peliculas_actor = sistema.obtener_peliculas_por_actor(actor_prueba.id_estrella)
        if peliculas_actor:
            for pelicula in peliculas_actor:
                print(f"- {pelicula}")
        else:
            print("No se encontraron películas para este actor")
    except (KeyError, IndexError):
        print("No se pudo encontrar un actor para la prueba")
    
    # Pruebas de adición de nuevos registros
    print("\n===== AGREGAR NUEVA PELÍCULA =====")
    titulo = "The Godfather"
    fecha_lanzamiento = "1972-03-24"
    url_poster = "https://example.com/godfather.jpg"
    try:
        nueva_pelicula = sistema.agregar_pelicula(titulo, fecha_lanzamiento, url_poster)
        print(f"Se agregó correctamente la película: {nueva_pelicula}")
    except Exception as e:
        print(f"Error al agregar la película: {e}")
    
    print("\n===== AGREGAR NUEVO ACTOR =====")
    nombre = "Al Pacino"
    fecha_nacimiento = "1940-04-25"
    ciudad_nacimiento = "New York City, New York, USA"
    url_imagen = "https://example.com/alpacino.jpg"
    try:
        nuevo_actor = sistema.agregar_actor(nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen)
        print(f"Se agregó correctamente el actor: {nuevo_actor}")
    except Exception as e:
        print(f"Error al agregar el actor: {e}")
    
    print("\n===== CREAR RELACIÓN ENTRE ACTOR Y PELÍCULA =====")
    try:
        if 'nueva_pelicula' in locals() and 'nuevo_actor' in locals():
            nueva_relacion = sistema.agregar_relacion(
                nueva_pelicula.id_pelicula, 
                nuevo_actor.id_estrella,
                "Protagonista"  # Ejemplo de personaje
            )
            print(f"Se creó correctamente la relación entre {nuevo_actor.nombre} y {nueva_pelicula.titulo}")
            print(f"Personaje: {nueva_relacion.personaje}")
            sistema.guardar_csv(ruta_relaciones, sistema.relaciones)

            # Verificar la relación
            peliculas_actor = sistema.obtener_peliculas_por_actor(nuevo_actor.id_estrella)
            print(f"Películas de {nuevo_actor.nombre}:")
            for pelicula in peliculas_actor:
                print(f"- {pelicula}")
    except Exception as e:
        print(f"Error al crear la relación: {e}")
    
    print("\n===== AGREGAR NUEVO USUARIO =====")
    username = "nuevo_usuario"
    nombre = "Usuario de Prueba"
    email = "usuario@test.com"
    password = "contraseña123"
    try:
        nuevo_usuario = sistema.agregar_usuario(username, nombre, email, password)
        if nuevo_usuario:
            print(f"Se agregó correctamente el usuario: {nuevo_usuario.nombre}")
        else:
            print("No se pudo agregar el usuario")
    except Exception as e:
        print(f"Error al agregar el usuario: {e}")





