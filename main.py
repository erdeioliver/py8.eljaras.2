'''
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!
'''

def elemzes(x):
    if x == 0:
        return print("A szám nulla")
    elif x % 2 == 0:
        return print("A szám pozitív")
    else:
        return print("A szám negatív")

szam = elemzes(1)