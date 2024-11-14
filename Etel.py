"""
1. Lépés: osztály létrehozása

"""

class Etel:
    """Konstruktor feladata, hogy létrehozza a konkrét példáyt a konkrét
    adatokkal a tervrajzból
    
    Beállítsa az adattagokat - objektum tulajdonságok értékei
    """
    def __init__(self, nev:str="",ar:int=1000):

        self.nev = nev
        self.ar = ar
        self.allapot = "folyamatban"
    
    def keszul(self):
        self.allapot= "kesz"
    
    def __str__(self):
        return f"Étel neve: {self.nev}, Ár: {self.ar}, Állapot: {self.allapot}"