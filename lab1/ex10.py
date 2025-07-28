# Two lists of numbers
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

# Use map and lambda to sum elements at the same position
summed_list = list(map(lambda x, y: x + y, list1, list2))

print("List 1:", list1)
print("List 2:", list2)
print("Summed list:", summed_list)
