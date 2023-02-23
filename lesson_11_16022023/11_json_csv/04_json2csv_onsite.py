# napište program, který načte data z .json souboru, 
# vyfilruje data podle žádoucích klíčů 
# a výsledné vyfiltrované data uloží do .csv souboru 

import csv
import json


def hlavni():
    rel_cesta = "data/ORIG_1.json"
    zadouci_klice = ("first_name", "last_name", "email")
    json_to_csv(rel_cesta, zadouci_klice)

def json_to_csv(soubor, zadouci_klice):
    slovniky = nacti_obsah_jsnu(soubor)

    vyfiltrovane = []

    for slovnik in slovniky:
        vyfiltrovane.append(filtruj_klice(zadouci_klice, slovnik))
    
    zapis_do_csv("vysledky.csv", vyfiltrovane)

def nacti_obsah_jsnu(soubor):
    try:
        with open(soubor) as json_data:
            return json.load(json_data)
    except FileNotFoundError:
        print("Soubor neexistuje, ukoncuji program!")
        quit()

def filtruj_klice(zadouci_klice, puvodni_slovnik):
    upraveny_slovnik = dict()

    for klic in puvodni_slovnik:
        if klic not in zadouci_klice:
            continue
        upraveny_slovnik [klic] = puvodni_slovnik[klic]
    
    return upraveny_slovnik
   
def zapis_do_csv(soubor, udaje):
    with open(soubor, mode = "w", newline="") as csv_vystup;
        sloupce = udaje[0].keys()
        zapis =csv.DictWriter(csv_vystup, fieldnames=sloupce)
        zapis.writeheader()
        zapis.writerows(udaje)

hlavni()
