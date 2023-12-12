# Import packages.
import turtle
import pandas as pd

# Set up Screen
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Game")
turtle.bgpic(image)
screen.setup(725, 491)

# Declare/Initialize variables.
master_key = '1111'
correct_guesses = []
counter = 0
path = "missing_states.csv"
df = pd.read_csv("50_states.csv")
number_of_states = len(df['state'])

# Function initialization

# This function processes the input from the user along with other objects for the program.
def processInput(answer_state, counter, correct_guesses):

    # Check if input is on list of states or is master key.
    if answer_state in df.state.values:
        review = answer_state in df.state.values
        print(f"State: {answer_state}")
        ctrlFlow(answer_state)
        counter = prgCounter(answer_state, counter)
        correct_guesses.append(answer_state)
        print(f"Length of list: {len(correct_guesses)}")
        # Master key. All states will be printed.
    elif answer_state == master_key:
        print("Master key. All states will be printed.")
        correct_guesses = []
        correct_guesses = df['state'].to_list()
        ctrlFlow(answer_state)
        counter = prgCounter(answer_state, counter)
    # Return counter to be evaluated in loop.
    return counter

# Creates a list of states that was not guessed by the users and outputs to a CSV file.
def missingStates(df, correct_guesses):
    missing_states = []
    for state in df['state']:
        if state not in correct_guesses:
            missing_states.append(state)
            dfms = pd.DataFrame(missing_states)
            dfms.columns = ['state']
            dfms.to_csv(path, index=None)

# This function controls increments the counter.
def prgCounter(anwser_state, counter):
        # Master key. Counter will be set to 50 to end program.
         if anwser_state == master_key:
             counter = 50
             print("Counter: ", counter)
         else:
             counter = counter + 1
             print("Counter: ", counter)
         return counter

# This function controls the flow whether the master key is used or not.
def ctrlFlow(anwser_state):
    # Master key. All states will be printed.
    if anwser_state == master_key:
        for state in df['state']:
            printText(state)
    elif anwser_state in df.state.values:
        printText(anwser_state)

# This function prints the text on the canvas.
def printText(state):
    x = df.loc[df['state'] == state, "x"].values[0]
    y = df.loc[df['state'] == state, "y"].values[0]
    turtle.hideturtle()
    turtle.penup()
    turtle.setposition(x, y)
    turtle.write(state)

# While loop that will remain true as long as the counter is less than the value of number_of_states.
while counter != number_of_states:

    # Input from user.
    answer_state = screen.textinput(title=f"Guess the State {counter}/50", prompt="Please enter a state name below.").title()

    # Evaluate if user input is on the list of states. Pass the input, data frame, counter and list to function.
    if answer_state == 'Exit':
        missingStates(df, correct_guesses)
        break
    if answer_state != 'Exit':
        counter = processInput(answer_state,  counter, correct_guesses)
