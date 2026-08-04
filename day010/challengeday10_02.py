def is_leap(year):
    """Verifies if a given year is a leap year. This is one of mines"""
  
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# TODO add more code here
def days_in_month(year, month):
    """shows the correspondent days for a chosen month. This is one of mines"""

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
    leap_year = "not "
    if 0 < month < 13:
        days_of_month = month_days[month - 1]
        if month == 2 and is_leap(year):
            days_of_month += 1
            leap_year = ""
    else:
        return "The month you introduced was not found"

    days_month = f"{month_year[month - 1]} has {days_of_month} days.\n{year} is {leap_year}a leap year."
    return days_month


# Do not change the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(year, month)
print(days)
