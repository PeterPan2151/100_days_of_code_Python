import art
import game_data
import random
import os


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


print(art.logo)
a_option = random.choice(game_data.data)
score = 0

game_on = True
while game_on:
    b_option = random.choice(game_data.data)
    if b_option == a_option:
        b_option = random.choice(game_data.data)

    print(f"Compare A: {format_data(a_option)}")
    print(art.vs)
    print(f"Compare B: {format_data(b_option)}")

    more_followers = input("Who has more followers? Type 'a' or 'b': ").lower()
    a_follower_count = a_option["follower_count"]
    b_follower_count = b_option["follower_count"]
    is_correct = check_answer(more_followers, a_follower_count, b_follower_count)

    if is_correct:
        os.system('cls')
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_on = False

    a_option = b_option


