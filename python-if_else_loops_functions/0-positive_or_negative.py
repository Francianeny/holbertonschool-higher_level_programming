#!/usr/bin/python3

import random

# Initialisation du nombre à zéro
number = 0

# Générer un nombre aléatoire jusqu'à ce qu'il soit différent de zéro
while number == 0:
    number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")
else:
    print(f"{number} is negative")
