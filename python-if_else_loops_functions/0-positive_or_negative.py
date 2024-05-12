#!/usr/bin/python3

import random

# Liste des nombres à utiliser comme référence pour la génération aléatoire
reference_numbers = [-4, 0, -3, -10, 10, -5, 6, 7, 5]

# Sélectionner aléatoirement un nombre parmi la liste de référence
number = random.choice(reference_numbers)

# Afficher le nombre généré avec sa polarité
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("0 is zero")
