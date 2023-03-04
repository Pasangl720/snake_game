import random

def play_game():
    print("Welcome to the guessing game!")
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = input("Guess a number between 1 and 100: ")
        attempts += 1
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number")
            continue
        if guess == secret_number:
            print(f"Congratulations, you guessed the number in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Your guess is too low, try again!")
        else:
            print("Your guess is too high, try again!")
    play_again = input("Do you want to play again? (y/n)")
    if play_again.lower() == 'y':
        play_game()
    else:
        print("Thank you for playing the guessing game!")
        
play_game()
