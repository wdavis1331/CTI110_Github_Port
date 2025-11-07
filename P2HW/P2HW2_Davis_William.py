# William Davis
# 10/10/2025
# Grades Summary
# This program asks the user to enter six grades, stores them in a list,
# and displays the lowest grade, highest grade, sum, and average of the grades.

# Step 1: Get grades from user
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

# Step 2: Store grades in a list
grades_list = [mod1, mod2, mod3, mod4, mod5, mod6]

# Step 3: Perform calculations
lowest = min(grades_list)
highest = max(grades_list)
total = sum(grades_list)
average = total / len(grades_list)

# Step 4: Display results formatted neatly
print("\n----------Results----------")
print(f"Lowest Grade:     {lowest:.1f}")
print(f"Highest Grade:    {highest:.1f}")
print(f"Sum of Grades:    {total:.1f}")
print(f"Average:          {average:.2f}")
print("---------------------------")