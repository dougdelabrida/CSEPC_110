import random

magic_number = random.randint(1, 10) # calls a function to generate a random number from 1 to 10
user_guess_number = None
number_of_guesses = 0

while user_guess_number != magic_number: # runs until the guess number is equals to magic number
    user_guess_number = int(input("What is your guess? (From 1 to 10) ")) # adds a new value each time the loop is runned

    number_of_guesses += 1 # increases the value

    if user_guess_number == magic_number:
        print("You guessed it!")
        print(f"Number of guesses: {number_of_guesses}")

        keep_playing = input("Do youn want to keep playing? (yes/no) ")

        if (keep_playing == "yes"):
            magic_number = random.randint(1, 10)
            user_guess_number = None
            number_of_guesses = 0

    elif user_guess_number > magic_number:
        print("Lower")
    else:
        print("Higher")
