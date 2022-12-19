"""
projekt_1.py: prvy projekt do Engeto Online Python Akademie
author: Ján Vozár 
email: jan.vozar@gmail.com
discord: johnyv#1474
"""

"""
1.vyžádá si od uživatele přihlašovací jméno a heslo,
2.zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
3.pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
4.pokud není registrovaný, upozorni jej a ukonči program.**

Registrováni jsou následující uživatelé:

+------+-------------+
| user |   password  |
+------+-------------+
| bob  |     123     |
| ann  |   pass123   |
| mike | password123 |
| liz  |   pass123   |
+------+-------------+

5.program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS:

6.pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
7.pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
8.pro vybraný text spočítá následující statistiky:

a)počet slov,
b)počet slov začínajících velkým písmenem,
c)počet slov psaných velkými písmeny,
d)počet slov psaných malými písmeny,
e)počet čísel (ne cifer),
f)sumu všech čísel (ne cifer) v textu.

"""
LINE = "=" * 35
TEXTS = ["abc"]
REGISTRED_USERS = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"} 

user = input("User name:")

def user_verification:

print(f"Unregistered user"{user}".Terminating the program,")

print(f"Welcome to the app" {user})
print(f"We have 3 texts to be analyzed.")
number=input("Enter a number btw. 1 and 3 to select:")

def word_counter:
    for word in text.split(" "): 
        if word in word_counts: 
            word_counts[word]+= 1 
        else: 
            word_counts[word]= 1 
    return word_counts 

def titlecase_word_counter:

def uppercase_word_counter:

def lowercase_word_counter:

def number_counter:

def sum_number:


print(f"Selected number is not in range.Terminating the program,")
print(f"Input is not recognized.Terminating the program,")

print(f"There are" {number_of_words} "words in the selected text.")
print(f"There are" {number_of_titlecase_words} "titlecase words.")
print(f"There are" {number_of_uppercase_words} "uppercase words.")
print(f"There are" {number_of_lowercase_words} "lowercase words.")
print(f"There are" {number of numbers} "numbers.")
print(f"The sum of all the numbers" {sum_of_numbers})