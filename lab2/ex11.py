numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
even_numbers = [x for x in numbers if x % 2 == 0]

print("Even numbers:", even_numbers)
