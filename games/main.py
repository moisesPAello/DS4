from Athlete import Athlete
from Sport import Sport
from Team import Team
from Game import Game
import json
 
def main(archivo_torneo:str):
    """Fucnion pricipal de juego"""
    if archivo_torneo != "":
        with open(archivo_torneo,"r", encoding="utf8")as file:
            torneo=json.load(file)
    else:
        players_mexico=['Chicharito','Piojo','Ochoa','Chucky','Tecatito','Araujo','Moreno','Guardado','Herrera','Layun','Jimenez']
        players_espania=['Ramos','Iniesta','Casillas','Xavi','Pique','Torres','Villa','Silva','Fabregas','Alonso','Busquets']
        players_brasil=["Neymar", "Coutihno", "Marcelo", "Paulinho", "Thiago", "Silva", "Firmino", "Danilo"]
        players_argentina=["Messi", "Aguero", "Di Maria", "Mascherano", "Higuain", "Dybala", "Otamendi", "Romero", "Rojo", "Banega", "Fazio"]
        lista_mexico=[Athlete(x) for x in players_mexico]
        lista_espania=[Athlete(x) for x in players_espania]
        lista_brasil=[Athlete(x) for x in players_brasil]
        lista_argentina=[Athlete(x) for x in players_argentina]

        soccer=Sport("Soccer",11,"FIFA")
        mexico=Team("Mexico",soccer,lista_mexico)
        espania = Team("España", soccer, lista_espania)
        brasil = Team("Brasil", soccer, lista_brasil)
        argentina = Team("Argentina", soccer, lista_argentina)
        equipos = [mexico, espania, brasil, argentina]
        juegos = {}
        for local in equipos:
            for visitante in equipos:
                if local != visitante:
                    juego = Game(local, visitante)
                    juegos[juego.to_json()["A"]["name"]] = juego.to_json()
                
        torneo = [juego.to_json()]
        torneo_json = "torneo.json"
        with open(torneo_json, "w", encoding="utf8") as f:
            json.dump(torneo, f, ensure_ascii=False, indent=4)
        print(f"Se eescribio el archivo {torneo_json} con un torneo de {len(torneo)} juego(s)")
    #Jugar todos los juegos del torneo
    for juego in torneo:
        A = Team(juego["A"]["name"], Sport(juego["A"]["sport"]["name"], juego["A"]["sport"]["players"], juego["A"]["sport"]["league"]), [Athlete(x["name"]) for x in juego ["A"]["players"]])
        B = Team(juego["B"]["name"], Sport(juego["B"]["sport"]["name"], juego["B"]["sport"]["players"], juego["B"]["sport"]["league"]), [Athlete(x["name"]) for x in juego ["B"]["players"]])
        game = Game(A, B)
        game.play()
        print(game)
        print("----------------")
        
if __name__ == "__main__":
    archivo_torneo = ""
    main(archivo_torneo)

