#!/usr/bin/python3

import random

# Générer un nombre aléatoire entre -10 et 10
number = random.randint(-10, 10)

# Vérifier si le nombre est différent de zéro
if number != 0:
    if number > 0:
        print(f"{number} is positive")
    else:
        print(f"{number} is negative")
else:
    print("0 is zero")
