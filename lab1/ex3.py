from datetime import datetime

# Take two dates as input in YYYY-MM-DD format
date_str1 = input("Enter the first date (YYYY-MM-DD): ")
date_str2 = input("Enter the second date (YYYY-MM-DD): ")

# Convert strings to datetime objects
date1 = datetime.strptime(date_str1, "%Y-%m-%d").date()
date2 = datetime.strptime(date_str2, "%Y-%m-%d").date()

# Calculate the difference
delta = abs((date1 - date2).days)

print(f"Number of days between {date1} and {date2} is: {delta}")
