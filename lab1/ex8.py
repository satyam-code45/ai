# Original list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter odd numbers, then square them
odd_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))

print("Original list:", numbers)
print("Squares of odd numbers:", odd_squares)
