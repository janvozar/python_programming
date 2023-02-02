import doctest

def vypocet_priemernej_hodnoty(*args: int) -> float:
    """
    >>> vypocet_priemernej_hodnoty (0,1)
  
    """
    vysledok = []
    for hodnota in args:
        if isinstance(hodnota, int):
            vysledok.append(hodnota)
    return sum(vysledok)/len(vysledok)

print(vypocet_priemernej_hodnoty(1, 3, 6, "fghd"))

doctest.testmod(name="vypocet_priemernej_hodnoty",verbose=True)