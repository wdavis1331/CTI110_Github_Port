# William Davis 
# 10/08/2025
# Travel Expenses Program
# This program calculates and displays travel expenses.

print("This program calculates and displays travel expenses")

# Get user inputs
budget = float(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")

fuel = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

# Calculate remaining balance
remaining_balance = budget - (fuel + accommodation + food)

# Display results
print("\n------------Travel Expenses------------")
print(f"{'Location:':20}{destination}")
print(f"{'Initial Budget:':20}${budget:,.2f}")
print(f"{'Fuel:':20}${fuel:,.2f}")
print(f"{'Accommodation:':20}${accommodation:,.2f}")
print(f"{'Food:':20}${food:,.2f}")
print("---------------------------------------")
print(f"{'Remaining Balance:':20}${remaining_balance:,.2f}")
3000