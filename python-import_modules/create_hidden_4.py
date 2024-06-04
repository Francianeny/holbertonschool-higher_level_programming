#!/usr/bin/python3

import compileall
import os

# Écrire le code source dans /tmp/hidden_4.py
source_code = '''def foo():
    print("foo")

def bar():
    print("bar")

def baz():
    print("baz")

def __hidden__():
    print("hidden")

a = 1
b = 2
c = 3
__d = 4
'''

with open('/tmp/hidden_4.py', 'w') as f:
    f.write(source_code)

# Compiler le fichier source en .pyc
compileall.compile_file('/tmp/hidden_4.py', force=True)

# Vérifier si le fichier .pyc a été créé
pycache_path = '/tmp/__pycache__'
if os.path.exists(pycache_path):
    compiled_files = os.listdir(pycache_path)
    print("Compiled files in __pycache__:", compiled_files)
else:
    print("Directory __pycache__ not found")
