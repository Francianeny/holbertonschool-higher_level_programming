#!/usr/bin/python3

import random

# Initialiser le nombre à zéro pour commencer la boucle
number = 0

# Continuer à générer un nombre aléatoire jusqu'à ce qu'il soit différent de zéro
while number == 0:
    number = random.randint(-10, 10)

# Vérifier si le nombre est positif, négatif ou zéro
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("0 is zero")
