"""Clase Sport"""
class Sport:
    """Clase para representar un deporte"""
    def __init__(self, name:str, players:int, league:str):
        """Metodo constructor"""
        self.name = name
        if isinstance(players, int): #Filtro de enteros
            self.players = players
        else:
            self.players = int(players)
        self.players = players
        self.league = league

    def __str__(self):
        """Metodo para representar la clase como string"""
        return f"Sport: {self.name}, {self.players}, {self.league}"
    
    def __repr__(self):
        """Metodo para representar la clase como string"""
        return f"Sport(name='{self.name}', players={self.players}, league='{self.league}')"
    
    def to_json(self)->dict:
        """Metodo para representar la clase como diccionario"""
        return {"name": self.name, "players": self.players, "league": self.league}
    
if __name__ == "__main__":
    sport = Sport("Soccer", 11, "FIFA")
    print(sport)
    print(repr(sport))
    print(sport.to_json())
    nfl = Sport("Football", "11", "NFL")
    lmp = Sport("Baseball", 9, "LMP")
    mlb = Sport("Baseball", 9, "MLB")
    lmx = Sport("Soccer", 11, "Liga MX")
    nba = Sport("Basketball", 5, "NBA")
    lista_deportes = [nfl, lmp, mlb, lmx, nba, sport]
    archivo_deportes = "games/deportes.txt"
    with open(archivo_deportes, "w") as file:
        for deporte in lista_deportes:
            file.write(repr(deporte)+"\n")
    sport_list = []
    with open(archivo_deportes, "r") as file:
        for line in file:
            deporte = eval(line)
            sport_list.append(deporte)
    print("Se han creado los objetos...")
    print(sport_list)
    print(sport_list[0].to_json())
    print()

    #Escritura de archivo en formato JSON
    print("Se escribe archivo JSON...")
    import json
    archivo_json = "games/deportes.json"
    sports_json = [sport.to_json() for sport in sport_list]
    with open(archivo_json, "w", encoding="utf8") as file:
        json.dump(sports_json, file, indent=4)
    print()
    #Leemos el archivo JSON
    print("Le lee archivo JSON...")
    sport_list_json = []
    with open(archivo_json, "r") as file:
        sport_list_json = json.load(file)
    print(sport_list_json)
    print(repr(sport_list_json[0]))