def is_leap(year):
    """Verifies if a given year is a leap year. This is one of mines"""
    leap=0
  
    if year % 4 ==0:
        if year % 100 ==0:
            if  year % 400 == 0:
                print("Leap year")
                leap = 1
            else:
                print("Not a leap year")
        else:
            print("Leap year")
            leap = 1
    else:
        print("Not a leap year")
    return leap
  
#TODO add more code here
def days_in_month(year, month):
    """shows the correspondent days for a chosen month. This is one of mines"""
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    month_year = ['January','Febrary', 'March', 'April', 'May', 'June', 'July', 'August', 'September','October','November','December']
    days_month = ""
    g_year = ""
  
    if month > 0 and month < 12:
        if month == 2 and is_leap(year)==1:
            days_month = month_year[month] + " has 29 days"
            g_year = str(year) + " is a " + str(is_leap(year))
        else:
            days_month = month_year[month-1] + " has " + str(month_days[month-1]) + " days"
            g_year = str(year) + " is not a " + str(is_leap(year))
        return days_month; g_year
    else:
        return "The month you introduced was not found"
      
#Do not change the code below
year = int(input())#Enter a year
month = int(input())#Enter a month
days = days_in_month(year, month)
print(days)
