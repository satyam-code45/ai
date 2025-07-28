import calendar

def is_leap(year):
    return calendar.isleap(year)

# Take year as input from the user
year_input = int(input("Enter a year: "))

# Check and print whether it's a leap year
if is_leap(year_input):
    print(f"{year_input} is a leap year.")
else:
    print(f"{year_input} is not a leap year.")
