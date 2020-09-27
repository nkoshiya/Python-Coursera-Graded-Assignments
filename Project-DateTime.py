"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    year1 = year
    month1 = month
    if month == 12:
        month2 = 1
        year2 = year1 +1
    else:
        year2 = year1
        month2 = month + 1
    try:    
        date1 = datetime.date(year1, month1, 1)
        date2 = datetime.date(year2, month2, 1)
    except ValueError:
        return 0
    diff = date2 - date1
    days = diff.days
    return days


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    month_day = days_in_month(year, month)
    if(1 <= year <= 9999)and(1 <= month <= 12)and(1 <= day <= month_day):
        return True
    else:
        return False    

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    valid1 = is_valid_date(year1, month1, day1)
    valid2 = is_valid_date(year2, month2, day2)

    if not(valid1 and valid2):
        return 0
    else:
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)             
    if(date2 > date1):
        diff = date2 - date1
        return diff.days
    else:
        return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    
    if is_valid_date(year, month, day):
        date1 = datetime.date(year, month, day)
        year1 = date1.year
        month1 = date1.month
        day1 = date1.day

        year2 = datetime.date.today().year
        month2 = datetime.date.today().month
        day2 = datetime.date.today().day
    
        age_days = days_between(year1, month1, day1, year2, month2, day2)
        return age_days
    else:
        return 0