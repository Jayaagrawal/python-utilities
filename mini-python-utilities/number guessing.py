#-Number guessing game Problem: Write a program where the computer randomly selects a number between 1 and 20. 
# The user guesses the number, and the program tells them if they are correct or not.


import random
# Ask user for range
max_range = int(input("Enter the maximum number for the range: "))

# Generate random number within that range
number = random.randint(1, max_range)

print(f"Guess the number between 1 and {max_range}!")

while True:  # loop until correct guess
    guess = int(input("Enter your guess: "))

    # Out of range check
    if guess < 1 or guess > max_range:
        print("❌ That guess is out of range. Try again.")
        continue

    # Correct guess
    if guess == number:
        print(" Kudoz! You guessed it right.")
        break

    # Feedback for wrong guesses
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")