# soubor muj_modul.py

def hlavni_funkce():
    funkce_1()
    funkce_2()
    funkce_3()
def funkce_1():
    print("Spouštění první funkce...")
def funkce_2():
    """Funkce, kterou potřebuješ."""
    print("Spouštění druhé funkce...")
def funkce_3():
    print("Spouštění třetí funkce...")


print("__name__pro modul.py:")
print(__name__)

print("Nahrávání modulu..")
hlavni_funkce()


# if __name__ == "__main__":
#     print("Nahrávání modulu..")
#     hlavni_funkce()
# else:
#     print("Spouštění souboru..")