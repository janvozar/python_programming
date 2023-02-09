import os

# slučte funkce preved_hlavni_mesta a precti_txt_soubor
# pokud při otevírání souboru nebude soubor existovat, odchytněte výjimku - FileNotFoundError

def hlavni_mesta():
    jmeno_souboru = "countries_and_cities.txt"
    preved_hlavni_mesta(jmeno_souboru)


def preved_hlavni_mesta(soubor: str):
    if os.path.isfile(soubor):
        print(f"Soubor \'{soubor}\' nalezen!", "Otevírám..", sep="\n")
        udaje = precti_txt_soubor(soubor)
        projdi_udaje(udaje)
    else:
        print(f"Soubor \'{soubor}\' neexistuje!")


def precti_txt_soubor(soubor: str) -> list:
    with open(soubor, encoding="utf-8") as txt:
        return txt.readlines()


def projdi_udaje(udaje: list) -> None:
    for udaj in udaje:
        if udaj == "quit":
            break
        else:
            preved_udaj(udaj)


def preved_udaj(udaj: str) -> None:
    print(udaj.strip().title())


hlavni_mesta()