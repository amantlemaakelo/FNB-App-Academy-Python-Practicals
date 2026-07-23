
# South African Fuel Cost Calculator
#The Challenge: “The South African Fuel Cost Calculator”
#With petrol prices shifting, drivers want to calculate travel costs. Create a quick calculator:
#1. Ask the user how many kilometers they want to drive.
#2. Ask them for the current petrol price per liter (this can be a decimal, like R22.45).
#3. Assume their car uses exactly 1 liter of fuel for every 10 kilometers driven.
#(Formula: liters_needed = kilometers / 10).
#4. Calculate the total cost (liters_needed * petrol_price).

#5. Use type casting to ensure your numbers work, and use round() to format the
#final cost to 2 decimal places.
# Ask the user for the distance to travel
#################################################
kilometers = float(input("Enter the number of kilometers you want to drive: "))

# Ask the user for the petrol price per liter
petrol_price = float(input("Enter the current petrol price per liter (R): "))

# Calculate liters of fuel needed
liters_needed = kilometers / 10

# Calculate the total fuel cost
total_cost = liters_needed * petrol_price

# Display the results
print("\n===== Fuel Cost Calculator =====")
print(f"Distance to travel : {kilometers} km")
print(f"Petrol price       : R{petrol_price}")
print(f"Fuel needed        : {round(liters_needed, 2)} liters")
print(f"Total fuel cost    : R{round(total_cost, 2)}")
print("================================")