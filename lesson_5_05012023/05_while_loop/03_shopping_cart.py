# https://learn.engeto.com/cs/kurz/python-while-cyklus/cviceni/SiAGhb48TAOF-EGYTjV5cQ/nakupni-kosik
# Zadané hodnoty
kosik = dict() # bude ve stejném formátu jako potraviny
oddelovac = "=" * 40
potraviny = {
    "mleko": [30, 5],  # index '0'-> cena, index '1' -> pocet
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10]
}
nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomenrac  |    15,-  |
+-----------+----------+
"""

# vypiš uvítání a obsah nabídky
# dokud uživatel nezadá q, ptej se jej na zboží:
# 	pokud se zboží nenachází v nabídce:
# 		vypiš, že zboží není v nabídce
# 	jinak pokud zboží ještě není v košíku a je v nabídce alespoň jeden kus:
# 		přidej jej do košíku
# 		z nabídky odečti jeden kus zboží -> tady jsme skoncili
# 	jinak pokud zboží již je v košíku  a je v nabídce alespoň jeden kus:
# 		přičti kus ke zboží v košíku
# 		z nabídky odečti jeden kus zboží
# 	jinak:
# 		vypiš, že zboží není v nabídce
# vypiš obsah košíku

print("Vitejte u naseho nakupniko kosiku!".center(len(oddelovac)))
print(oddelovac)
print(nabidka)



while (zbozi:=input("Zadavej zbozi, pro ukonceni stiskni `q`: ")) != "q":
    if zbozi not in potraviny:
        print(f"Zbozi {zbozi} neni v nabidce.")
    elif zbozi not in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi] = [potraviny[zbozi][0], 1]
    else:
        print("tada")
    
