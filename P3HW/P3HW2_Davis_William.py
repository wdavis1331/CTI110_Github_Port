# William Davis
# 10/25/2025
# Payroll Calculator
# This program calculates the gross pay for an employee, including overtime pay if applicable.


# Ask user for input
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Determine overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results
print("\n------------------------------------------------------------")
print(f"Employee Name: {employee_name}")
print("------------------------------------------------------------")
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("------------------------------------------------------------")
print(f"{hours_worked:<15.2f}${pay_rate:<14.2f}{overtime_hours:<15.2f}${overtime_pay:<14.2f}${regular_pay:<14.2f}${gross_pay:<14.2f}")
print("------------------------------------------------------------")