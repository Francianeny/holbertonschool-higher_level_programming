#!/usr/bin/python3

# Assigner les valeurs aux variables a et b
a = 1
b = 2

# Importer la fonction add depuis add_0.py
add_module = __import__('add_0')
add = add_module.add

# Afficher le résultat de l'addition
print('{} + {} = {}'.format(a, b, add(a, b)))
