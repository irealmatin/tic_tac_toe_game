# Import the tkinter module
from tkinter import *
# Import the random module
import random

# Define the game board
#==========#
# 1|2|3
# - - -
# 4|5|6
# - - -
# 7|8|9
#==========#

#===========================Function==================================#

# Define a function to handle the next turn
def Next_Turn(i,j):

    # Declare that we are using the global variable 'player'
    global player

    # Check if the button is empty and if no winner has been found
    if buttons[i][j]['text'] == "" and Check_Winner() is False:

        # If player 1 is playing
        if player == players[0]:

            # Change the text of the button to player 1's symbol
            buttons[i][j]['text'] = player

            # If the game is not won, change the player
            if Check_Winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            # If player 1 wins, display winner
            elif Check_Winner() is True:
                label.config(text=(players[0]+" wins"))

            # If the game is a tie, display tie message
            elif Check_Winner() == "Tie":
                label.config(text="Tie!")

        # If player 2 is playing
        else:
            # Change the text of the button to player 2's symbol
            buttons[i][j]['text'] = player

            # If the game is not won, change the player
            if Check_Winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            # If player 2 wins, display winner
            elif Check_Winner() is True:
                label.config(text=(players[1]+" wins"))

            # If the game is a tie, display tie message
            elif Check_Winner() == "Tie":
                label.config(text="Tie!")

# Define a function to check if a player has won
def Check_Winner():
    
        # Check rows for win
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    
        # Check columns for win
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
        # Check diagonal top-left to bottom-right for win
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

        # Check diagonal top-right to bottom-left for win
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
        # if all buttoms full we set yellow color to show that the game was tie
    elif Empty_Spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

# define a function for empty space
def Empty_Spaces():
    Spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                Spaces -= 1

    if Spaces == 0:
        return False
    else:
        return True
# define a function for set a new game
def New_Game():

    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    # delete all last choices
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")
            
#=========================================Design===================================#

# Create a Tkinter window
root = Tk()
# Set the title of the window
root.title("Tic--Tac--Toe")
# Set the window to be non-resizable
root.resizable(0, 0)

# Create a 3x3 list of buttons to represent the game board
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# Set the color of window 
#root.configure(bg='blue')

# Define a list of players
players = ['X', 'O']
# Randomly choose the current player
player = random.choice(players)

# Create a label to display the current player's turn
label = Label(text=player + ' turn', font=('consolas', 30) )
# Place the label at the top of the window
label.pack(side='top')

# Create a reset button to start a new game
reset_button = Button(text="Reset", font=('consolas', 15),bg='gray', command=New_Game)
# Place the reset button at the top of the window
reset_button.pack(side='top')

# Create a frame to hold the buttons
frame = Frame(root)
# Place the frame in the window
frame.pack()

# Create a 3x3 grid of buttons
for i in range(3):
    for j in range(3):
        # Create a button with '-' as the default text
        buttons[i][j] = Button(frame, text='', font=('consolas', 30),
                               width=5, height=2,
                               command=lambda i=i, j=j: Next_Turn(i, j))
        # Place the button in the grid
        buttons[i][j].grid(row=i, column=j)




# Run the mainloop to start the game
root.mainloop()

