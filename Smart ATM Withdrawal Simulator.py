#The Challenge: “The Smart ATM Withdrawal Simulator”
#Simulate a bank transaction checking if a user has enough money.
#1. Set a fixed variable representing a bank balance, for example: balance = 500.
#2. Ask the user how much money they want to withdraw. (Remember to cast it to an integer or float!).
#3. If the request is less than or equal to the balance, deduct the amount and print:
#“Withdrawal successful! Remaining balance: RX”.
#4. But what if they try to withdraw a negative amount or zero? Add an elif statement checking if the request is less than or equal to 0. If so, print: “Invalid amount”. You must withdraw more than “R0”.
#5. Otherwise (else), print: “Declined. Insufficient funds”
#########################################################

# Smart ATM Withdrawal Simulator

# Set the initial bank balance
balance = 500

# Ask the user how much they want to withdraw
withdrawal = float(input("Enter the amount you want to withdraw (P): "))

# Check the withdrawal amount
if withdrawal <= 0:
    print("Invalid amount. You must withdraw more than P0.")
elif withdrawal <= balance:
    balance -= withdrawal
    print(f"Withdrawal successful! Remaining balance: P{balance:.2f}")
else:
    print("Declined. Insufficient funds.")