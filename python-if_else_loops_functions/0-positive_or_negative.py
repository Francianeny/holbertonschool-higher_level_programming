#!/usr/bin/python3

import random

# Générer un nombre aléatoire entre -10 et 10
number = random.randint(-10, 10)

# Si le nombre est zéro, ajuster en conséquence
if number == 0:
    if random.choice([True, False]):
        number += 1
    else:
        number -= 1

# Vérifier si le nombre est positif, négatif ou zéro
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("0 is zero")
