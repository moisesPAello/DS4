#Hola mundo de Flask

from flask import Flask

app = Flask(__name__)

@app.route('/')  #Home page o raíz o indice
def index():
    return '''<html>
                <head>
                    <title>Hello world</title>
                </head>
                
                <body>  
                    <h1>Hola Mundo</h1>
                    <p>Ir a la página de <a href="/about">Acerca de</a></p>
                </body>
        </html>'''

@app.route('/about')  # Corregido: agregada la barra diagonal
def about():
    return '''<html>
                <head>
                    <title>Hello world</title>
                </head>
                
                <body>  
                    <h1>Hola Mundo</h1>
                    <p>Ir a la página de <a href="/">Inicio</a></p>
                </body>
        </html>'''

if __name__ == '__main__':
    app.run(debug=True)  #Activa el modo de depuración