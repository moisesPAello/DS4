class Athlete:
    """Athlete class"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Athlete: {self.name}"
    
    def __repr__(self):
        return f"Athlete('{self.name}')"
    
    def display(self):
        print(f"{self.name}")

if __name__ == "__main__":
    a = Athlete("Ana G.")
    a.display()
    print(a)
    print(repr(a))
    print(f"a: {id(a)}")
    
    b = eval(repr(a))
    print(b)
    print(f"b: {id(b)}")