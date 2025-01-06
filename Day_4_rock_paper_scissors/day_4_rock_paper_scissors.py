import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]
computer_move = random.choice(moves)
computer_index = moves.index(computer_move)

print("Welcome to the rock, paper, scissors game.")
player_move = int(input("Type 0 for rock, 1 for paper or 2 for scissors: "))

print(f"Computer choose: \n{computer_move}")
print("VS")
print(f"Player choose: \n{moves[player_move]}")

if player_move == computer_index:
    print("It is a tie")
elif player_move == 0 and computer_index == 2:
    print("Player wins")
elif player_move == 2 and computer_index == 0:
    print("Computer wins")
elif player_move > computer_index:
    print("Player wins")
elif player_move < computer_index:
    print("Computer wins wins")
