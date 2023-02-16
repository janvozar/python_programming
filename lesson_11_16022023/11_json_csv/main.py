import sys

print("seznam:", sys.argv)

if len(sys.argv) != 2:
    print(f"Soubor: {sys.argv[0]} potřebuje povinný argument se jménem textového souboru")
elif not sys.argv[1].endswith(".txt"):
    print(f"Soubor: {sys.argv[1]} neni textovy soubor!")
else:
    print("Spoustim soubor!")