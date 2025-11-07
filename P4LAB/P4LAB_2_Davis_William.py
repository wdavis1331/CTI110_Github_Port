#William Davis
#11/2/2025
# Multiplication Table Program
# This program prompts the user for an integer and displays its multiplication table from 1 to 12.

run_again = "yes"

while run_again.lower() == "yes":
    # Ask the user for an integer
    number = int(input("Enter an integer: "))

    # Check if the number is zero or higher
    if number >= 0:
        print(f"\nMultiplication Table for {number}")
        print("---------------------------")
        # Use a for loop to display the table from 1 to 12
        for i in range(1, 13):
            print(f"{number} x {i:2} = {number * i}")
    else:
        print("Sorry, I cannot accept negative values.")

    # Ask if the user wants to run again
    print()
    run_again = input("Do you wish to run the program again? (yes/no): ")

print("Thank you for using the program!")
