# 100 Days of Code | Day 25 | U.S. States Game

main.py was created for Day 25 of the 100 Days of Code: Python course from Dr. Angela Yu. This version of the application differs from the developed version of Dr. Yu's where I have opted to include a 'master key' that when enetered, solves the entire puzzle and ends the game. The user will need to enter the sequence '1111' into the prompt in order to intialize the program to solve itself.

As the user performs correct guesses of states, the program will write the name of the state using a Turtle object onto the canvas. The value that user enters will also be recorded in a separate list if it is a valid state. Once the user has completed guessing all 50 states, the program will end. The user also has the option of entering the sequence 'Exit' to end the program prematurely. If the program is ended prematurely, the list that appends the values that are recorded from the user will be compared aganist the state Data Frame from the orignal CSV. Any value that is left off is then appended to a new list with that new list being outputed to a CSV file.

## Program Requirements ##

1. Convert the guess to Title case.
2. Check if the guess is among the 50 states.
3. Write correct guesses onto the map.
4. Use a loop to allow the user ot keep guessing.
5. Record the correct guesses in a list.
6. Keep track of score.
