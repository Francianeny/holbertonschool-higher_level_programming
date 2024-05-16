#!/usr/bin/python3
import os
import imp

if __name__ == "__main__":
    chemin_module = '/tmp/hidden_4.pyc'

    if os.path.exists(chemin_module):
        nom_module = os.path.splitext(os.path.basename(chemin_module))[0]
        module = imp.load_compiled(nom_module, chemin_module)

        noms = [nom for nom in dir(module) if not nom.startswith("__")]
        noms.sort()  # Trier les noms par ordre alphabétique

        for nom in noms:
            print(nom)
