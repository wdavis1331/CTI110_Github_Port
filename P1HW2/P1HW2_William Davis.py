# William Davis
# 09/22/2025
# Travel Budget Calculator
# This program asks the user for their budget, destination, and expected
# expenses, then calculates how much money they will have left after the trip.

# Ask user to enter their budget
budget = float(input("Enter your total budget: "))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask user for amount they will spend on gas
gas = float(input("Enter the amount you will spend on gas: "))

# Ask user for amount they will spend on accommodation
accommodation = float(input("Enter the amount you will spend on accommodation: "))

# Ask user for amount they will spend on food
food = float(input("Enter the amount you will spend on food: "))

# Add expenses
total_expenses = gas + accommodation + food

# Subtract expenses from budget
remaining_balance = budget - total_expenses

# Display results
print("\nTravel Summary")
print("-------------------")
print(f"Destination: {destination}")
print(f"Budget: ${budget:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")
