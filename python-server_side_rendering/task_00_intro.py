#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    try:
        # Vérification du type de template
        if not isinstance(template, str):
            raise TypeError("Template should be a string.")

        # Vérification si attendees est une liste de dictionnaires
        if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
            raise TypeError("Attendees should be a list of dictionaries.")

        # Vérification si le template est vide
        if not template.strip():
            raise ValueError("Template is empty, no output files generated.")

        # Vérification si la liste attendees est vide
        if not attendees:
            raise ValueError("No data provided, no output files generated.")

        # Génération des invitations
        for idx, attendee in enumerate(attendees, start=1):
            # Création d'une copie du template
            invitation = template[:]

            # Remplacement des placeholders avec les valeurs des dictionnaires attendee
            for placeholder in ["name", "event_title", "event_date", "event_location"]:
                value = attendee.get(placeholder, "N/A")
                if value is None:
                    value = "N/A"
                invitation = invitation.replace(f"{{{placeholder}}}", str(value))

            # Définition du nom du fichier de sortie
            output_filename = f"output_{idx}.txt"

            # Écriture de l'invitation dans le fichier de sortie
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(invitation)

        print(f"{len(attendees)} invitation files generated.")

    except TypeError as e:
        print(f"Error: {e}")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    template = "Hello {name}, You are invited to {event_title} on {event_date} at {event_location}."
    attendees = [
        {"name": "Alice", "event_title": "Party", "event_date": "2024-07-31", "event_location": "Paris"},
        {"name": "Bob", "event_title": "Conference", "event_date": "2024-08-15", "event_location": "New York"},
        {"name": "Charlie", "event_title": "Meeting", "event_location": "London"}
    ]

    generate_invitations(template, attendees)









