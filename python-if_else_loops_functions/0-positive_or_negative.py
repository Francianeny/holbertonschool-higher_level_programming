#!/usr/bin/python3

numbers = [5, -7, 0, 10, -5]  # Liste des nombres prédéfinis

for number in numbers:
    if number > 0:
        print(f"{number} is positive")
    elif number == 0:
        print("0 is zero")
    else:
        print(f"{number} is negative")
