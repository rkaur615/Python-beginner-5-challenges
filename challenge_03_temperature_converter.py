# Challenge 03 - Temperature Converter

# Ask the user for temperature in Celsius
celsius = input("Enter temperature in Celsius: ")

# Convert to float
celsius = float(celsius)

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print result rounded to 2 decimal places
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")