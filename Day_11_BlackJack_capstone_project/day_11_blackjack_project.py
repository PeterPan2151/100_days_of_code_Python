import random
import os
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(player_card_list):
    if len(player_card_list) == 2 and sum(player_card_list) == 21:
        return 0

    if 11 in player_card_list and sum(player_card_list) > 21:
        player_card_list.append(1)
        player_card_list.remove(11)

    return sum(player_card_list)


def compare(user_points, computer_points):
    if user_points == computer_points:
        return "Draw"
    elif computer_points == 0:
        return "Loose Computer has a black jack!"
    elif user_points == 0:
        return "Win Player has a black jack!"
    elif user_points > 21:
        return "You went over, you loose."
    elif computer_points > 21:
        return "Computer over 21, you win."
    else:
        if user_points > computer_points:
            return "You win"
        else:
            return "You loose"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("Do you want to draw another card? Type 'y' or 'n': ")
            if another_card == 'y':
                user_cards.append(deal_card())
            elif another_card == 'n':
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y':
    os.system('cls')
    play_game()



