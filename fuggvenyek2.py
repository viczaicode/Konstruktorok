def osszefizetes(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i].fizetes
    return osszeg

def legidosebb_ember(lista):
    MAX_INDEX = 2024
    jelenlegi_ev = 2024
    for i in range(0,len(lista),1):
        if (MAX_INDEX > lista[i].Szul_ev):
            MAX_INDEX = lista[i].Szul_ev
        kor = jelenlegi_ev - MAX_INDEX 
    return kor

def hany_beosztott(lista):
    szamlalo = 0
    for i in range(0, len(lista),1):
        if (lista[i].pozicio == "beosztott"):
            szamlalo += 1
    return szamlalo

def legalacsonyabb_fizetes(lista):
    MAX_INDEX = 200000000
    for i in range(0,len(lista),1):
        if (MAX_INDEX > lista[i].fizetes):
            MAX_INDEX = lista[i].fizetes
            nev = lista[i].nev
    return nev
