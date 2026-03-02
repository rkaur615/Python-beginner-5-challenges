# Challenge 05 - Profile Card

# Collect user information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height_m = float(input("Enter your height in metres: "))
favorite_number = int(input("Enter your favourite number: "))

# Convert height to centimeters
height_cm = int(height_m * 100)

# Print formatted profile card
print("\n================================")
print("        YOUR PROFILE CARD")
print("================================")
print(f" Name:              {name}")
print(f" Age:               {age} years")
print(f" Height:            {height_m}m ({height_cm}cm)")
print(f" Favourite Number:  {favorite_number}")
print("================================")