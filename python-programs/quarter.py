# Imports
from datetime import *

# Global variables
today_date = date.today()


# Create customise ordinal for the day
def get_ordinal(d):
    if d == 1 or d == 11 or d == 21 or d == 31:
        return "st"
    elif d == 2 or d == 12 or d == 22:
        return "nd"
    elif d == 3 or d == 23:
        return "rd"
    else:
        return "th"


# Convert month integer into month name
def create_month_word():
    return today_date.strftime("%B")


# Create a quarter from today's date
def create_quarter():
    if month in range(1, 4):
        return "Q1"
    elif month in range(4, 7):
        return "Q2"
    elif month in range(7, 10):
        return "Q3"
    else:
        return "Q4"


# Break date for customization
month = date.today().month
day = date.today().day
year = date.today().year

# Output
print("\nHere is today's date")
print("----------------------")
# Format the date correctly
date_msg = "Today's date is: {}{} {} {}"
print(date_msg.format(day, get_ordinal(day), create_month_word(), year))
print("Current quarter:", create_quarter())
