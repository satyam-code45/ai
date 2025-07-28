from datetime import datetime, date

# Take birthdate input from the user
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

# Convert string to date object
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

# Get today's date
today = date.today()

# Calculate age
age = today.year - birthdate.year

# Adjust if birthday hasn't occurred yet this year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

print(f"You are {age} years old.")
