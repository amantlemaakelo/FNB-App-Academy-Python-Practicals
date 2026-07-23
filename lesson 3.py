num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

#'Hello' + 'World' = 'HelloWorld'
# "5 + 3" = "53"
print(num1 + num2)
print(int(num1) + int(num2))

# Core Data Types
# str : String/Text "hello" "asfg#fm"
# int : Integer or whole numbers
# float : Floating-point 5.0
# bool : Boolean True/

#Calculating the bill
bill = float(input("Enter the total bill amount: P"))
tip = 0.15  # Calculate 15% tip
val_tip = bill * tip
total_amount = bill + val_tip
print(f"Here is the tip: P{val_tip}")
print(f"Here is the tip:{round(val_tip, 2)} rounded")

print(f"Here is the total amount: {total_amount}")
print(f"Here is the tip: {round(val_tip, 2)} rounded")

