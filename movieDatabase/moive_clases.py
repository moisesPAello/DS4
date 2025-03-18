from datetime import datetime
import csv
from hashlib import sha256

class Actor:
    """Clase para representar un actor"""
    def __init__(self, id_actor, nombre, fecha_nacimiento, ciudad_nacimiento, url_imagen):
        self.id_actor = id_actor
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
            'id_actor': self.id_actor,
            'nombre': self.nombre,
            'fecha_nacimiento': self.fecha_nacimiento.strftime('%Y-%m-%d') if self.fecha_nacimiento else None,
            'ciudad_nacimiento': self.ciudad_nacimiento,
            'url_imagen': self.url_imagen
        }

class Pelicula:
    """Clase para representar una película"""
    def __init__(self, id_pelicula, titulo, fecha_lanzamiento, url_poster):
        self.id_pelicula = id_pelicula
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

class Relacion:
    """Clase para representar la relación entre actores y películas"""
    def __init__(self, id_actor, id_pelicula):
        self.id_actor = id_actor
        self.id_pelicula = id_pelicula

    def to_dict(self):
        """Devuelve un diccionario con los datos de la relación"""
        return {
            'id_actor': self.id_actor,
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

class SistemaCine:
    """Clase para representar el sistema de cine"""
    def __init__(self):
        self.actores = []
        self.peliculas = []
        self.relaciones = []
        self.usuarios = []
        self.usuario_actual = None  # Corregido el nombre de la variable

    def carga_csv(self, archivo, clase):
        """Método para cargar datos desde un archivo CSV"""
        try:
            with open(archivo, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if clase == Actor:
                        self.actores.append(Actor(
                            id_actor=row['id_estrella'],
                            nombre=row['nombre'],
                            fecha_nacimiento=row['fecha_nacimiento'],
                            ciudad_nacimiento=row['ciudad_nacimiento'],
                            url_imagen=row['url_imagen']
                        ))
                    elif clase == Pelicula:
                        self.peliculas.append(Pelicula(
                            id_pelicula=row[''],  # Columna vacía en CSV que corresponde al ID
                            titulo=row['titulo_pelicula'],
                            fecha_lanzamiento=row['fecha_lanzamiento'],
                            url_poster=row['url_poster']
                        ))
                    elif clase == Relacion:
                        self.relaciones.append(Relacion(
                            id_actor=row['id_estrella'],
                            id_pelicula=row['id_pelicula']
                        ))
                    elif clase == Usuario:
                        self.usuarios.append(Usuario(
                            username=row['username'],
                            nombre=row['nombre_completo'],
                            email=row['email'],
                            password=row['password']
                        ))
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {archivo}")
        except Exception as e:
            print(f"Error al cargar el archivo {archivo}: {e}")

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
        actor = sistema.actores[0]
        print(f"ID: {actor.id_actor}")
        print(f"Nombre: {actor.nombre}")
        print(f"Fecha de nacimiento: {actor.fecha_nacimiento}")
        print(f"Ciudad de nacimiento: {actor.ciudad_nacimiento}")
    
    if sistema.peliculas:
        print(f"\n===== PRIMERA PELÍCULA =====")
        pelicula = sistema.peliculas[0]
        print(f"ID: {pelicula.id_pelicula}")
        print(f"Título: {pelicula.titulo}")
        print(f"Fecha de lanzamiento: {pelicula.fecha_lanzamiento}")



