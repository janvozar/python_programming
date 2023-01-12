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