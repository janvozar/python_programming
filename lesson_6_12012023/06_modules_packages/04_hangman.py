import os
from random import choice

from lekce_moduly.figurine import hangman
from lekce_moduly.words import random_words as slova

zivoty = 7
hra_bezi = True

slovo = choice(slova)
tajnicka = len(slovo) * ["_"]

while hra_bezi and zivoty > 0:
    os.system("clear")
    print(slovo)
    print(f"tajnicka: {tajnicka}, zivoty {zivoty} ")
    print(hangman[0])
    hra_bezi = False

    hadanie = input("Hadaj pismeno/slovo:")

    if hadanie == slovo:
        hra_bezi = False
    elif len(hadanie) == 1 and hadanie in slovo:
        for index, pismeno in enumerate(slovo):
            if hadanie ==  pismeno:
                tajnicka[index] = hadanie    
            if "_" not in tajnicka:
                hra_bezi = False

    else:
        zivoty -= 1

if not  hra_bezi:
    os.system("clear")
    print(hangman[7 - zivoty], f"Tajnicka:{slovo}", "Vyhral si", sep="\n")
else:
    os.system("clear")
    print(hangman[7 - zivoty], f"Tajnicka: {slovo}", "Prehral si", sep="\n")               