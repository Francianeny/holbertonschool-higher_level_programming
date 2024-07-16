#!/usr/bin/python3

import os

def generate_invitations(template, attendees):
    """
    Generate and print invitations for each attendee.

    Parameters:
    template (str): The template string with placeholders.
    attendees (list): A list of dictionaries, each containing details of an attendee.
    """
    # Vérification des types d'entrée
    if not isinstance(template, str):
        print("Error: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return

    # Vérification des entrées vides
    if not template.strip():
        print("Error: template is empty.")
        return

    if not attendees:
        print("Error: attendees list is empty.")
        return

    for attendee in attendees:
        invitation = template.format(
            name=attendee["name"],
            event_title=attendee["event_title"],
            event_date=attendee["event_date"] if attendee["event_date"] else "TBD",
            event_location=attendee["event_location"]
        )
        print(invitation)
        print("-" * 40)  # Séparation entre les invitations


