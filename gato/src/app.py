"""
Este archivo es el punto de entrada a la aplicacion.
Aqui se importan las funciones de tablero.py y se ejecutan.
"""
from ui import UI

def main():
    """Funcion principal"""
    ui = UI()
    ui.run()

if __name__ == '__main__':
    main()