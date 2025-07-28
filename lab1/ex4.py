from datetime import datetime

# Take date input from the user
date_str = input("Enter a date (YYYY-MM-DD): ")

# Convert to datetime object
date_obj = datetime.strptime(date_str, "%Y-%m-%d")

# Get weekday name
day_of_week = date_obj.strftime("%A")

print(f"{date_str} falls on a {day_of_week}.")
