from turtle import Turtle, Screen
from random import randint, choice

tim = Turtle()
tim.shape('turtle')
tim.color('blue')

direction = [0, 90, 180, 270]

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# for i in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
screen = Screen()
screen.colormode(255)


def set_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    color = (r, g, b)
    return color


def draw_shapes(num_sides):
    angle = 360 / num_sides
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    for _ in range(num_sides):
        tim.pencolor(r, g, b)
        tim.forward(100)
        tim.right(angle)


def draw_circle():
    tim.pencolor(set_color())
    tim.circle(100)


def draw_spirograph(size_of_gap):
    tim.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        draw_circle()
        tim.setheading(tim.heading() + size_of_gap)


# for i in range(3, 11):
#     draw_shapes(i)

# for _ in range(40):
#     random_color = set_color()
#     tim.speed(10)
#     tim.pencolor(random_color)
#     tim.pensize(10)
#     tim.forward(50)
#     turn = choice(direction)
#     tim.setheading(turn)

draw_spirograph(10)

screen.exitonclick()
