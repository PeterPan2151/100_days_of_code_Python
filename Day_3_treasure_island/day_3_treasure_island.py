# This project consist of an choose your own adventure game using if blocks for conditional apporvals.

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction_choice = input("You're at a cross road. Where do you want to go?\n\tType \"left\" or \"right\": ").lower()
if direction_choice == "left":
    print("You kept running and arrive at a lake. There is a house on the middle.")
    lake_choice = input("Will tou wait for a boat or swi across?\n\tTpe \"wait\" or \"swim\": ").lower()
    if lake_choice == "wait":
        print("You waited for a boat, great choice, you avoided the sharks. You arrive unharmed and enter the house, "
              "in the main room there are 3 doors, one red, one blue and one yellow.")
        door_choice = input("Which door are you choosing?\n\tType \"red\" or \"blue\" or \"yellow\": ").lower()
        if door_choice == "red":
            print("You enter the red room, there is no light, but you know you are not alone. A light "
                  "goes on and you are surrounded by 4 hungry tigers. Bon Appetit. Game Over")
        elif door_choice == "blue":
            print("Great choice, blue is my favorite color. And guess what? The treasure is right in front of you. "
                  "Great job, You Win!!")
        elif door_choice == "yellow":
            print("You enter the yellow room. There is nothing here, except for a poisonous gas you can't smell. "
                  "Within seconds you die. Game Over")
        else:
            print("Invalid choice, try again.")
    elif lake_choice == "swim":
        print("Look at you, a natural swimmer. Bad thing you didn't notice the sharks in the water. Game Over, "
              "but at least the sharks ate today.")
    else:
        print("Invalid choice, please try again.")
elif direction_choice == "right":
    print("You kept running and out of nowhere, you dont feel the ground. Hope you brought a parachute, "
          "or else you are falling to a certain death. Game Over.")
else:
    print("Invalid choice, try again")
