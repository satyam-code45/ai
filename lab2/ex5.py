days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

num = int(input("Enter a number (1-7): "))

if 1 <= num <= 7:
    print("Day:", days[num-1])
else:
    print("Invalid input! Please enter a number between 1 and 7.")
