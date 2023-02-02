from os import path
from data.vzor import PREVOD

# Chceme načíst obsah textového souboru `byty.txt`, který je umístěný v podadresáři `data`.

# Údaje převeď pmocí vzorového slovníku ze zadání.

# Celá úloha se bude skládat z těchto na sebe navazujících kroků:
# 1. **Rozvržení** struktury programu,
# 2. **vyhledání** textového souboru,
# 3. **načtení** textového souboru,
# 4. **iterování** načtenými daty,
# 5. **selekcí** původního označení bytů,
# 6. **nahrazení** původního označení novým označením,
# 7. **spojení** nového označení a zbytku původního řádku.

# MYSLET VE FUNKCICH !


def preved_typy_bytu(subor):
    #funkcia, ktora vezme subor a v zaveru vytvori novy subor s prevedenymi udajmi
    if existuje_vstupny_txt(subor)
        # funkcia, ci subor existuje, pokial ano, pobezi dalsia funkcia
        print(nacitaj_obsah_txt(subor)(0))
        # funkcia, ktora nacita obsah suboru a vrati nam ho
        riadok = nacitaj_obsah_txt(subor)[0]
        # funkcia, ktora prevedie tym bytu na zaklade slovniku vzor.PREVOD
        print(preved_typ_bytu(PREVOD,riadok))
        # funkcia, ktora bude prechadzat jednotlive riadky v suboru
        # funkcia, ktora vytvori novy subor so ziskanymi datami -> writelines

    pass

def existuje_vstupny_txt(subor: str) -> bool:
    if os.path.isfile(subor):
        print("Nacitam subor!")
        return True
    else:
        print("Subor neexistuje!")
        return False

def nacitaj_obsah_txt(subor: str) -> list:
    with open(subor,mode = "r", encoding= "utf-8") as txt:
        return txt.readlines()

def preved_typ_bytu(vzor: dict, udaj: str) -> str:
    povodny, zbytok = udaj.split(",", maxsplit=1)
    nove_oznacenie = vzor.get (povodny, "neexistujuci typ" )
    return ",".join((nove_oznacenie,zbytok))


preved_typy_bytu("data/byty.txt")