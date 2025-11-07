# William Davis
# 10/03/2025
# Vehicle MPG Calculator
# This program stores vehicle MPG values in a dictionary, allows the user
# to select a vehicle, enter miles to drive, and calculates the gallons of gas needed.

# Create dictionary with vehicle MPG
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Create variable holding all the keys
keys = vehicle_mpg.keys()

# Print the keys
print("Available vehicles:", keys)

# Prompt user to enter a vehicle
vehicle_choice = input("Enter a vehicle from the list above (case-sensitive): ")

# Display MPG for the chosen vehicle
mpg = vehicle_mpg[vehicle_choice]
print(f"{vehicle_choice} has an MPG of {mpg}")

# Prompt user to enter the number of miles
miles = float(input(f"Enter the number of miles you will drive the {vehicle_choice}: "))

# Calculate gallons needed
gallons_needed = miles / mpg

# Display gallons needed, rounded to 2 decimal places
print(f"Gallons of gas needed: {gallons_needed:.2f}")

