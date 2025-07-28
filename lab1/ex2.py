from datetime import datetime

# Get current date
current_date = datetime.now()

# Format the date as Day-Month-Year
formatted_date = current_date.strftime("%d-%b-%Y")

print("Current date:", formatted_date)
