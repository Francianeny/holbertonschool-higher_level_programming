#!/usr/bin/python3

# 0-import_add.py

# Importer la fonction add depuis add_0.py
from add_0 import add

# Assigner les valeurs aux variables a et b
a = 1
b = 2

# Calculer le résultat de l'addition
result = add(a, b)

# Afficher le résultat avec le format requis
print('{} + {} = {}'.format(a, b, result))
