# grade_report.py

# Task Overview
# Extend the Unit 5 grade classifier into a full grade report generator.
# The program processes a list of student dictionaries,
# calculates averages, assigns grades and pass/fail status,
# generates a class summary, and allows the user to search for students.

# Requirements
# • Store at least 5 students as a list of dictionaries:
#   [{name, maths, english, science}, ...]
# • Use a for loop to iterate over all students and calculate each student's average.
# • Apply the grade/status logic from Unit 5 inside the loop.
# • Build a results list of dictionaries containing:
#   name, average, grade, status.
# • After the main loop, calculate:
#   class average, highest mark, lowest mark.
# • Display a formatted class report showing individual results and class statistics.
# • Use a while loop to let the user search for a student by name after the report is shown.

# Store student data
students = [
    {"name": "Amara", "maths": 85, "english": 78, "science": 90},
    {"name": "Bela", "maths": 65, "english": 72, "science": 68},
    {"name": "Lerato", "maths": 45, "english": 58, "science": 50},
    {"name": "Amantle", "maths": 95, "english": 88, "science": 92},
    {"name": "Beauty", "maths": 35, "english": 42, "science": 38}
]

# Store processed results
results = []

# Variables for class statistics
total_average = 0
highest_average = 0
lowest_average = 100

# Process each student
for student in students:

    average = (student["maths"] + student["english"] + student["science"]) / 3

    # Determine grade
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Determine pass/fail
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    # Save processed results
    results.append({
        "name": student["name"],
        "average": round(average, 2),
        "grade": grade,
        "status": status
    })

    # Update class statistics
    total_average += average

    if average > highest_average:
        highest_average = average

    if average < lowest_average:
        lowest_average = average

# Calculate class average
class_average = total_average / len(students)

# Display report
print("\n========== CLASS REPORT ==========")

for result in results:
    print(f"Name    : {result['name']}")
    print(f"Average : {result['average']}")
    print(f"Grade   : {result['grade']}")
    print(f"Status  : {result['status']}")
    print("-------------------------------")

print("\n====== CLASS STATISTICS ======")
print(f"Class Average : {round(class_average,2)}")
print(f"Highest Average : {round(highest_average,2)}")
print(f"Lowest Average : {round(lowest_average,2)}")

# Search section
while True:
    search = input("\nEnter a student name to search (or type 'exit' to quit): ")

    if search.lower() == "exit":
        print("Program ended.")
        break

    found = False

    for result in results:
        if result["name"].lower() == search.lower():
            print("\nStudent Found")
            print(f"Name    : {result['name']}")
            print(f"Average : {result['average']}")
            print(f"Grade   : {result['grade']}")
            print(f"Status  : {result['status']}")
            found = True
            break

    if not found:
        print("Student not found.")