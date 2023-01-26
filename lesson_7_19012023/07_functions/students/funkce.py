# plus_jedna(2) -->3

def plus_jedna(cislo):
    return cislo + 1

vysledek =plus_jedna(2)

print(vysledek)

# plus_jedna([2,5,9]) --> [3,6,10]

cisla = [2,5,9]
novy_seznam = []

for cislo in cisla:
    novy_seznam.append(cislo + 1)

print(novy_seznam)

def pridej_jedna(seznam_cisel):
    novy_seznam = []

    for cislo in seznam_cisel:
        novy_seznam.append(cislo + 1)

    return novy_seznam

print(pridej_jedna([11,12,13]))
