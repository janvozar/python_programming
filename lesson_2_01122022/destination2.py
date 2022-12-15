mesta = [
    "Praha", "Viden", "Olomouc",
    "Svitavy", "Zlin", "Ostrava"
]
domeny = ("gmail.com", "seznam.cz", "email.cz")
zlavy = ("Olomouc", "Svitavy", "Ostrava")
ceny = (150, 200, 120, 120, 100, 180)
dvojita_ciara = "=" * 35
ciara = "-" * 35
nabydka = \
"""1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180"""

# vziat vstup od uzivatela
# vstup preved na cislo 
# pokial uzivatel zada cislo medzi 1-6
#     od vstupu odpocitaj jedna
#     na danej pozicii vyhladaj mesto v zozname
#     vysledne mesto vytlac
# inak
#     vypis cislo neexistuje
#     ukonci program --> quit ()

destinacia = int(input("DESTINACIA: "))
if destinacia >=1 and destinacia <=6:
    upravena_destinacia = mesta [destinacia -1]
    print(f"Destinacia: {upravena_destinacia}")
else:
    print ("Cislo nexistuje. Ukoncujem...")
    quit()