# Challenge 04 - Shopping Receipt

# Get item 1
item1 = input("Enter item 1 name: ")
price1 = float(input("Enter item 1 price: "))

# Get item 2
item2 = input("Enter item 2 name: ")
price2 = float(input("Enter item 2 price: "))

# Get item 3
item3 = input("Enter item 3 name: ")
price3 = float(input("Enter item 3 price: "))

# Calculate total
total = price1 + price2 + price3

# Print receipt
print("\n---------------------------")
print(f"{item1:<15} ${price1:>6.2f}")
print(f"{item2:<15} ${price2:>6.2f}")
print(f"{item3:<15} ${price3:>6.2f}")
print("---------------------------")
print(f"{'TOTAL':<15} ${total:>6.2f}")
print("---------------------------")