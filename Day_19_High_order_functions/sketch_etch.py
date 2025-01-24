from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_clockwise():
    position = tim.heading()
    position += 10
    tim.setheading(position)


def turn_anticlockwise():
    position = tim.heading()
    position -= 10
    tim.setheading(position)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=turn_anticlockwise, key='d')
screen.onkey(fun=turn_clockwise, key='a')
screen.onkey(fun=clear_screen, key='c')
screen.exitonclick()
