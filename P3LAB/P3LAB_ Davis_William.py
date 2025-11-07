# William Davis
# 10/15/2025
# Assignment: Money Breakdown Program
# This program takes a money value and calculates the most efficient number 
# of dollars, quarters, dimes, nickels, and pennies needed.

# Get user input
amount = float(input("Enter an amount of money: "))

# Convert to cents to avoid floating-point rounding errors
cents = int(round(amount * 100))

# Calculate dollars and coins
dollars = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

# Display results 
if dollars > 0:
    print(f"{dollars} dollar" + ("s" if dollars > 1 else ""))

if quarters > 0:
    print(f"{quarters} quarter" + ("s" if quarters > 1 else ""))

if dimes > 0:
    print(f"{dimes} dime" + ("s" if dimes > 1 else ""))

if nickels > 0:
    print(f"{nickels} nickel" + ("s" if nickels > 1 else ""))

if pennies > 0:
    # "penny" → "pennies"
    if pennies == 1:
        print("1 penny")
    else:
        print(f"{pennies} pennies")
