from os import path
from data.vzor import PREVOD

# Chceme načíst obsah textového souboru `byty.txt`, který je umístěný v podadresáři `data`.
# Údaje převeď pmocí vzorového slovníku ze zadání.

def preved_typy_bytu(soubor):
    # funkce, která vezme soubor a v záveru vytvoří nový soubor s převedenými údaji

    # funkce, zda soubor existuje, pokud ano, pobezi další funkce
    if existuje_vstupni_txt(soubor):
        # funkce, která načte obsah a vrátí nám jej
        puvodni_data = nacti_obsah_txt(soubor)
        # funkce, která bude procházet jednotlivé řádky v souboru
        vysledne_data = projdi_vsechna_data(puvodni_data, PREVOD)
        # funkce, která vytvoří nový soubor se získanými daty -> writelines
        zapis_obsah_txt(vysledne_data, "vystup.txt")

def existuje_vstupni_txt(soubor: str) -> bool:
    if path.isfile(soubor):
        print("Načítáme soubor!")
        return True
    else:
        print("Soubor neexistuje!")
        return False

def nacti_obsah_txt(soubor: str) -> list:
    with open(soubor, mode = "r", encoding = "utf-8") as txt:
        return txt.readlines()

def preved_typ_bytu(vzor: dict, udaj: str) -> str:
    puvodni, zbytek  = udaj.split(",", maxsplit=1)
    nove_oznaceni = vzor.get(puvodni, "neexistujici typ")
    return ",".join((nove_oznaceni, zbytek))

# DU
def projdi_vsechna_data(data: list, vzor: dict) -> list:
    nova_data = []

    for udaj in data:
        prevod = preved_typ_bytu(vzor, udaj)
        nova_data.append(prevod)
    return nova_data

def zapis_obsah_txt(data: set, soubor: str) -> None:
    with open(soubor, mode="w", encoding="utf-8") as txt:
        txt.writelines(data)

preved_typy_bytu("data/byty.txt")
