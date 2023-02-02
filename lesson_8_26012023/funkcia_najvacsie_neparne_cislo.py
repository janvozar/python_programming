#sude = parne
#liche = neparne

#najvacsie neparne cislo ([1,3,6, "fgsd"] )  - > 3
#najvacsie cislo = 0
# pre cisla v zozoname
    # pokial cislo je typu cislo A je neparne A je vacsie ako nejvacsie cislo
        # uloz do najvacsie cislo
    #vrat najvacsie cislo  

import doctest

def najvacsie_neparne_cislo (sekvencia):

    """
    >>> najvacsie_neparne_cislo (0,2)
    1.0 
    """


    najvacsie_neparne_cislo = 0
    for hodnota in sekvencia:
        if isinstance(hodnota, int) and hodnota % 2 and hodnota > najvacsie_neparne_cislo:
            najvacsie_neparne_cislo = hodnota
    return(najvacsie_neparne_cislo)
    print()

doctest.testmod()
