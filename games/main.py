from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import json
import game_logic as gl

 
def main(archivo_torneo:str):
    """Fucnion pricipal de juego"""
    
    if archivo_torneo != "":
        with open(archivo_torneo,"r", encoding="utf8")as file:
            torneo=json.load(file)
    else:
        gl.create_gamefile()
        archivo_torneo = "games/torneo.json"
        with open(archivo_torneo,"r", encoding="utf8")as file:
            torneo=json.load(file)
    
    #Jugar todos los juegos del torneo
    gl.play_game(torneo)
        
    #Calcular el tablero de puntuación         
    tablero  = gl .scoring(torneo)
    gl.display_tablero(tablero)
    
         
                
if __name__ == "__main__":
    archivo_torneo = ""
    main(archivo_torneo)