# Vstupní proměnné
oddelovac = "=" * 62
uzivatele = {"tomas", "petr", "marek"}
sluzby = ("dostupne filmy", "detaily filmu", "reziseri")
film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
    )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}

# Společný slovník 'filmy'

ceny = {"jablko":10}

filmy = {
    film_1["JMENO"]: film_1,
    film_2["JMENO"]: film_2,
    film_3["JMENO"]: film_3,
    film_4["JMENO"]: film_4,
    }

print(filmy["The Prestige"])

uzivatel = input("Zadej jmeno: ")

if uzivatel in uzivatele:
    print("V pořádku!")
    print(oddelovac)
    print("Vítejte v našem filmovém slovníku!".upper().center(len(oddelovac)))
    print(oddelovac)
    print("|".join(sluzby).center(len(oddelovac)))
    print(oddelovac)
else:
    print("Neregistrovaný uživatel!")
    quit()

vyber = input("Vyber sluzby: ")

if vyber == "dostupne filmy":
    print("Dostupné filmy: ")
    print(", ".join(filmy.keys()))
    print(oddelovac)

# PRIKLAD PSEUDOKODU
# pokud bude vyber uzivatele "detaily filmu":
#   ziskej od uživatele název filmu
#   vyhledej ve slovniku s filmy zadaný film podle jména
#   vytiskni jmeno tohoto filmu (jinak "Takovy film neni ve slovniku")
#   vytiskni oddelovac
# pokud bude vyber uzivatele "reziseri":
#   vyhledej pod kazdym filmem ve slovniku s filmy jmeno rezisera
#   vytiskni jména režiséru (každého jen jednou), která budou spojena čárkou
#   vytiskni oddelovac
# jinak:
#   vytiskni "Vybrana sluzba neni v nabidce, ukoncuji.."

elif vyber == "detaily filmu":
    film = input("Vyber film: ")
    film_detail = filmy.get(film, "Takovy film neni ve slovniku")
    print(film_detail)
    print(oddelovac)
elif vyber == "reziseri":
    reziseri = (
      filmy["Shawshank Redemption"]["REZISER"],
      filmy["The Godfather"]["REZISER"],
      filmy["The Dark Knight"]["REZISER"],
      filmy["The Prestige"]["REZISER"]
    )
    print(", ".join(set(reziseri)))
    print(oddelovac)
else:
    print("Vybrana sluzba neni v nabidce, ukoncuji..")