# vstupni promenne
mesta = [
    "Praha", "Viden", "Olomouc",
    "Svitavy", "Zlin", "Ostrava"
]
domeny = ("gmail.com", "seznam.cz", "email.cz")
slevy = ("Olomouc", "Svitavy", "Ostrava")
ceny = (150, 200, 120, 120, 100, 180)
dvojita_cara = "=" * 35
cara = "-" * 35
nabidka = \
"""1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180"""

# pozdravit uzivatele & vypsat nabidku
print(
    "VITEJTE U NASI APLIKACE DESTINATIO!",
    cara,
    nabidka,
    dvojita_cara,
    sep="\n"
)

# ziskat vstupy od uzivatele
destinace = int(input("CISLO DESTINACE:"))
upravena_destinace = mesta[destinace - 1]

# overeni spravneho cisla destinace
if destinace <= 6 and destinace >= 1:
    print(upravena_destinace)
else:
    print("Vybrane cislo neexistuje! Ukoncuji..")
    quit()
print(cara)

# overit jestli uzivatel dostane slevu
if upravena_destinace in slevy:
    nova_cena = 0.75 * ceny[destinace - 1]
    print(f"ZISKAVATE 25% SLEVU! CENA: {nova_cena}")
    print(cara)
else:
    nova_cena = ceny[destinace - 1]

jmeno = input("JMENO:")
prijmeni = input("PRIJMENI:")
print(cara)

# overime spravne jmeno a prijmeni
if jmeno.isalpha() and prijmeni.isalpha():
    print(f"Cele jmeno: {jmeno} {prijmeni}")
else:
    print("Jmeno nebo prijmeni nejsou v poradku! Ukoncuji..")
    quit()
print(cara)

email = input("EMAIL:")
print(cara)

# overeni validni emailove adresy
if "@" in email and email.split("@")[1] in domeny:
    print("Email je v poradku")
else:
    print(cara)
    print("Neplatna emailova adresa. Ukoncuji..")
    quit()
print(dvojita_cara)

print(f"""DEKUJI, {jmeno} ZA OBJEDNAVKU,
CIL. DESTINACE: {upravena_destinace}, CENA JIZDNEHO: {nova_cena},
NA TVUJ MAIL {email} JSME TI POSLALI LISTEK.""")
