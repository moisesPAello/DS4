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
        return f'{self.titulo} ({self.fecha_lanzamiento.year})'

class Relacion:
    """Clase para representar la relación entre actores y películas"""
    def __init__(self, id_relacion, id_estrella, id_pelicula):
        self.id_relacion = int(id_relacion)
        self.id_estrella = int(id_estrella)
        self.id_pelicula = int(id_pelicula)

    def to_dict(self):
        """Devuelve un diccionario con los datos de la relación"""
        return {
            'id_relacion': self.id_relacion,
            'id_estrella': self.id_estrella,
            'id_pelicula': self.id_pelicula
        }

class Usuario:
    """Clase para representar un usuario"""
    def __init__(self, username, nombre, email, password):
        self.username = username
        self.nombre = nombre
        self.email = email
        self.password = self.hash_password(password)

    def hash_password(self, password):
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
                            id_pelicula=row['id_pelicula']
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
            self.idx_actor = max(self.actores.keys()) + 1 if self.actores else 0
        elif clase == Pelicula:
            self.idx_pelicula = max(self.peliculas.keys()) + 1 if self.peliculas else 0
        elif clase == Relacion:
            self.idx_relacion = max(self.relaciones.keys()) + 1 if self.relaciones else 0

    def obtener_peliculas_por_actor(self, id_estrella):
        """Metodo para obtener las peliculas de un actor"""
        ids_peliculas = [relacion.id_pelicula for relacion in self.relaciones.values() if relacion.id_estrella == id_estrella]
        return [self.peliculas[id_pelicula] for id_pelicula in ids_peliculas]
    
    def obtener_actores_por_pelicula(self, id_pelicula):
        """Metodo para obtener los actores de una pelicula"""
        ids_actores = [relacion.id_estrella for relacion in self.relaciones.values() if relacion.id_pelicula == id_pelicula]
        return [self.actores[id_estrella] for id_estrella in ids_actores]

if __name__ == "__main__":
    # Crear instancia del sistema
    sistema = SistemaCine()
    
    # Rutas a los archivos CSV
    ruta_actores = "datos/movies_db - actores.csv"
    ruta_peliculas = "datos/movies_db - peliculas.csv"
    ruta_relaciones = "datos/movies_db - relacion.csv"
    ruta_usuarios = "datos/movies_db - users.csv"
    
    # Cargar datos desde CSV
    print("\n===== CARGANDO DATOS =====")
    sistema.carga_csv(ruta_actores, Actor)
    sistema.carga_csv(ruta_peliculas, Pelicula)
    sistema.carga_csv(ruta_relaciones, Relacion)
    sistema.carga_csv(ruta_usuarios, Usuario)
    
    # Mostrar estadísticas de los datos cargados
    print(f"\n===== ESTADÍSTICAS =====")
    print(f"Actores cargados: {len(sistema.actores)}")
    print(f"Películas cargadas: {len(sistema.peliculas)}")
    print(f"Relaciones cargadas: {len(sistema.relaciones)}")
    print(f"Usuarios cargados: {len(sistema.usuarios)}")
    
    # Mostrar algunos ejemplos de los datos cargados
    if sistema.actores:
        print(f"\n===== PRIMER ACTOR =====")
        actor = sistema.actores[next(iter(sistema.actores))]
        print(f"ID: {actor.id_estrella}")
        print(f"Nombre: {actor.nombre}")
        print(f"Fecha de nacimiento: {actor.fecha_nacimiento}")
        print(f"Ciudad de nacimiento: {actor.ciudad_nacimiento}")
    
    if sistema.peliculas:
        print(f"\n===== PRIMERA PELÍCULA =====")
        pelicula = sistema.peliculas[next(iter(sistema.peliculas))]
        print(f"ID: {pelicula.id_pelicula}")
        print(f"Título: {pelicula.titulo}")
        print(f"Fecha de lanzamiento: {pelicula.fecha_lanzamiento}")

    if sistema.actores:
        print(f"\n===== BÚSQUEDA ACTOR =====")
        try:
            nombre_actor = str(input("Ingrese el nombre del actor que desea buscar: "))
            actor = sistema.actores[next(key for key, value in sistema.actores.items() if value.nombre == nombre_actor)]
            print(actor.__str__())
        except ValueError:
            print("Nombre no encontrado.")

        print(f"\n===== PELÍCULAS DEL ACTOR =====")
        peliculas = sistema.obtener_peliculas_por_actor(actor.id_estrella)
        for pelicula in peliculas:
            print(pelicula.__str__())

    if sistema.usuarios:
        print(f"\n===== BÚSQUEDA USUARIO =====")
        try:
            user = sistema.usuarios["Moises"]
            print(user.__str__())
        except ValueError:
            print("Usuario no encontrado.")




