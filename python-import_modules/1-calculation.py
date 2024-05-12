#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    return (a + b)


def sub(a, b):
    """My subtraction function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)


def mul(a, b):
    """My multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)


def div(a, b):
    """My division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return a / b

# Définir les valeurs pour a et b
a = 10
b = 5

# Appeler les fonctions et afficher les résultats
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} / {b} = {div(a, b)}")
