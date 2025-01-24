import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
my_turtle = screen.textinput('Make your bet', 'Choose your turtle:')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if my_turtle:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == my_turtle:
                print(f'You won! The {winning_turtle} turtle won the race!')
            else:
                print(f'You lost. The {winning_turtle} turtle won the race!')
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()


