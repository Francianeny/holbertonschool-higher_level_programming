#!/usr/bin/python3

import random

# Initialisation du générateur de nombres aléatoires avec une valeur fixe
random.seed(0)

number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print("0 is zero")
else:
    print(f"{number} is negative")
