# List of names
names = ["Alice", "Bob", "Charlotte", "Daniel", "Eve", "Jonathan", "Mia"]

# Filter names longer than 5 characters
long_names = list(filter(lambda name: len(name) > 5, names))

print("Original names:", names)
print("Names with more than 5 characters:", long_names)
