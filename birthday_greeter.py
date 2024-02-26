"""
Module for identifying colleagues who should be greeted with their birthdays in the upcoming week.

This module includes a function that checks a list of users with their names and birthdays,
determines whose birthdays fall into the next week, 
and prints a list of these users organized by the day of the week.
"""

from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users_list):
    """
    Prints a list of users to be greeted with their birthdays in the upcoming week.

    Args:
    - users (list): A list of dictionaries, each containing 'name' and 'birthday' of a user.
                    'birthday' should be a datetime object.
    
    The function calculates which users have their birthdays in the next week from today,
    and prints their names grouped by the weekday of their birthday. 
    If a birthday falls on a weekend, it's moved to Monday.
    """
    today = datetime.now().date()  # Current date as a datetime.date object
    one_week_ahead = today + timedelta(days=7)
    birthdays = defaultdict(list)

    for user in users_list:
        name = user["name"]
        # Ensure birthday is a datetime.date object for comparison
        birthday = user["birthday"].date()  # Use .date() for conversion

         # Adjust the year of the birthday to this year for comparison
        birthday_this_year = birthday.replace(year=today.year)

        # If this year's birthday has already passed, consider next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Compare with current date and date a week ahead
        if today <= birthday_this_year <= one_week_ahead:
            # Determine the weekday for the birthday
            day_of_week = birthday_this_year.strftime("%A")
            if birthday_this_year.weekday() >= 5:  # Moving weekends to Monday
                day_of_week = "Monday"
            birthdays[day_of_week].append(name)

    # Printing the result
    for day, names in birthdays.items():
        print(f"{day}: {', '.join(names)}")

# Example usage
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Ivan Koum", "birthday": datetime(1984, 3, 3)},
]

get_birthdays_per_week(users)
