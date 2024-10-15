import tkinter as tk
from tkinter import messagebox


# Function to check if someone has won
def check_winner():
    # Horizontal
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]

    # Vertical
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    # No winner
    return None


# Function to handle button clicks
def on_click(row, col, winner=None):
    global turn

    if buttons[row][col]["text"] == "" and not winner:
        buttons[row][col]["text"] = turn
        board[row][col] = turn
        winner = check_winner()

        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
        elif all(board[row][col] != "" for row in range(3) for col in range(3)):
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        else:
            turn = "O" if turn == "X" else "X"


# Function to reset the game
def reset_game():
    global turn, board, winner
    turn = "X"
    winner = None
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""


# Initialize the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Variables
turn = "X"
winner = None
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

# Create buttons
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", width=10, height=3,
                                      font=("Arial", 24),
                                      command=lambda r=row, c=col: on_click(r, c))
        buttons[row][col].grid(row=row, column=col)

# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Start the Tkinter main loop
root.mainloop()
