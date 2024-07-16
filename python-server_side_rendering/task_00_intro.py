#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    """
    Generate and write invitations for each attendee to a separate file.

    Parameters:
    template (str): The template string with placeholders.
    attendees (list): A list of dictionaries, each containing details of an attendee.
    """
    # Vérification des types d'entrée
    if not isinstance(template, str):
        print("Error: Invalid input type. Template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Invalid input type. Attendees must be a list of dictionaries.")
        return

    # Vérification des entrées vides
    if not template.strip():
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        invitation = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A") if attendee.get("event_date") else "TBD",
            event_location=attendee.get("event_location", "N/A")
        )
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.write(invitation)






