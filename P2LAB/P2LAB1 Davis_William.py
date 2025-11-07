# Davis, William
# 10/01/2025
# Circle Calculator
# This program calculates the diameter, circumference, and area of a circle
# based on a radius provided by the user, and formats the results.

import math

# Ask user for radius
radius = float(input("Enter the radius of the circle: "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display results with specified formatting
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")
