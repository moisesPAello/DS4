"""
    Clase Team: Equipo
"""
from Athlete import Athlete
from Sport import Sport
class Team:
    """Clase para respresentar un equipo"""
    def __init__(self, name:str, sport:Sport, player:list):
        """Constructor de la clase Team"""
        self.name = name
        self.sport = sport
        self.players = player

    def __str__(self):
        """Metodo para representar la calse como string"""
        return f"Team: {self.name}, {self.sport}, {self.players}"
    
    def __repr__(self):
        """Metodo para representar la clase como string"""
        return f"Team(name='{self.name}', sport={repr(self.sport)}, player={self.players})"
    
    def to_json(self)->dict:
        """Metodo para representar la clase como diccionario"""
        return {"name":self.name, "sport":self.sport.to_json(), "players":[player.to_json() for player in self.players]}
    

if __name__ == "__main__":
    atleta1 = Athlete("Michale Jordan")
    atleta2 = Athlete("Kobe Bryant")
    atleta3 = Athlete("Lebron James")
    atleta4 = Athlete("Stephen Curry")
    atleta5 = Athlete("Shaquille O'Neal")
    deporte = Sport("Basketball", 5, "NBA")
    lakers = Team("Los Angeles Lakers", deporte, 
        [atleta1, atleta2, atleta3, atleta4, atleta5])
    print(lakers)
