#filter_slov(["apple", "banana", "Ant", "book"], 'A', False) -> ["apple","Ant"]

# pre kazde slovo v zozname
    #pokial je prve pismeno slova rovnake ako zadane pismeno alebo
    #pokial nie je case sensitive
    #skontroluj, ci sa rovna prve pismeno slova zadanemu prvemu pismenu bez ohladu na velikost
        #pridaj slovo do noveho zoznamu
#vrat novy zoznam


def filter_slov(slovo: list, prve_pismeno: str, case_sensitive = True): -> list:
    vysledok = []
    for slovo in slova:
        rovnake_pismeno = slovo[0].upper() == prve_pismeno.upper
        if slovo[0] != prve_pismeno:
            continue
        elif not case_sensitive and rovnake_pismeno:
            vysledok.append(slovo)
        elif slovo[0] == prve_pismeno:
            vysledok.append(slovo)
    return vysledok




        #(not case_sensitive and rovnake_pismeno):