#Multi-Function Calculator
#Build a Python calculator called calculator.py that takes two numbers as input and performs all four basic arithmetic operations plus two advanced operations. The calculator must handle user input safely using type casting and display results clearly using f-strings.

#Requirements
#Use float(input()) to collect two numbers from the user
#Calculate and display: addition, subtraction, multiplication, division
#Calculate and display: floor division (//) and modulus (%)
#Round all results to 2 decimal places using round()
#Handle division by zero — if the second number is 0, display a friendly error message instead of crashing
#Display all results in a formatted table using f-strings

#########################################
# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations
addition = round(num1 + num2, 2)
subtraction = round(num1 - num2, 2)
multiplication = round(num1 * num2, 2)

# Display results
print("\n========== Calculator Results ==========")
print(f"Addition       : {addition}")
print(f"Subtraction    : {subtraction}")
print(f"Multiplication : {multiplication}")

# Check for division by zero
if num2 == 0:
    print("Division       : Error! Cannot divide by zero.")
    print("Floor Division : Error! Cannot divide by zero.")
    print("Modulus        : Error! Cannot divide by zero.")
else:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

    print(f"Division       : {division}")
    print(f"Floor Division : {floor_division}")
    print(f"Modulus        : {modulus}")

print("========================================")

