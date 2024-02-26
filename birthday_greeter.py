"""
Module for identifying colleagues who need to be greeted with a birthday in the coming week.

This module contains the function get_birthday_greetings, which checks the list of colleagues
and determines whose birthdays fall on the next week from the current date.
"""

from datetime import datetime, timedelta

def get_birthday_greetings(colleagues_list):
    """
    Determines colleagues who should be greeted with a birthday in the coming week.
    
    Parameters:
    - colleagues_list (list): A list of dictionaries, where each dictionary contains a colleague's
      name and their birthday in the format "YYYY-MM-DD".
    
    Returns:
    - list: A list of names of colleagues whose birthdays fall in the next week.
    """

    today = datetime.now()
    week_later = today + timedelta(days=7)
    greetings_list = []

    for colleague in colleagues_list:
        birthday = datetime.strptime(colleague["birthday"], "%Y-%m-%d")
        birthday_this_year = birthday.replace(year=today.year)

        if today <= birthday_this_year <= week_later:
            greetings_list.append(colleague["name"])

    return greetings_list

# Test colleagues
colleagues = [
    {"name": "Alice", "birthday": "1983-12-29"},
    {"name": "Bob", "birthday": "1984-12-24"},
    {"name": "Charlie", "birthday": "1985-01-02"},
    {"name": "Igor", "birthday": "1985-03-02"},
]

# Function call and output of the result
print(get_birthday_greetings(colleagues))
