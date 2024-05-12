#!/usr/bin/python3

# Importer les fonctions du module calculator_1.py
from calculator_1 import add, sub, mul, div

# Définir les valeurs des variables a et b
a = 10
b = 5

# Appeler chaque fonction importée et imprimer les résultats
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
