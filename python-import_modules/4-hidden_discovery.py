#!/usr/bin/python3
import importlib.util
import os

if __name__ == "__main__":
    # Identifier le chemin du fichier .pyc compilé
    pycache_path = '/tmp/__pycache__'
    chemin_module = None
    for file in os.listdir(pycache_path):
        if file.startswith('hidden_4') and file.endswith('.pyc'):
            chemin_module = os.path.join(pycache_path, file)
            break

    if chemin_module is None:
        raise FileNotFoundError("Le fichier hidden_4.pyc n'a pas été trouvé dans le répertoire __pycache__")

    # Charger le module compilé
    spec = importlib.util.spec_from_file_location("hidden_4", chemin_module)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Récupérer et trier les noms
    noms = [nom for nom in dir(module) if not nom.startswith("__")]
    noms.sort()  # Trier les noms par ordre alphabétique

    # Afficher les noms
    for nom in noms:
        print(nom)
