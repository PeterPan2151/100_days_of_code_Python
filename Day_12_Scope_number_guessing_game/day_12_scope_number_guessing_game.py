import art
import random


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5


def random_number():
    return random.randint(1, 100)


def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random_number()
    lives = set_difficulty()

    # print(f"The number is {number_to_guess}")
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number_to_guess:
            print("You got it!!")
            print(f"The answer was {number_to_guess}.")
            break
        elif guess > number_to_guess:
            print("Too high.")
            lives -= 1
        elif guess < number_to_guess:
            print("Too low")
            lives -= 1

        if lives == 0:
            print("You've run out of guesses try again.")
            break


game()


