#!/usr/bin/python3

import random

# Liste des nombres non nuls entre -10 et 10
non_zero_numbers = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sélectionner aléatoirement un nombre parmi la liste
number = random.choice(non_zero_numbers)

# Vérifier si le nombre est positif, négatif ou zéro
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("0 is zero")
