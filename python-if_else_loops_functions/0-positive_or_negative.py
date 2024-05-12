#!/usr/bin/python3

import random

# Générer un nombre aléatoire entre -10 et 10
number = 0
while number == 0:
    number = random.randint(-10, 10)

# Vérifier si le nombre est positif, négatif ou zéro
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("0 is zero")
