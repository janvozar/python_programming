import os

# slučte funkce preved_hlavni_mesta a precti_txt_soubor
# pokud při otevírání souboru nebude soubor existovat, odchytněte výjimku - FileNotFoundError

def hlavni_mesta():
    jmeno_souboru = "countries_and_cities.txt"
    preved_hlavni_mesta(jmeno_souboru)


def preved_hlavni_mesta(soubor: str):
    try:
        with open(soubor, encoding="utf-8") as txt:
            udaje = txt.readline()
    except FileNotFoundError:
        print(f"Soubor \'{soubor}\' neexistuje!")
    else:
        projdi_udaje(udaje)

def projdi_udaje(udaje: list) -> None:
    for udaj in udaje:
        if udaj == "quit":
            break
        else:
            preved_udaj(udaj)


def preved_udaj(udaj: str) -> None:
    print(udaj.strip().title())


hlavni_mesta()