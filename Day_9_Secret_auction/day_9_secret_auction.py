import os

def find_highest_bider(bidders):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidders:
        amount = bidders[bidder]
        if amount > highest_bid:
            highest_bid = amount
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


game_on = False
bidders = {}
while not game_on:
    name = input("What is your name? ")
    bid_amount = float(input("What's your bid? "))
    bidders[name] = bid_amount
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders == 'no':
        game_on = True
        find_highest_bider(bidders)
    elif more_bidders == 'yes':
        os.system('cls')


