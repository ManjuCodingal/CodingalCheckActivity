# Rock Paper Scissor App using Tkinter

import tkinter as tk
from tkinter import messagebox
import random

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissor App")
root.geometry("400x400")
root.configure(bg="lightblue")

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to play game
def play(user_choice):
    computer_choice = random.choice(choices)

    # Decide winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    # Display result
    result_label.config(
        text=f"Your Choice: {user_choice}\n"
             f"Computer Choice: {computer_choice}\n\n"
             f"{result}"
    )

# Heading
heading = tk.Label(
    root,
    text="Rock Paper Scissor Game",
    font=("Arial", 18, "bold"),
    bg="lightblue",
    fg="darkblue"
)
heading.pack(pady=20)

# Instruction Label
instruction = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 12),
    bg="lightblue"
)
instruction.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=20)

# Rock Button
rock_btn = tk.Button(
    button_frame,
    text="Rock",
    width=12,
    font=("Arial", 12),
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=10)

# Paper Button
paper_btn = tk.Button(
    button_frame,
    text="Paper",
    width=12,
    font=("Arial", 12),
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=10)

# Scissors Button
scissor_btn = tk.Button(
    button_frame,
    text="Scissors",
    width=12,
    font=("Arial", 12),
    command=lambda: play("Scissors")
)
scissor_btn.grid(row=0, column=2, padx=10)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="lightblue",
    fg="green"
)
result_label.pack(pady=30)

# Run the application
root.mainloop()