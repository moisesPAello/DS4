from Team import Team
from Athlete import Athlete
from Sport import Sport
from random import choice
class Game:
    """Clase Game: Juego entre dos equipos"""
    sports_dict = {
            "LMP": [x for x in range(0, 11)],
            "NBA": [x for x in range(50, 136)],
            "NFL": [x for x in range(0, 61)],
            "MLB": [x for x in range(0, 21)],
            "MLX": [x for x in range(0, 11)]
        }
    def __init__(self, A:Team, B:Team):
        """Constructor de la clase Game"""
        self.A = A
        self.B = B
        self.score = dict()
        self.score[A.name] = 0
        self.score[B.name] = 0

    def play(self):
        """Juego simulado entre dos euipos"""
        league = self.A.sport.league
        points = self.sports_dict[league]
        puntos1 = choice(points)
        puntos2 = choice(points)
        self.score[self.A.name] = puntos1
        self.score[self.B.name] = puntos2

    def __str__(self):
        """Metodo para representar la clase como string"""
        return f"Game: {self.A.name}: {self.score[self.A.name]} - {self.score[self.B.name]} :{self.B.name}"
        
    def __repr__(self):
        """Metodo para representar la clase como string"""
        return f"Game(A={repr(self.A)}, B={repr(self.B)}), score)"

    def to_json(self)->dict:
        """Metodo para representar la clase como string"""
        return {"A":self.A.to_json(), "B":self.B.to_json(), "score":self.score}

if __name__ == "__main__":
    dt = ["Jordan", "Johnson", "Pipen", "Bird", "Kobe"]
    cz = ["Bjovik", "Czack", "Pfeizer", "Leonard", "Kempfe"]
    players_a = [Athlete(x) for x in dt]
    players_b = [Athlete(x) for x in cz]
    basketball = Sport("Basketball", 5, "NBA")
    team_a = Team("Dream Team", basketball, players_a)
    team_b = Team("Czeck Rep.", basketball, players_b)
    game = Game(team_a, team_b)
    print(game)
    game.play()
    print(game)
    print("----------------")
    print(repr(game))
    print(game.to_json())
    filename_json =  "games/game.json"
    with open(filename_json, "w", encoding="utf8") as f:
        f.write(str(game.to_json()))
        
    