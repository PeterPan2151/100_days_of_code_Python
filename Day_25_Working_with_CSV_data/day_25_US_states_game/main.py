import turtle
import pandas

# Setting up screen
screen = turtle.Screen()
screen.title('U.S States Game')
image = './blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Read the data from the CSV File
data = pandas.read_csv('./50_states.csv')

# needed for the logic of the program
correct_guesses = []
score = 0

# Loop to keep having the user playing
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f'{len(correct_guesses)}/50 States Correct',
                                    prompt='What\'s another state\'s name?').title()

    # Option to break the loop
    if answer_state == 'Exit':
        missing_states = []
        for state in list(data.state):
            if state not in correct_guesses:
                missing_states.append(state)
        # Create the CSV file with remaining states to learn
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('States_to_study.csv')
        break

    # check if a previous state has not been entered, if it has, continue, if not, do logic
    if answer_state not in correct_guesses:
        # Check is entered state is in the 'state' column form the CSV
        if answer_state in list(data.state):
            score += 1
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            # get the row with the entered state name
            state_data = data[data.state == answer_state]
            print(state_data.x.item())
            print(state_data.y.item())
            t.goto(state_data.x.item(), state_data.y.item())
            t.write(answer_state)
            correct_guesses.append(answer_state)

if score == 50:
    print('Great Work, you really know your states! Im impressed')
else:
    print("You have some study to do.")

screen.exitonclick()

