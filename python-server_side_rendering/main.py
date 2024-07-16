#!/usr/bin/python3

# main.py lit le modèle d'invitation depuis le fichier templaxe.txt et appelle la fonction generate_invitations

from task_00_intro import generate_invitations

# Lire le modèle depuis un fichier
with open('template.txt', 'r', encoding='utf-8') as file:
    template_content = file.read()

# Liste des participants
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

# Appeler la fonction avec le modèle et la liste des participants
generate_invitations(template_content, attendees)
