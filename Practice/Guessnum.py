import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize attempt counter
attempts = 0

# Welcome message
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Can you guess what it is?\n")

# Loop until user guesses correctly
while True:
    try:
        # Get user input
        guess = int(input("Enter your guess: "))
        
        # Validate input range
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.\n")
            continue
        
        attempts += 1
        
        # Check if guess is correct
        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed correctly!")
            print(f"The number was {secret_number}.")
            print(f"It took you {attempts} attempt(s) to win!\n")
            break
        elif guess < secret_number:
            print("Your guess is too low. Try again!\n")
        else:
            print("Your guess is too high. Try again!\n")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")
