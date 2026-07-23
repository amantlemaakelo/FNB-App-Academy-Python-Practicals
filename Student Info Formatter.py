#Student Info Formatter
#Write a Python script called student_info.py that collects personal information from the user and displays it in a formatted profile card. The program must demonstrate correct use of all four data types, string manipulation, arithmetic, and the f-string output format.
#
#Requirements
#Use input() to collect: first name, surname, age (as an integer), and a favourite number (as a float)
#Display a formatted greeting using an f-string: ‘Welcome, [Full Name]!’
#Display the name in UPPERCASE using .upper() and in Title Case using .title()
#Calculate and display the age in months (age × 12)
#Round the favourite number to 2 decimal places using round()
#Print the data type of each collected value using type()
## string_formatter.py
################################################################
# Collect user input
# student_info.py

# Collect user information
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
favourite_number = float(input("Enter your favourite number: "))

# Full name
full_name = f"{first_name} {surname}"

# Age in months
age_months = age * 12

# Display profile
print("\n========== STUDENT PROFILE ==========")
print(f"Welcome, {full_name}!")
print(f"Name in UPPERCASE : {full_name.upper()}")
print(f"Name in Title Case: {full_name.title()}")
print(f"Age               : {age} years")
print(f"Age in Months     : {age_months}")
print(f"Favourite Number  : {round(favourite_number, 2)}")

# Display data types
print("\nData Types")
print(f"First Name       : {type(first_name)}")
print(f"Surname          : {type(surname)}")
print(f"Age              : {type(age)}")
print(f"Favourite Number : {type(favourite_number)}")
print("=====================================")