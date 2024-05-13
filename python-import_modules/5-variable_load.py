#!/usr/bin/python3

def main():
    # Exécute le contenu du fichier variable_load_5.py
    with open('variable_load_5.py', 'r') as file:
        code = compile(file.read(), 'variable_load_5.py', 'exec')
        exec(code, globals())
        # Imprime la valeur de la variable 'a'
        print(a)

        if __name__ == "__main__":
            main()
