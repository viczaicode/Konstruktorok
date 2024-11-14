"""
Hozz létre egy osztályzatok listát osztalyzatok_lista = [3,4,5,2,3,4,5,4] 
és nevek = ["Béla", "Jenő", "Ági", "Rozi"]

nevek és a nevekhez tartozó osztályzatok összetartoznak

etelek = ["húsleves", "krumplis"]
ar = [1234,3456]

Új adatszerkezet - ami egybe tudja kezelni az összetartozó adatokat

szemely = {név: "Béla", osztalyzat: 3}

kaja1 = {nev:"húsleves", ar:1234, elk_ido:2}
kaja2 = {nev:"krumplis", ar:3456, elk_ido:0.5}

objektumok - tulajdonságokkal (főnevek) és viselkedéssel
 (cselekvés) bíró adatszerkezet

Készítünk egy sablont ami alapján le tudjuk gyártani
a konkrét egyedeket. 
OSZTÁLY - sablon - tervrajz
OBJEKTUM - konkrét egyedek - konkrét termék

"""
from Alkalmazott import Alkalmazott
import fuggvenyek2
import Etel
"""from Etel import Etel
import fuggvenyek

2. Létrehozzuk a konkrét példányt a tervrajz
alapján""""""



etel_lista = []
etel_lista.append(Etel("Húsleves",1234))
etel_lista.append(Etel("Krumplis",2345))
etel_lista.append(Etel("Rántott hús",2145))
etel_lista.append(Etel("palacsinta",1450))

print("Szia én vagyok a " + etel_lista[0].nev + " Az állapotom " + etel_lista[0].allapot)

etel_lista[0].keszul()

print("Szia én vagyok a " + etel_lista[0].nev + " Az állapotom " + etel_lista[0].allapot)
print("Szia én vagyok a " + etel_lista[1].nev + " Az állapotom " + etel_lista[1].allapot)



Írj metódust, amely paraméterében megkapja a listát és kiírja az ételek neveit
és árait látványos formában



fuggvenyek.etlap(etel_lista)


Írj metódust, ... , megmondja az ételek átlagárát"""

"""Írj metódust, ... , megmondja a legdrágább étel nevét"""

"""atlag = fuggvenyek.atlagar(etel_lista)
print(f"Az ételek árainak átlaga: {atlag}")

MAX_INDEX = fuggvenyek.legdragabb_etel(etel_lista)
print(f"A legdrágább kaja: {MAX_INDEX}")"""

emberek_lista = []
emberek_lista.append(Alkalmazott("Jani",1998,150000,"beosztott"))
emberek_lista.append(Alkalmazott("Ernő",2002,220000, "cégvezető"))
emberek_lista.append(Alkalmazott("Imre",1978,600000, "könyvelő"))
emberek_lista.append(Alkalmazott("Lajos",2009,750000, "beosztott"))
emberek_lista.append(Alkalmazott("Viki",2010,350000, "HR"))

osszfizetes = fuggvenyek2.osszefizetes(emberek_lista)
print(f"Az alkalmazottak összfizetése: {osszfizetes}")
Legidosebb_ember = fuggvenyek2.legidosebb_ember(emberek_lista)
print(f"Ennyi idős a legidősebb ember: {Legidosebb_ember}")
hany_beosztott = fuggvenyek2.hany_beosztott(emberek_lista)
print(f"Ennyi beosztott pozícióban lévő alkalmazott van: {hany_beosztott}")
legalacsonyabb_fizetes = fuggvenyek2.legalacsonyabb_fizetes(emberek_lista)
print(f"Neki van a legalacsonyabb fizetése: {legalacsonyabb_fizetes}")
fizetesemeles = Etel.fizetesemeles(legalacsonyabb_fizetes)
print(f"Megnöveltem a fizetéséet {fizetesemeles}")