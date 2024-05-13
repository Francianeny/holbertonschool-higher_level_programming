#!/usr/bin/python3

import calculator_1

if __name__ == "__main__":
    a = 10
    b = 5

# Appeler les fonctions et afficher les résultats
print("{} + {} = {:.0f}".format(a, b, add(a, b)))
print("{} - {} = {:.0f}".format(a, b, sub(a, b)))
print("{} * {} = {:.0f}".format(a, b, mul(a, b)))
print("{} / {} = {:.0f}".format(a, b, div(a, b)))

