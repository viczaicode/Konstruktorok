

def etlap(lista):
    """itt irjuk ki az etelek neveit és árait"""
    for i in range(0, len(lista,),1):
        print(f"** {lista[i].nev} {lista[i].ar:>8}Ft **")

def atlagar(lista):
    osszeg = 0
    atlag = 0
    db = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i].ar
        db += 1
    atlag = osszeg / db
    return atlag

def legdragabb_etel(lista):
    MAX_INDEX = 0
    for i in range(0,len(lista),1):
        if (MAX_INDEX < lista[i].ar):
            MAX_INDEX = lista[i].ar
            nev = lista[i].nev
    return nev