#A countdown using while loop

count = 6

while count > 0:
    print(count)
    count = count - 1

print("Blast Off!!")

###building a simple rep counter
for rep in range(1, 6):
    print(f"This is rep no.{rep}")

###A guessing game
secret_word = "python"
while True:
    guess = input("Guess the programming language we are using: ").lower()
    if guess == secret_word:
        print("You guessed the correct language!")
        break
    else:
        print("Incorrect guess. Try again!")