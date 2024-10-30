import tkinter as tk
from tkinter import messagebox

# Initialize the main game window
root = tk.Tk()
root.title("Tic Tac Toe")

# Game variables
current_player = "X"  # Player X always starts
buttons = [[None, None, None], [None, None, None], [None, None, None]]

# Function to check for a win or a tie
def check_winner():
    # Check rows, columns, and diagonals
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            declare_winner(buttons[i][0]["text"])
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            declare_winner(buttons[0][i]["text"])

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        declare_winner(buttons[0][0]["text"])

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        declare_winner(buttons[0][2]["text"])

    # Check for a tie
    if all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
        reset_game()

# Function to declare the winner
def declare_winner(player):
    messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
    reset_game()

# Function to handle button clicks
def button_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "" and current_player:
        buttons[row][col]["text"] = current_player
        check_winner()
        current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

# Create the buttons (grid) for the game
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                                  command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# Start the Tkinter event loop
root.mainloop()
