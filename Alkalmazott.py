from datetime import datetime
class Alkalmazott:
    def __init__(self, nev:str="",Szul_ev:int=0,fizetes:int=1000, pozicio:str=""):

        self.nev = nev
        self.Szul_ev = Szul_ev
        self.fizetes = fizetes
        self.pozicio = pozicio
        self.kor()

    def kor(self):
        jelenlegi_ev = datetime.now().year
        return jelenlegi_ev - self.Szul_ev

    def __str__(self):
        return f"Ember neve: {self.nev}, Fizetése: {self.ar}, Születési éve: {self.Szul_ev}, Pozíciója: {self.pozicio}"
    
    def fizetesemeles(self, ertek:float=1.20):
       self.fizetes = self.fizetes * ertek


    

            

