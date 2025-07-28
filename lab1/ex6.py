# List of temperatures in Celsius
celsius_temps = [0, 20, 37, 100]

# Convert to Fahrenheit using map and lambda
fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))

print("Celsius:", celsius_temps)
print("Fahrenheit:", fahrenheit_temps)
